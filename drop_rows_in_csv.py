import pandas as pd

csv_path = "path_to_file.csv"
output_modified_csv_file_path = "modified_file_path.csv"
column_to_check = "Country"
if_different_from_then_drop_row = "France"

csv_file = pd.read_csv(csv_path)
indexes_to_drop = []
for i in range(len(csv_file)):
    if csv_file.get(column_to_check)[i] != if_different_from_then_drop_row:
        print(i)
        indexes_to_drop.append(i)

csv_dropped = csv_file.drop(indexes_to_drop)
csv_dropped.to_csv(output_modified_csv_file_path)