import pandas as pd

def combine_columns(file_path, output_file_path):
    df = pd.read_csv(file_path, delimiter=';')

    df['Combined'] = 'Path: ' + df['Path'] + '\nSHA: ' + df['SHA3']

    df.to_csv(output_file_path, index=False)

input_file = '/Users/user/current_csv.csv'
output_file = '/Users/user/combined_csv.csv'

combine_columns(input_file, output_file)