from datasets import load_dataset
import pandas as pd

print("Downloading CodeXGLUE Defect Detection dataset...")

dataset = load_dataset(
    "google/code_x_glue_cc_defect_detection"
)

print("\nDataset Info:")
print(dataset)

# Convert train split to dataframe
train_df = pd.DataFrame(dataset["train"])

print("\nColumns:")
print(train_df.columns.tolist())

print("\nFirst 5 rows:")
print(train_df.head())

# Save locally
train_df.to_csv("dataset.csv", index=False)

print("\nDataset saved as dataset.csv")
print(f"Total samples: {len(train_df)}")

print("\nLabel Distribution:")
print(train_df["target"].value_counts())

print("\nSample Code:")
print(train_df.iloc[0]["func"])

print("\nLabel:")
print(train_df.iloc[0]["target"])
