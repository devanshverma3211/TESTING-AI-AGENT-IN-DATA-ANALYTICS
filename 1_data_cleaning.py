import pandas as pd

def clean_tv_data(input_file, output_file):
    print(f"Loading {input_file}...")
    df = pd.read_csv(input_file)

    # 1. Fill missing overview values
    print("Filling missing overviews...")
    df['overview'] = df['overview'].fillna('No overview available.')

    # 2. Standardize first_air_date to datetime
    print("Standardizing dates...")
    df['first_air_date'] = pd.to_datetime(df['first_air_date'], errors='coerce')

    # 3. Trim whitespace from name and overview
    print("Trimming whitespace...")
    df['name'] = df['name'].str.strip()
    df['overview'] = df['overview'].str.strip()

    # Save the cleaned data
    df.to_csv(output_file, index=False)
    print(f"Success: Cleaned data saved to {output_file}")
    return df

if __name__ == "__main__":
    clean_tv_data('top_rated_tv.csv', 'top_rated_tv_cleaned.csv')
