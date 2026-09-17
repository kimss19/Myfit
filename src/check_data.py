import pandas as pd 

reference = pd.read_csv('data/reference_garments.csv')  # Load reference data
target = pd.read_csv('data/target_products.csv')  # Load target data

print("=== Reference Garments ===")
print(reference)

print("\n=== Target Garments ===")
print(target)

print("\nReference columns:")
print(reference.columns.tolist())