import pandas as pd

def clean_cols(input_csv, ref_cols):
    df = pd.read_csv(input_csv)

    # Remove columns based on reference column names or substrings
    dropp = [col for col in df.columns if any(sub in col for sub in ref_cols)]
    cleaned = df.drop(columns=dropp)
    
    cleaned.rename(columns={"Unnamed: 0": "Timestamp"}, inplace=True)
    cleaned.columns = cleaned.columns.str.replace("b'", "").str.replace("'", "")

    cleaned.to_csv(input_csv.replace("_t.csv", "_clean.csv"), index=False,float_format='%.8f')



### File 081
ref1_cols = ["TBAL1","TBAL2"]
clean_cols("filter_data/081_t.csv", ref1_cols)


### File 131
ref2_cols = ["OPR5","OPR6"]
clean_cols("filter_data/131_t.csv", ref2_cols)
