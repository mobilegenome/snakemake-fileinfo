# Snakemake Workflow for File Size and MD5 Checksum Aggregation

## Description

This Snakemake workflow processes a list of sample files, calculates their file sizes and MD5 checksums, and aggregates this information into a single CSV file. The input is a CSV file containing the sample names and file paths. The output is a CSV file containing the sample names, file paths, file sizes, and MD5 checksums.


## Files
Snakefile: Defines the workflow.
config.yaml: Contains the configuration parameters, including the paths to the input and output CSV files.
input_samples.csv: A CSV file containing the sample names and file paths.
scripts/aggregate.py: A Python script that aggregates the file size and MD5 checksum information into a CSV file.

## Installation
Install Snakemake if you haven't already:

bash
Copy code
conda install -c bioconda snakemake
Make sure you have Python installed. You can use Anaconda or Miniconda to manage your Python environment.

## Usage

### Prepare the input CSV file:

Create a file named input_samples.csv with the following format:

```csv

sample1,/path/to/sample1.txt
sample2,/path/to/sample2.txt
sample3,/path/to/sample3.txt
```

## Configure the workflow:

Edit the config.yaml file to specify the paths to the input and output CSV files:

```yaml
input_csv: input_samples.csv
output_csv: results/aggregate.csv
```

Run the workflow:

Navigate to the project directory and execute the following command:

```bash
snakemake --cores 1
```
This command will run the workflow using a single core.
