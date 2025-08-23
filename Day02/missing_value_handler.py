# reusable tool 

# Requirements
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

filepath = "C:\\Users\\Downloads\\titanic.csv"

# Creating functtion to reuse

def reusable_data_cleaner(filepath, strategy='mean',fill_object='Unknown'):
    # Load the csv into dataframe
    df = pd.read_csv(filepath)

    # Showing visualization before transformation
    sns.heatmap(df.isna(), cbar=False, cmap='viridis')
    plt.title('Missing Values Heatmap Before Cleaning')
    plt.show()

    # Missing values before cleaning
    print("Initial missing values:\n",df.isna().sum(), '\n')

    # Check the data type of all columns
    print("Data types of columns are:")
    for col in df.columns:
        print(col,':', df[col].dtype)
    print()
        
    # Filling the missing
    for col in df.columns:
        if df[col].isna().sum() > 0:
            if df[col].dtype in ['int64', 'float64']:
                ans = input(f'For column {col} enter mean, median or mode to replace missing value with: ').strip().lower()
                if ans == 'mean':
                    df.fillna({col :df[col].mean()}, inplace=True)
                    
                elif ans == 'median':
                    df.fillna({col :df[col].median()}, inplace=True)
                elif ans == 'mode':
                    df.fillna({col :df[col].mode()[0]}, inplace=True)
                else:
                    print("Invalid input for column", col, "Skipping...")
                
            elif df[col].dtype == 'object':
                df.fillna("Unknown", inplace=True)

    # Showing the rows that contain missing values
    missing_values = df[df.isna().any(axis=1)]
    print("Rows still containing missing values:",missing_values)
    
    # Dropping the row if all the data is missing
    df.dropna(how='all', inplace=True)
    
    # Missing values after cleaning
    print("Later missing values:\n",df.isna().sum(), '\n')

    # Visualization after cleaning
    sns.heatmap(df.isna(), cbar=False, cmap='viridis')
    plt.title("Missing Values Heatmap After Cleaning")
    plt.show()

    return df



cleaned_df = reusable_data_cleaner("C:\\Users\\Downloads\\titanic.csv")
print("\n Cleaned Data Preview", cleaned_df.head())


save_path = input("Enter the file path to save cleaned csv file or press 'Enter' to skip: ").strip()
if save_path:
    cleaned_df.to_csv(save_path, index=False)
    print(f"Cleaned data saved to {save_path}")
