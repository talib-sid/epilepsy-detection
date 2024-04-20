import pandas as pd

def clean_cols(input_csv, ref_cols):
    df = pd.read_csv(input_csv)
    cleaned = df.copy()
    cleaned.columns = cleaned.columns.str.strip("b'")  # Remove 'b' from column names

    # Extract channel names and remove columns accordingly
    cleaned_columns = cleaned.columns.tolist()

    dropp = [col for col in cleaned_columns if col.split()[-1][0] in ['G', 'F', 'I']]
    dropp += [col for col in cleaned_columns if any(ref in col for ref in ref_cols)]

    cleaned.drop(columns=dropp, inplace=True)

    cleaned.rename(columns={"Unnamed: 0": "Timestamp"}, inplace=True)
    cleaned.to_csv(input_csv.replace("_t.csv", "_clean.csv"), index=False,float_format='%.8f')



### File 081
ref1_cols = ["TBAL1","TBAL2"]
clean_cols("filter_data/081_t.csv", ref1_cols)


### File 131
ref2_cols = ["OPR5","OPR6"]
clean_cols("filter_data/131_t.csv", ref2_cols)
