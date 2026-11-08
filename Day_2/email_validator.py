# Email Validator (no regex)
# A newsletter tool must reject bad emails before sending

emails = ["rahul@gmail.com", "priya.singh@company.co.in", "amit@@mail.com", "sneha@gmail","@yahoo.com", "john doe@mail.com", "NEHA@Outlook.COM"]
valid = [email for email in emails if "@" in email and "." in email]