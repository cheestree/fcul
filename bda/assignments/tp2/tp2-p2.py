import pandas as pd


def readCSV(file_name: str):
    try:
        csv = pd.read_csv(file_name)
    except Exception as e:
        raise Exception(f"Error loading file {e}")
    return csv

def selectColumns(csv: pd.DataFrame, columns: list[str]):
    selectedColumns = csv[columns]
    print(selectedColumns)

def filterRowsByAge(csv: pd.DataFrame, threshold: int):
    rows = csv[csv['age'] > threshold]
    print(rows)

def sortBy(csv: pd.DataFrame, sortBy: str, limit: int):
    rows = csv.sort_values(by=sortBy)
    print(rows.head(limit))

def aggregate(csv: pd.DataFrame, column: str, threshold: int):
    filtered = csv[csv['N'] > threshold]
    avg = filtered[column].mean()
    print(avg)

def groupingCounting(csv: pd.DataFrame, conditions: pd.Series):
    filtered = csv[conditions]
    count = filtered.count
    print(count)

def main():
    csv = readCSV("../dias_catalogue.csv")

    #   Exercise 1
    print("Exercise 1")
    selectColumns(csv, ['name', 'RA_ICRS', 'DE_ICRS', 'Vr', 'Plx'])

    #   Exercise 2
    print("Exercise 2")
    filterRowsByAge(csv, 1)

    #   Exercise 3
    print("Exercise 3")
    sortBy(csv, 'Plx', 10)

    #   Exercise 4
    print("Exercise 4")
    aggregate(csv, 'FeH', 10)

    #   Exercise 5
    print("Exercise 5")
    groupingCounting(csv, (csv['flagdispPM'] == 1) & (csv['sigPM'] > 2))

if __name__ == "__main__":
    main()