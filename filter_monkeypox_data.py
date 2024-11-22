import os
import pandas as pd

# Reading the dataset
file_path = 'data/raw_data/original/monkeypox_2022_5_to_2024_to_11.csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format
data['date'] = pd.to_datetime(data['date'])

# Request the user to input the year and month range
while True:
    try:
        # Input for start year and month
        start_year = int(input("Enter the start year (e.g., 2022): "))
        start_month = int(input("Enter the start month (1-12): "))

        # Input for end year and month
        end_year = int(input("Enter the end year (e.g., 2024): "))
        end_month = int(input("Enter the end month (1-12): "))

        # Validate input
        if start_month < 1 or start_month > 12 or end_month < 1 or end_month > 12:
            print("Month must be between 1 and 12. Please try again.")
        elif start_year > end_year or (start_year == end_year and start_month > end_month):
            print("The start date cannot be later than the end date. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter numeric year and month values (e.g., 2022 and 5 for May).")

# Filter the data for the selected year and month range
filtered_data = data[
    (data['date'].dt.year > start_year) | 
    ((data['date'].dt.year == start_year) & (data['date'].dt.month >= start_month)) & 
    (data['date'].dt.year < end_year) | 
    ((data['date'].dt.year == end_year) & (data['date'].dt.month <= end_month))
]

# Check if there is data for the selected year and month range
if filtered_data.empty:
    print(f"No data found for the range {start_month}/{start_year} to {end_month}/{end_year}.")
else:
    # Path to folder for saving the results
    output_folder = 'data/raw_data/filtered'
    os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist

    # Save the filtered data to a new file in the filtered folder
    output_file = os.path.join(output_folder, f'monkeypox_{start_year}_{start_month}_to_{end_year}_{end_month}_filtered.csv')
    filtered_data.to_csv(output_file, index=False)

    print(f"Data successfully filtered for the range {start_month}/{start_year} to {end_month}/{end_year}, and saved to: {output_file}")
