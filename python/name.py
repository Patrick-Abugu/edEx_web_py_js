my_name = input("Name: ")
my_age = int(input("Age: "))
print(f"You are: {my_name}.")
if my_age == 0:
    print("Age cannot be zero")
elif my_age >= 26:
    print(f"Wow! you are getting old mate. You are {my_age} years old alraedy!")
else:
    print(f"You are still {my_age} years old, but start thinking about your life.")

