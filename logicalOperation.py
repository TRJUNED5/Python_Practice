temp = int(input("What is the temperature: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today!")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("the temperature if bad today")
    print("stay inside")
