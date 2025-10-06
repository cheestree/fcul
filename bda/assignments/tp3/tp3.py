import json

import numpy as np
import pandas as pd
import pymongo as pm
from pymongo.database import Collection


def createConnection(host: str, port: str, user: str, password: str, collection: str):
    client = pm.MongoClient(f"mongodb://{user}:{password}@{host}:{port}/?authSource=admin")
    mydb = client["adb"]
    mycol = mydb[collection]
    return mycol

def insertDocuments(col: Collection, docs):
    if docs:
        result = col.insert_many(docs, ordered=False)
        print(f"Inserted {len(result.inserted_ids)} documents.")
    else:
        print("No documents to insert.")
    print("Total documents in collection:", col.count_documents({}))

def findAllDocuments(col: Collection):
    for doc in col.find():
        print(doc)

def queryCollection(col: Collection, queries: dict):
    print(f"Finding with queries: {queries}")
    for doc in col.find(queries):
        print(doc)

def sortLimit(col: Collection, column: str, limit: int = 10, descending: bool = False):
    direction = pm.DESCENDING if descending else pm.ASCENDING
    cursor = col.find().sort(column, direction).limit(limit)
    for doc in cursor:
        print(doc)

def updateDocuments(col: Collection, query: dict, operation: dict):
    res = col.update_many(query, operation)
    print(f"update_many matched={res.matched_count}, modified={res.modified_count}")
    return res

def deleteDocuments(col: Collection, query: dict):
    col.delete_many(query)

def aggregateMetalBins(col: Collection):
    pipeline = [
        {
            "$facet": {
                "avgAge": [
                    { "$group": { "_id": None, "avgAge": { "$avg": "$features.age" } } }
                ],
                "fehBins": [
                    {
                        "$group": {
                            "_id": {
                                "$switch": {
                                    "branches": [
                                        { "case": { "$lt": ["$features.FeH", -1] }, "then": "FeH < -1" },
                                        { "case": { "$and": [
                                            { "$gte": ["$features.FeH", -1] },
                                            { "$lte": ["$features.FeH", 0] }
                                        ] }, "then": "-1 =< FeH =< 0" }
                                    ],
                                    "default": "FeH > 0"
                                }
                            },
                            "count": { "$sum": 1 }
                        }
                    },
                    { "$sort": { "_id": 1 } }
                ],
                "distStats": [
                    { "$group": {
                        "_id": None,
                        "minDist": { "$min": "$position.dist_PLX" },
                        "maxDist": { "$max": "$position.dist_PLX" }
                    } }
                ]
            }
        }
    ]
    res = list(col.aggregate(pipeline))
    if not res:
        print("No aggregation results")
        return
    out = res[0]

    avg_age = out.get("avgAge", [])
    print(f"Average age: {avg_age[0]['avgAge'] if avg_age else None}")

    print("Metallicity bins (counts):")
    for b in out.get("fehBins", []):
        print(f"  {b['_id']}: {b['count']}")

    dist = out.get("distStats", [])
    if dist:
        print(f"Min dist_PLX: {dist[0]['minDist']}, Max dist_PLX: {dist[0]['maxDist']}")

def aggregateComputedFields(col: Collection):
    pipeline = [
        {
            "$project": {
                "features.radius_pc": { "$divide": ["$features.Diam_pc", 2] },
                "position.dist_ly": { "$multiply": [ "$position.dist_PLX", 3.26156 ]  },
                "_id": 0,
                "name": 1,
                "features.Diam_pc": 1,
            }
        }
    ]
    res = col.aggregate(pipeline)
    if not res:
        print("No aggregation results")
        return

    print("Sample with computed fields:")
    for doc in res:
        print(doc)

def projectionNestedFields(col: Collection, fields: dict):
    res = col.find({}, fields)
    if not res:
        print("No documents found")
        return

    print("Projection of nested fields:")
    for doc in res:
        print(doc)

def main():
    #   Exercise 1
    print("Exercise 1: Reading CSV and writing filtered JSON")
    df = pd.read_csv('dias_catalogue.csv')

    df['position'] = df[['RA_ICRS', 'DE_ICRS', 'Plx', 'dist_PLX']].apply(
        lambda s: s.to_dict(), axis=1
    )

    df['features'] = df[['r50', 'Vr', 'age', 'FeH', 'Diam_pc']].apply(
        lambda s: s.to_dict(), axis=1
    )

    #   Write out Name and features to a json file
    df[['name', 'position', 'features']].to_json("dias_catalogue_filtered.json", 
        orient = "records", 
        date_format = "iso", 
        double_precision = 10, 
        force_ascii = True, 
        date_unit = "ms", 
        default_handler = None, 
        indent=2
    )

    with open("dias_catalogue_filtered.json", "r", encoding="utf-8") as f:
        docs = json.load(f) 

        #   Exercise 2
        print("Exercise 2: Creating MongoDB connection")
        col = createConnection("localhost", "27017", "root", "root", "star_database")

        #   Exercise 3
        print("Exercise 3: Inserting documents into MongoDB")
        insertDocuments(col, docs)

        #   Exercise 4
        print("Exercise 4: Finding all documents")
        findAllDocuments(col)

        #   Exercise 5
        print("Exercise 5: Querying documents with conditions")
        gtAge = { "features.age": { "$gt": 5 } }
        ltPlx = { "position.dist_PLX": { "$lt": 100 } }
        ltFeh = { "features.FeH": { "$lt": -0.5 } }
        queryCollection(col, gtAge)
        queryCollection(col, ltPlx)
        queryCollection(col, ltFeh)
        combined = { "$and": [ gtAge, ltPlx ] }
        queryCollection(col, combined)

        #   Exercise 6
        print("Exercise 6: Sorting and limiting query results")
        sortLimit(col, "features.age", 3, descending=True)
        sortLimit(col, "position.dist_PLX", 5, descending=False)

        #   Exercise 7
        print("Exercise 7: Updating documents")
        updateDocuments(col, {}, {"$mul": {"features.Diam_pc": 2}})
        updateDocuments(col, {"features.FeH": {"$gt": 0}}, {"$set": {"features.luminosity": 1.0}})

        total_with_lum = col.count_documents({"features.luminosity": {"$exists": True}})
        print(f"Docs with features.luminosity present: {total_with_lum}")
        print("Sample (FeH > 0) with name, Diam_pc, luminosity:")
        for doc in col.find({"features.FeH": {"$gt": 0}}, {"_id": 0, "name": 1, "features.Diam_pc": 1, "features.luminosity": 1}).limit(3):
            print(doc)

        #   Exercise 8
        print("Exercise 8: Deleting documents")
        print(f"Documents pre deletion: {col.count_documents({})}")
        deleteDocuments(col, { "position.dist_PLX": { "$gt": 1000 } })
        deleteDocuments(col, { "name": "ASCC_10" })
        print(f"Documents post deletion: {col.count_documents({})}")

        #   Exercise 9
        print("Exercise 9: Aggregating documents")
        aggregateMetalBins(col)

        #   Exercise 10
        print("Exercise 10: Aggregating with computed fields")
        aggregateComputedFields(col)

        #   Exercise 11
        print("Exercise 11: Projection of nested fields")
        print("Show only name, RA_ICRS, DE_ICRS")
        projectionNestedFields(col, {"_id": 0, "name": 1, "position.RA_ICRS": 1, "position.DE_ICRS": 1})
        print("Show all fields except _id")
        projectionNestedFields(col, {"_id": 0})
        print("Exclude position.Plx field")
        projectionNestedFields(col, {"position.Plx": 0})


if __name__ == "__main__":
    main()