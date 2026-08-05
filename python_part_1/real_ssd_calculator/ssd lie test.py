# How TB and GB lie to you
unit = input('Enter advertised Drive (TB/GB) : ').upper()

# Calculation
if unit == 'TB':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB':
    discrepancy = 1000000000 / 1073741824
else:
    print("Error: Please enter either TB or GB.")
    exit()

ad_cap = float(input('Enter the advertised capacity of that drive : '))

# Calculate the real capacity and round it
real_capacity = round(ad_cap * discrepancy, 2)

# Using an f-string for clean output
print(f'The actual capacity is {real_capacity} {unit}')