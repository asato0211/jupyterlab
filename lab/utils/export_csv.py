import csv

def export_csv(df, filename='output.csv'):
    df.to_csv(
        path_or_buf=filename,
        encoding='utf8',
        index=False,
        quoting=csv.QUOTE_NONNUMERIC
    )
