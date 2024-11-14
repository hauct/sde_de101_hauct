print(
    "################################################################################"
)
print("Use standard python libraries to do the transformations")
print(
    "################################################################################"
)

import csv
# Question: How do you read data from a CSV file at ./data/sample_data.csv into a list of dictionaries?
data = []
with open("./data/sample_data.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Question: How do you remove duplicate rows based on customer ID?
data_unique = []
customer_ids_seen = set()
for row in data:
    if row["Customer_ID"] not in customer_ids_seen:
        data_unique.append(row)
        customer_ids_seen.add(row["Customer_ID"])
    else:
        print(f'duplicate customer id {row["Customer_ID"]}')

# Question: How do you handle missing values by replacing them with 0?
for row in data_unique:
    if not row["Age"]:
        print(f'Customer {row["Customer_Name"]} does not have Age value')
        row["Age"] = 0
    if not row["Purchase_Amount"]:
        row["Purchase_Amount"] = 0.0

# Question: How do you remove outliers such as age > 100 or purchase amount > 1000?
data_cleaned = [
    row
    for row in data_unique
    if int(row["Age"]) <= 100 and float(row["Purchase_Amount"]) <= 1000
]

# Question: How do you convert the Gender column to a binary format (0 for Female, 1 for Male)?
for row in data_cleaned:
    if row["Gender"] == "Female":
        row["Gender"] = 0
    elif row["Gender"] == "Male":
        row["Gender"] = 1

# Question: How do you split the Customer_Name column into separate First_Name and Last_Name columns?
for row in data_cleaned:
    first_name, last_name = row["Customer_Name"].split(" ", 1)
    row["First_Name"] = first_name
    row["Last_Name"] = last_name
    del row["Customer_Name"]

# Question: How do you calculate the total purchase amount by Gender?
total_purchase_by_gender = {}
for row in data_cleaned:
    total_purchase_by_gender[row["Gender"]] += float(row["Purchase_Amount"])

# Question: How do you calculate the average purchase amount by Age group?
# assume age_groups is the grouping we want
# hint: Why do we convert to float?
age_groups = {"18-30": [], "31-40": [], "41-50": [], "51-60": [], "61-70": []}

# Question: How do you print the results for total purchase amount by Gender and average purchase amount by Age group?
your_total_purchase_amount_by_gender = {} # your results should be assigned to this variable
average_purchase_by_age_group = {} # your results should be assigned to this variable

print(f"Total purchase amount by Gender: {your_total_purchase_amount_by_gender}")
print(f"Average purchase amount by Age group: {average_purchase_by_age_group}")

print(
    "################################################################################"
)
print("Use DuckDB to do the transformations")
print(
    "################################################################################"
)

# Question: How do you connect to DuckDB and load data from a CSV file into a DuckDB table?
# Connect to DuckDB and load data

# Read data from CSV file into DuckDB table

# Question: How do you remove duplicate rows based on customer ID in DuckDB?

# Question: How do you handle missing values by replacing them with 0 in DuckDB?

# Question: How do you remove outliers (e.g., age > 100 or purchase amount > 1000) in DuckDB?

# Question: How do you convert the Gender column to a binary format (0 for Female, 1 for Male) in DuckDB?

# Question: How do you split the Customer_Name column into separate First_Name and Last_Name columns in DuckDB?

# Question: How do you calculate the total purchase amount by Gender in DuckDB?

# Question: How do you calculate the average purchase amount by Age group in DuckDB?

# Question: How do you print the results for total purchase amount by Gender and average purchase amount by Age group in DuckDB?
print("====================== Results ======================")
print("Total purchase amount by Gender:")
print("Average purchase amount by Age group:")
