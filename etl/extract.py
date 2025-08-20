import pandas as pd

def extract(file_path: str) -> pd.DataFrame:
    """
    Load raw retail sales CSV into a Pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df
