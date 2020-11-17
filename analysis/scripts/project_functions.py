import pandas as pd

def load_and_process(directory):
    
    df1 = (pd.read_csv(directory)
          .dropna()
          )
    return df1
