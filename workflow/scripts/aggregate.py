import pandas as pd
import glob

# Get input file paths from Snakemake
input_files = snakemake.input
output_file = snakemake.output[0]

# Initialize list to store data
data = []

# Read each input file and append the data to the list
for file in input_files:
    with open(file, 'r') as f:
        line = f.readline().strip()
        sample_name, file_path, file_size, md5_sum = line.split(',')
        data.append([sample_name, file_path, file_size, md5_sum])

# Create a DataFrame
df = pd.DataFrame(data, columns=['sample_name', 'file_path', 'file_size', 'md5_sum'])

# Write DataFrame to CSV
df.to_csv(output_file, index=False)
