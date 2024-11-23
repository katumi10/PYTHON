# while loop = execute some code while some condition remains true

# i = 1
# while i <= 10:
#      print(i * '*')
#      i = i + 1 

name = input("What is your name? : ")

while name == "":
    print("Please enter your name! ")
    name = input("What is your name? : ")

print(f"Hello {name}")





num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10 :
    print(f"{num} is not a valid number")
    num = int(input("Enter another number!: "))
print(f"{num} is a valid number ")     