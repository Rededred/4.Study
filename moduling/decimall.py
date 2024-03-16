from decimal import Decimal

print(Decimal('0.1')*3)
print(float(Decimal('0.1')*3))

number = Decimal("0.446")
number = number.quantize(Decimal("0.00"))
print(number)

number = Decimal("0.999")
print(number.quantize(Decimal("1.00")))