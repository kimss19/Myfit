import pandas as pd

reference = pd.read_csv("data/reference_tops.csv")
target = pd.read_csv("data/target_tops.csv")

print("=== Reference Tops ===")
print(reference)

print("\n=== Target Tops ===")
print(target)