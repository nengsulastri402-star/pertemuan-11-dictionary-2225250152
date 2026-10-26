data = {"nama": "Ayu", "nilai": 85, "kelas": "A"}

print("--- Menelusuri items() (Key dan Value) ---")
for key, value in data.items():
    print(f"{key}: {value}")

print("\n--- Menelusuri keys() ---")
for k in data.keys():
    print("Key:", k)

print("\n--- Menelusuri values() ---")
for v in data.values():
    print("Value:", v)
