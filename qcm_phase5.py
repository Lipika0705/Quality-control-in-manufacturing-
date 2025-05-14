import random

# Simulated batch of 100 products with random lengths
batch_size = 100
product_lengths = [round(random.uniform(9.0, 11.0), 2) for _ in range(batch_size)]

# Acceptable length range
min_length = 9.5
max_length = 10.5

# Quality check
passed = []
failed = []

for i, length in enumerate(product_lengths, 1):
    if min_length <= length <= max_length:
        passed.append((i, length))
    else:
        failed.append((i, length))

# Summary report
print(f"Total products: {batch_size}")
print(f"Passed: {len(passed)}")
print(f"Failed: {len(failed)}")
print(f"Pass rate: {(len(passed)/batch_size) * 100:.2f}%")

# Optional: Show defective products
if failed:
    print("\nDefective products (ID, Length):")
    for product in failed:
        print(product)
else:
    print("\nNo defective products!")
