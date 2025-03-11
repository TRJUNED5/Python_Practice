age  = int(input("How old are u?:"))

if age == 100:
    print("You are century old")
elif age > 18:
    print("you are an adult")
elif age < 0:
    print("You haven't born yet")
else:
    print("You are a child")