import pandas as pd
import os


def combine_csv_files(folder_path):
    """
    read all csv files in given path and combines them to one DataFrame
    args: path to folder with the csv-files (str)
    returns: combined DataFrame (pandas.DataFrame)
    """

    # collect dataframes in list
    dataframes = []
    for file in [f for f in os.listdir(folder_path) if f.endswith('.csv')]:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path, delimiter=';')
        dataframes.append(df)

    # concatenate DataFrames
    # fill missing data with "unknown"
    combined_df = pd.concat(dataframes).fillna('unknown')
    combined_df = combined_df.fillna('unknown')

    return combined_df



def main():
    path = 'resources'
    combined_df = combine_csv_files(path)
    combined_df.to_csv(os.path.join(path, 'combined.csv'), index=False, sep=';')
    print("combined dataframe saved in combined.csv")

if __name__ == "__main__":
    main()
