registered_password = "ie29ej"
entered_password = ""

while entered_password != registered_password:
    entered_password = input("Please enter password: ")

    if entered_password != registered_password:
        print("Please input correct password")
    else:
        print("Access granted")


registered_password = "luka123."
entered_password = ""
attempts = 0

while entered_password != registered_password and attempts < 3:
    entered_password = input("Please enter password: ")
    # attempts = attempts + 1
    attempts += 1

    if entered_password != registered_password:
        print("Please input correct password")

        if attempts == 3:
            print("Attempts failed")
        else:
            print("You tried", attempts, "time")
    else:
        print("Access granted")