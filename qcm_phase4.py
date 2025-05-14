lengths = [100.5, 99.0, 102.1, 98.7, 100.0]

target = 100.0
tolerance = 2.0

for i, length in enumerate(lengths, 1):
    if target - tolerance <= length <= target + tolerance:
        print(f"Product {i}: PASS")
    else:
        print(f"Product {i}: FAIL")
