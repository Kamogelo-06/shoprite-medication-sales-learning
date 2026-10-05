import pandas as pd

df = pd.read_csv("medirite_public_products.csv")
print(df)
print("\n--- Total categories:", len(df))
