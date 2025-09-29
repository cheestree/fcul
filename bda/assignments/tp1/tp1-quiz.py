
import numpy as np
import pandas as pd

def main():
    csv = pd.read_csv('../dias_catalogue.csv')
    
    filtered = filterData(csv)
    createdAgeBins = createAgeBins(filtered)
    groupedAndSummerized = groupAndSummerize(createdAgeBins)
    sortedAndExported = sortAndExport(groupedAndSummerized)

    print(sortedAndExported)

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

if __name__ == "__main__":
    main()