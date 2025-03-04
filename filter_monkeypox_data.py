import os
import pandas as pd

# Request the user to input the year and month range to process data
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

# Reading the dataset
data_file = f"monkeypox_{start_year}_{start_month}_to_{end_year}_{end_month}"
file_path = f'data/raw/original/{data_file}.csv'
data = pd.read_csv(file_path)

# Ensure the 'date' column is in datetime format
data['date'] = pd.to_datetime(data['date'])

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
    # New input for the range to save the data
    while True:
        try:
            # Input for new start year and month for saving
            new_start_year = int(input("Enter the new start year for saving (e.g., 2022): "))
            new_start_month = int(input("Enter the new start month for saving (1-12): "))
            
            # Input for new end year and month for saving
            new_end_year = int(input("Enter the end year (e.g., 2024): "))
            new_end_month = int(input("Enter the end month (1-12): "))
            
            # Validate the new start year and month input
            if new_start_month < 1 or new_start_month > 12 or new_end_month < 1 or new_end_month > 12:
                print("Month must be between 1 and 12. Please try again.")
            elif new_start_year < start_year or (new_start_year == start_year and new_start_month < start_month):
                print("The new start date for saving cannot be earlier than the original start date. Please try again.")
            elif new_end_year < new_start_year or (new_end_year == new_start_year and new_end_month < new_start_month):
                print("The new end date for saving cannot be earlier than the new start date. Please try again.")
            elif new_end_year > end_year or (new_end_year == end_year and new_end_month > end_month):
                print("The new end date for saving cannot be later than the original end date. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter numeric year and month values (e.g., 2022 and 5 for May).")
    
    # Path to folder for saving the results
    output_folder = 'data/raw/filtered'
    os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist

    # Save the filtered data to a new file in the filtered folder with new start year and month for saving
    output_file = os.path.join(output_folder, f'monkeypox_{new_start_year}_{new_start_month}_to_{new_end_year}_{new_end_month}_filtered.csv').replace("\\", "/")
    filtered_data.to_csv(output_file, index=False)

    print(f"Data successfully filtered for the range {start_month}/{start_year} to {end_month}/{end_year}, and saved to: {output_file}")
