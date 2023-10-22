# is_good = False
#
# if is_good:
#     print(0.1 * 1000000)
# else:
#     print(0.2 * 1000000)

price = 1000000
is_good = False

if is_good:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")