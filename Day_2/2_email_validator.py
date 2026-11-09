# Email Validator (no regex)
# A newsletter tool must reject bad emails before sending

emails = ["rahul@gmail.com", "priya.singh@company.co.in", "amit@@mail.com", "sneha@gmail","@yahoo.com", "john doe@mail.com", "NEHA@Outlook.COM"]
valid = []
invaid = []


for email in emails:
    if "@" in email:
        if email.count("@") == 1:
            if email[0] != "@":
                if " " not in email:
                    if email[0] != ".":
                        valid.append(email.lower())

                    else:
                        invaid.append(email.lower())
                else:
                    invaid.append(email.lower())
            else:
                invaid.append(email.lower())
        else:
            invaid.append(email.lower())
    else:
        invaid.append(email.lower())

print(f"Valid Email : {valid}")
print(f"Invalid Email : {invaid}")