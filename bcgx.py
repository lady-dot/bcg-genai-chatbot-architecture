import pandas as pd

# Creating the database dictionary with perfect column lengths (9 items each)
data = {
    "Company": [
        "Microsoft", "Microsoft", "Microsoft",
        "Tesla", "Tesla", "Tesla",
        "Apple", "Apple", "Apple"
    ],
    "Year": [2023, 2024, 2025, 2023, 2024, 2025, 2023, 2024, 2025],
    # Enter your extracted figures below (keep units consistent, e.g., in millions)
    "Total Revenue": [211915, 245122, 245122, 96773, 96773, 96773, 383285, 391035, 391035],
    "Net Income": [72361, 88136, 88136, 14997, 15000, 15000, 96995, 93736, 93736],
    "Total Assets": [411976, 512203, 512203, 104508, 110000, 110000, 352581, 365000, 365000],
    "Total Liabilities": [205749, 219110, 219110, 43009, 45000, 45000, 290437, 305000, 305000],
    "Cash Flow from Operating Activities": [87582, 118548, 118548, 13256, 14000, 14000, 110581, 115000, 115000]
}

# 1. Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# 2. Export directly to a clean CSV file
df.to_csv("financial_data.csv", index=False)
print("CSV File successfully created as 'financial_data.csv'!")