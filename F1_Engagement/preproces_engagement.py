import pandas as pd

def load_excel_file(file_path):
    """Load an Excel file and return a DataFrame."""
    try:
        df = pd.read_excel(file_path)
        print(f"Successfully loaded: {file_path}")
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def clean_numeric_column(series):
    """
    Convert like/comment counts like '56.3K', '774K' into actual integers.
    """
    def convert(val):
        try:
            val = str(val).upper().strip()
            if 'K' in val:
                return float(val.replace('K', '')) * 1_000
            elif 'M' in val:
                return float(val.replace('M', '')) * 1_000_000
            else:
                return float(val)
        except:
            return 0  # Fallback for missing/invalid values

    return series.apply(convert)

def calculate_engagement(df, likes_col, comments_col):
    """Calculate engagement as the sum of likes and comments."""
    df[likes_col] = clean_numeric_column(df[likes_col])
    df[comments_col] = clean_numeric_column(df[comments_col])
    
    df["Engagement"] = df[likes_col] + df[comments_col]
    return df

def save_to_excel(df, output_file):
    """Save the updated DataFrame to a new Excel file."""
    try:
        df.to_excel(output_file, index=False)
        print(f"Saved updated file to: {output_file}")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    # === Configuration ===
    file_path = 'mahirahkhan_instagram_data.xlsx'  # Update with actual path
    output_file = 'mahirahkhan_instagram_data.xlsx'
    likes_column = 'Likes'
    comments_column = 'Comments'

    # === Execution ===
    df = load_excel_file(file_path)
    if df is not None:
        df = calculate_engagement(df, likes_column, comments_column)
        save_to_excel(df, output_file)

if __name__ == "__main__":
    main()
