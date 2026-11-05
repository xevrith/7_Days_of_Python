# Login Attempt Guard
# A banking app must lock the account after repeated wrong passwords.

password = "admin@123"
attempts = 3

while attempts > 0:

    user_password = input("Enter your password : ")

    if user_password == " ":
        continue

    if user_password == password:
        print(f"Welcome")
        break

    else:
        print(f"Wrong Password")

        attempts -= 1
    print(f"{attempts} Attempts Left")


if attempts == 0:
    print(f"Access Locked")
