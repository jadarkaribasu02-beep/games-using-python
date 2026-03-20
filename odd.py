num = (int(input("enter a number")))

def check_odd_even_bitwise(num):
    if (num & 1) == 0:
        return "even"
    else:
        return "odd"
print(f"The number {num} is {check_odd_even_bitwise(num)}.")
