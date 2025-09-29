import numpy as np
import pandas as pd


def main1():
    print("Welcome to the CSV Data CLI!")
    file_name = input("Enter the CSV file name (default: dias_catalogue.csv): ") or "dias_catalogue.csv"
    try:
        csv = pd.read_csv(file_name)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    while True:
        print("\nMenu:")
        print("1. Show first five rows")
        print("2. Show dataset info")
        print("3. Select columns and show rows")
        print("4. Filter rows (Plx > 1)")
        print("5. Show missing values per column")
        print("6. Show summary statistics for Diam_pc")
        print("7. Group by flagdispPM and show mean sigPM")
        print("8. Add DistMod column")
        print("9. Save selected columns to file")
        print("0. Exit")
        choice = input("Choose an option: ")

        try:    
            if choice == "1":
                number = int(input("How many rows to show? (default: 5)"))
                firstFive(csv, number)
            elif choice == "2":
                datasetInfo(csv)
            elif choice == "3":
                cols = input("Enter columns separated by commas: (default: RA_ICRS, DE_ICRS)").split(",")
                cols = [c.strip() for c in cols]
                length = int(input("How many rows to show? (default: 10)"))
                selectColumns(csv, cols, length)
            elif choice == "4":
                cols = input("Enter columns separated by commas: (default: name, Plx, dist_PLX)").split(",")
                cols = [c.strip() for c in cols]
                filtering(csv, cols)
            elif choice == "5":
                cols = input("Enter columns separated by commas: (default: age)").split(",")
                number = int(input("How many rows to show? (default: 5)"))
                sorting(csv, cols, number)
            elif choice == "6":
                handlingNaN(csv)
            elif choice == "7":
                col = input("Enter column: (default: Diam_pc)").split(",")[0]
                summary(csv, col)
            elif choice == "8":
                grouping(csv, 'flagdispPM')
            elif choice == "9":
                addColumn(csv, 'DistMod')
            elif choice == "10":
                cols = input("Enter columns to save, separated by commas: ").split(",")
                cols = [c.strip() for c in cols]
                fname = input("Enter output file name (without .csv): ")
                saveColumnsToFile(csv, cols, fname)
            elif choice == "0":
                print("Exiting.")
                break
            else:
                print("Invalid option. Please try again.")
        except:
            print("An exception occurred")

def firstFive(csv: pd.DataFrame, length: int = 5):
    firstFive = csv.head(length)
    print(firstFive)


def datasetInfo(csv: pd.DataFrame):
    info = csv.info()
    shape = csv.shape
    print(f"Shape: {shape}")
    print(info)

def selectColumns(csv: pd.DataFrame, columns: list[str] = ["RA_ICRS", "DE_ICRS"], length: int = 10):
    columnsInfo = csv[columns]
    firstFive = columnsInfo.head(length)
    print(firstFive)

def filtering(csv: pd.DataFrame, columns: list[str] = ["name", "Plx", "dist_PLX"]):
    filtered = csv[csv['Plx'] > 1]
    columnsInfo = filtered[columns]
    length = columnsInfo.count()
    print(filtered[columns])
    print(f"Total columns: {length}")

def sorting(csv: pd.DataFrame, sortBy: list[str], length: int = 5):
    sorted = csv.sort_values(sortBy)
    firstFive = sorted.head(length)
    print(firstFive)

def handlingNaN(csv: pd.DataFrame):
    nulls = csv.isnull().sum()
    print(nulls)

def summary(csv: pd.DataFrame, column: str = "Diam_pc"):
    mean = csv[column].mean()
    median = csv[column].median()
    std = csv[column].std()
    print(f"Statistics of column {column}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard deviation: {std}")

def grouping(csv: pd.DataFrame, groupBy: str):
    group = csv.groupby(groupBy)['sigPM'].mean()
    print(group)

def addColumn(csv: pd.DataFrame, columnName: str):
    csv[columnName] = 5*np.log10(csv['dist_PLX'])-5
    print(f"Column added")
    print(csv[columnName])

def saveColumnsToFile(csv: pd.DataFrame, columns: list[str], fileName: str):
    selectedColumns = csv[columns]
    selectedColumns.to_csv(fileName+'.csv', index=False)

#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -#
#
#                                       TP1
#
#-  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -#

def filterData(csv: pd.DataFrame):
    filtered = csv[~csv['age'].isna() & ~csv['FeH'].isna()]
    return filtered


def createAgeBins(csv: pd.DataFrame):
    conditions = [
        (csv['age'] < 100),
        (csv['age'] >= 100) & (csv['age'] < 1000),
        (csv['age'] >= 1000)
    ]
    choices = ['Young', 'Intermediate', 'Old']
    csv['AgeClass'] = np.select(conditions, choices, default='Unknown')
    return csv


def groupAndSummerize(csv: pd.DataFrame):
    grouped = csv.groupby('AgeClass')['FeH'].agg(
        Mean_FeH='mean',
        Std_FeH='std',
        Count='count'
    ).reset_index()
    return grouped

def sortAndExport(csv: pd.DataFrame):
    sorted = csv.sort_values('Mean_FeH', ascending=False)
    selectColumns = sorted[['AgeClass', 'Mean_FeH', 'Std_FeH', 'Count']]
    selectColumns.to_csv('metallicity_summary.csv')

    return selectColumns

def main():
    csv = pd.read_csv('dias_catalogue.csv')
    filtered = filterData(csv)
    createdAgeBins = createAgeBins(filtered)
    groupedAndSummerized = groupAndSummerize(createdAgeBins)
    sortedAndExported = sortAndExport(groupedAndSummerized)

    print(sortedAndExported)


if __name__ == "__main__":
    main()