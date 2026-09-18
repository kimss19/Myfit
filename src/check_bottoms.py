import pandas as pd

reference = pd.read_csv("data/reference_bottoms.csv")
target = pd.read_csv("data/target_bottoms.csv")

ref = reference.iloc[0]

print("=== Reference Bottom ===")
print(ref)

print("\n=== Target Bottom Comparison ===")

for _, row in target.iterrows():
    waist_diff = row["waist"] - ref["waist"]
    rise_diff = row["rise"] - ref["rise"]
    thigh_diff = row["thigh"] - ref["thigh"]
    hem_diff = row["hem"] - ref["hem"]
    length_diff = row["length"] - ref["length"]

    print(f"\nSize: {row['size']}")
    print(f"Waist difference: {waist_diff:+.1f} cm")
    print(f"Rise difference: {rise_diff:+.1f} cm")
    print(f"Thigh difference: {thigh_diff:+.1f} cm")
    print(f"Hem difference: {hem_diff:+.1f} cm")
    print(f"Length difference: {length_diff:+.1f} cm")