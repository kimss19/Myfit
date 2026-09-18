import pandas as pd
from silhouette_profiles import BOTTOM_SILHOUETTE_PROFILES

reference = pd.read_csv("data/reference_bottoms.csv")
target = pd.read_csv("data/target_bottoms.csv")

# 기준 옷 1개
ref = reference.iloc[0]

# 이번에 원하는 착용 방식
# options:
# fitted
# true_to_design
# relaxed
print("이번 옷을 어떻게 입고 싶나요?")
print("1. fitted")
print("2. true_to_design")
print("3. relaxed")

choice = input("번호를 선택하세요 (1/2/3): ")

preference_map = {
    "1": "fitted",
    "2": "true_to_design",
    "3": "relaxed"
}

wearing_preference = preference_map.get(choice)

if wearing_preference is None:
    print("잘못된 입력입니다.")
    exit()


print("=== Reference Garment ===")
print(f"Category: {ref['subcategory']}")
print(f"Silhouette: {ref['silhouette']}")
print(f"Perceived fit: {ref['perceived_fit']}")
print(f"User rating: {ref['user_rating']}")

print("\n=== Target Garment ===")

for _, row in target.iterrows():

    print(f"\nSize: {row['size']}")
    print(f"Target silhouette: {row['silhouette']}")
    print(f"Wearing preference: {wearing_preference}")

    differences = {
        "waist": row["waist"] - ref["waist"],
        "rise": row["rise"] - ref["rise"],
        "thigh": row["thigh"] - ref["thigh"],
        "hem": row["hem"] - ref["hem"],
        "length": row["length"] - ref["length"],
    }

    print("\nMeasurement differences:")

    for feature, value in differences.items():
        print(f"{feature}: {value:+.1f} cm")
        
    target_silhouette = row["silhouette"]

    profile = BOTTOM_SILHOUETTE_PROFILES[target_silhouette]

    print("\n=== Silhouette Profile ===")
    print(f"Silhouette: {target_silhouette}")
    print("Weights:")

    for feature, weight in profile["weights"].items():
        print(f"  {feature}: {weight}")
        
    