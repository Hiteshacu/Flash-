name = 'Hitesh'
age=20
b = True
print(type(name))
print(type(age))
print(type(b))

name = input("Enetr your name: ")
print("Hello",name)

age = int(input("Enter your age: "))
if age >= 18: print("You are eligible to vote.")
elif age >=21: print("You are eligible to vote and clubbing")
else: print("You are a kid.")