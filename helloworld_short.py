last_name = input("Enter your lastname: ")
first_name = input("Enter your firstname: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

# print("Hello, " + first_name + " " + last_name + "!")
print(f"Hello, {first_name} {last_name}! Your age is {age}.")

print(type(last_name))
print(type(age))
print(age + 2)
print(f'{(height + 0.1):.2f}')



