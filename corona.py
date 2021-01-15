import pandas as pd
data_df = pd.read_csv('https://raw.githubusercontent.com/rs-delve/covid19_datasets/master/dataset/combined_dataset_latest.csv', parse_dates=['DATE'])

country_name = input("Enter Your Country Name: ")

print(data_df[data_df['country_name'] == f"{country_name}"])