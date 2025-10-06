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

def queryCollection(col: Collection, queries: dict, fields: dict):
    #print(f"Finding with queries: {queries}")
    res = col.find(queries, fields)
    for doc in col.find(queries, fields):
        #print(doc)
        pass
    return res.collection

def sortBy(col: Collection, sortByColumn: str, fields: dict, limit: int = 5, descending: bool = False):
    direction = pm.DESCENDING if descending else pm.ASCENDING
    cursor = col.find({}, fields).sort(sortByColumn, direction).limit(limit)
    for doc in cursor:
        print(doc)

def addFields(col: Collection, new_fields: dict, project_fields: dict):
    pipeline = [{ "$addFields": new_fields }, { "$project": project_fields }]
    cursor = col.aggregate(pipeline)
    for doc in cursor:
        #print(doc)
        pass

def main():
    col = createConnection("localhost", "27017", "root", "root", "star_database")

    lt = { "position.dist_PLX": { "$lt": 300 } }
    gt = { "features.Vr": { "$gt": 10 } }
    combined = { "$and": [lt, gt] }
    fields = { "_id": 0, "name": 1, "position.RA_ICRS": 1, "position.DE_ICRS": 1, "features.Vr": 1 }
    queried = queryCollection(col, combined, fields)

    query = "features.Vr"
    sortBy(queried, query, fields, 5, True)

    fields = { "position.sky_coord": [ "$position.RA_ICRS", "$position.DE_ICRS" ], "motion.flag": "fast_mover" }
    addFields(queried, fields, { "_id": 0, "name": 1, "position.sky_coord": 1, "motion.flag": 1 })

if __name__ == "__main__":
    main()

# Número de aluno: 66208 - Daniel Carvalho