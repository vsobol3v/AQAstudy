age = 26
name = "Alex"
if age == 25 or name == "Alex":
    print(f"Im {age} years old, my name is {name}")
elif age > 25:
    print("Im older than 25")
else:
    print("Im younger than 25")

name = "Alex"
if "m" in name:
    print(f"My name is {name}")
else:
    print(f"My name is not {name}")

pin = 1234
attempts_const = 3
user_pin = int(input("Enter your PIN "))

def check(user_pin, attempts):
    if pin == user_pin:
        print("Enter sum")
    else:
        attempts = attempts - 1
        if attempts != 0:
            print(f'PIN is incorrect. {attempts} attempts left')
            user_pin = int(input("Enter your PIN "))
            check(user_pin, attempts)
        else:
            print("PIN is incorrect. Your card has been blocked")


check(user_pin, attempts_const)
