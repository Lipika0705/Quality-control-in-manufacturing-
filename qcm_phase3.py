product_measurements = [9.8, 10.2, 10.0, 10.5, 9.7]

lower_limit = 9.5
upper_limit = 10.0

for i, measurement in enumerate(product_measurements, 1):
    if lower_limit <= measurement <= upper_limit:
        print(f"Product {i}: PASS ({measurement} mm)")
    else:
        print(f"Product {i}: FAIL ({measurement} mm)")
