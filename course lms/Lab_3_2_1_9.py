secret_name = "chubacabra"
name = input("input the name: ")


while True:
    name = input("input the name: ")
    if name == secret_name:
        break

print("You've successfully left the loop.")

