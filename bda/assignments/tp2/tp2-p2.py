import pandas as pd


def readCSV(file_name: str):
    try:
        csv = pd.read_csv(file_name)
    except Exception as e:
        print(f"Error loading file: {e}")
        return
    return csv

def selectColumns(csv: pd.DataFrame, columns: list[str]):
    columns = csv[columns]
    print(columns)

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

def groupingCounting(csv: pd.DataFrame, conditions):
    filtered = csv[conditions]
    count = filtered.count
    print(count)

def main():
    csv = readCSV("dias_catalogue.csv")

    selectColumns(csv, ['name', 'RA_ICRS', 'DE_ICRS', 'Vr', 'Plx'])
    filterRowsByAge(csv, 1)
    sortBy(csv, 'Plx', 10)
    aggregate(csv, 'FeH', 10)
    groupingCounting(csv, (csv['flagdispPM'] == 1) & (csv['sigPM'] > 2))

if __name__ == "__main__":
    main()