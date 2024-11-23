# format specifiers = {value:flags} format a value based on what
#                        flags are inserted

# : = insert a space before positive numbers

price1 = 12.345
price2 = 45.324
price3 = 78.98
# 1.  .(number)f = round to that many decimal places(fixed point)
#.2f indicates the number of decimal points/places to add
# f meaning floating point number
print(f"Price 1 is ${price1:.2f}")# $12.35
print(f"Price 2 is ${price2:.2f}")# $45.32
print(f"Price 3 is ${price3:.1f}")# $79.1

#2. :(number) = allocate that many spaces
print(f"Price 1 is ${price1:10}") # $       12.345
print(f"Price 2 is ${price2:13}") # $          45.324
print(f"Price 3 is ${price3:11}") # $        78.98

# :03 = allocate and zero pad that many spaces
#Precede a number with zero

print(f"Price 1 is ${price1:020}") #$0000000000000012.345
print(f"Price 2 is ${price2:010}") #$000045.324
print(f"Price 3 is ${price3:030}") #$00000000000000000000000078.98

#4. :< = left justify

print(f"Price 1 is ${price1:<10}") #Price 1 is $12.345
print(f"Price 2 is ${price2:<10}") #Price 2 is $45.324
print(f"Price 3 is ${price3:<1}")  #Price 3 is $78.98

#5. : = right justify

print(f"Price 1 is ${price1:>10}") #Price 1 is $    12.345
print(f"Price 2 is ${price2:>10}") #Price 2 is $    45.324
print(f"Price 3 is ${price3:>13}") #Price 3 is $       78.98

#6. :^ = center align

print(f"Price 1 is ${price1:^10}") #Price 1 is $  12.345
print(f"Price 2 is ${price2:^10}") #Price 2 is $  45.324
print(f"Price 3 is ${price3:^10}") #Price 2 is    78.98

#7. :+ = use a plus sign to indicate a positive value
print(f"Price 1 is ${price1:+}")# $+12.35
print(f"Price 2 is ${price2:+}")# $+45.32
print(f"Price 3 is ${price3:+}")# $+78.98

#8. := = place sign to leftmost position

print(f"Price 1 is ${price1:=}")# $12.35
print(f"Price 2 is ${price2:=}")# $45.32
print(f"Price 3 is ${price3:=}")# $78.98


#10. :, = comma seperator
#3,000.23

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")