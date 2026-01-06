# num= float(input("Enter a decimal value  : "))

# intger_part=int(num)
# farction_part=num-intger_part

# print("integer part : " , intger_part)
# print(f"fraction part : {farction_part} ")

# above solution causes floating point precision problem

from decimal import Decimal

num = Decimal(input("Enter s decimal value : "))
integer_part = int(num)
fraction_part = num - integer_part

print("integer part :", integer_part)
print("fraction part :", fraction_part)
