def load_and_process(directory):
    df1 = (pd.read_csv(directory).drop(columns = ["price", "weekly_price"]))
    return df1
