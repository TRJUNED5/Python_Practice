#while loop

#while 1==1:
#    print("Help! I'm stuck in a loop")

name = ""

#same
#while len(name) == 0:
while not name:
    name = input("Enter your name: ")

print("Hello "+name)