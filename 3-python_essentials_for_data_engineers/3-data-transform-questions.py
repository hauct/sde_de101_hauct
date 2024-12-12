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

# print(data)
# Question: How do you remove duplicate rows based on customer ID?
data_unique = []
customer_ids_seen = set()
for row in data:
    if row["Customer_ID"] not in customer_ids_seen:
        data_unique.append(row)
        customer_ids_seen.add(row["Customer_ID"])
    else:
        print(f'duplicate customer id {row["Customer_ID"]}')

# print(data_unique)

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

# # Question: How do you calculate the total purchase amount by Gender?
total_purchase_by_gender = {0: 0.0, 1: 0.0}
for row in data_cleaned:
    gender = row["Gender"]
    total_purchase_by_gender[gender] += float(row["Purchase_Amount"])

print(total_purchase_by_gender)
# Question: How do you calculate the average purchase amount by Age group?
# assume age_groups is the grouping we want
# hint: Why do we convert to float?
age_groups = {"18-30": [], "31-40": [], "41-50": [], "51-60": [], "61-70": []}
for row in data_cleaned:
    age = int(row["Age"])
    if age <= 30:
        age_groups["18-30"].append(float(row["Purchase_Amount"]))
    elif age <= 40:
        age_groups["31-40"].append(float(row["Purchase_Amount"]))
    elif age <= 50:
        age_groups["41-50"].append(float(row["Purchase_Amount"]))
    elif age <= 60:
        age_groups["51-60"].append(float(row["Purchase_Amount"]))
    else:
        age_groups["61-70"].append(float(row["Purchase_Amount"]))

average_purchase_by_age_group = {
    group: sum(amounts) / len(amounts) for group, amounts in age_groups.items()
}

# Question: How do you print the results for total purchase amount by Gender and average purchase amount by Age group?

print(f"Total purchase amount by Gender: {total_purchase_by_gender}")
print(f"Average purchase amount by Age group: {average_purchase_by_age_group}")

print(
    "################################################################################"
)
print("Use DuckDB to do the transformations")
print(
    "################################################################################"
)

# Question: How do you connect to DuckDB and load data from a CSV file into a DuckDB table?
import duckdb

# Connect to DuckDB and load data
con = duckdb.connect(database=':memory:', read_only=False)

# Read data from CSV file into DuckDB table
con.execute("CREATE TABLE data AS SELECT * FROM read_csv_auto('./data/sample_data.csv')")

# Question: How do you remove duplicate rows based on customer ID in DuckDB?
con.execute("CREATE TABLE data_unique AS SELECT DISTINCT ON (Customer_ID) * FROM data")

# Question: How do you handle missing values by replacing them with 0 in DuckDB?
con.execute("""
    UPDATE data_unique
    SET Age = COALESCE(Age, 0),
        Purchase_Amount = COALESCE(Purchase_Amount, 0.0)
""")

# Question: How do you remove outliers (e.g., age > 100 or purchase amount > 1000) in DuckDB?
con.execute("""
    CREATE TABLE data_cleaned AS
    SELECT * FROM data_unique
    WHERE Age <= 100 AND Purchase_Amount <= 1000
""")

# Question: How do you convert the Gender column to a binary format (0 for Female, 1 for Male) in DuckDB?
con.execute("""
    UPDATE data_cleaned
    SET Gender = CASE WHEN Gender = 'Female' THEN 0 ELSE 1 END
""")

# Question: How do you split the Customer_Name column into separate First_Name and Last_Name columns in DuckDB?
con.execute("""
    ALTER TABLE data_cleaned
    ADD COLUMN First_Name VARCHAR
""")
con.execute("""
    ALTER TABLE data_cleaned
    ADD COLUMN Last_Name VARCHAR
""")
con.execute("""
    UPDATE data_cleaned
    SET First_Name = SPLIT_PART(Customer_Name, ' ', 1),
        Last_Name = SPLIT_PART(Customer_Name, ' ', 2)
""")
con.execute("ALTER TABLE data_cleaned DROP COLUMN Customer_Name")

# Question: How do you calculate the total purchase amount by Gender in DuckDB?
total_purchase_by_gender = con.execute("""
    SELECT Gender, SUM(Purchase_Amount) AS Total_Purchase
    FROM data_cleaned
    GROUP BY Gender
""").fetchall()

# Question: How do you calculate the average purchase amount by Age group in DuckDB?
average_purchase_by_age_group = con.execute("""
    SELECT
        CASE
            WHEN Age BETWEEN 18 AND 30 THEN '18-30'
            WHEN Age BETWEEN 31 AND 40 THEN '31-40'
            WHEN Age BETWEEN 41 AND 50 THEN '41-50'
            WHEN Age BETWEEN 51 AND 60 THEN '51-60'
            WHEN Age BETWEEN 61 AND 70 THEN '61-70'
        END AS Age_Group,
        AVG(Purchase_Amount) AS Average_Purchase
    FROM data_cleaned
    GROUP BY Age_Group
""").fetchall()

# Question: How do you print the results for total purchase amount by Gender and average purchase amount by Age group in DuckDB?
print("====================== Results ======================")
print("Total purchase amount by Gender:", total_purchase_by_gender)
print("Average purchase amount by Age group:", average_purchase_by_age_group)
