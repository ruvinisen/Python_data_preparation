# import libraries
import pandas as pd
import os

# Specify the path to the folder
folder_path = '/content/test'

# Get a list of all files in the folder
file_names = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]
#file_names = os.listdir(folder_path)

# List to store DataFrames
dfs = []

# Create a folder to store CSV files if it doesn't exist
csv_folder = 'csv_output_1'
os.makedirs(csv_folder, exist_ok=True)

for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    df = pd.read_excel(file_path,sheet_name=0)

    # drop the 1st row
    df1= df.drop(0)

    # rename the columns
    new_column_names = ['location', '2G_cell_name', '2G_cell_id', '3G_cell_name','3G_cell_id', '4G_cell_name','4G_cell_id' ]
    df1.columns = new_column_names

    # deleting commas in the lacoation column
    df1['location'] = df1['location'].str.replace(',', '')

    # drop rows with no value in all the columns
    df1.dropna(axis=0, how="all" , inplace=True)

    # fill nan
    df1['location'] = df1['location'].fillna(method='ffill')

    # remove columns
    df3=df1.drop(columns=['2G_cell_id',  '3G_cell_id','4G_cell_id'])


    # Construct the full path for the CSV file
    csv_file = os.path.splitext(file_name)[0] + '.csv'
    csv_path = os.path.join(csv_folder, csv_file)

    # Save the DataFrame as a CSV file
    df3.to_csv(csv_path, index=False)

