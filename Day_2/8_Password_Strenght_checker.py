# Password Strength Checker
# A sign-up form needs a strength meter.

tests = ["abc", "password123", "Rahul@2026", "Str0ng#Pass", "NoDigits!!", " Sp ace1!A"]
approve_password = {}
score = 0

for password in tests:

    if len(password) >= 8:
        score += 1
        approve_password[password] = score

        if any(char.isupper() for char in password):
            score += 1
            approve_password[password] = score

            if any(char.islower() for char in password):
                score += 1
                approve_password[password] = score

                if any(char.isdigit() for char in password):
                    score += 1
                    approve_password[password] = score

                    if "!@#$%^&*" in password:
                        score += 1
                        approve_password[password] = score

                    else:
                        score -= 1
                        approve_password[password] = score

                else:
                    score -= 1
                    approve_password[password] = score

            else:
                score -= 1
                approve_password[password] = score

        else:
            score -= 1
            approve_password[password] = score
    else:
        score -= 1
        approve_password[password] = score

new_records = {k: v for k,v in approve_password.items() if v > 0}
print(new_records)