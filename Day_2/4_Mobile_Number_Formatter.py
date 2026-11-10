# Mobile Number Formatter
# Phone numbers in a sales sheet come in many formats. Normalise them

raw = ["+91 98765-43210", "09876543210", "98765 43210", "(+91)9876543210", "12345", "98765abcde"]
digits = []

for numbers in raw:
    digits.append(numbers.replace("+91","").strip().replace(" ","").replace("-","").replace("()",""))

clean_list = []

for clean_num in digits:
    if clean_num[0] == "0":
        clean_list.append(clean_num.replace("0","",1))
    else:
        clean_list.append(clean_num)

formatted = []
for phone_numbers in clean_list:

    if len(phone_numbers) == 10:
        first_half = phone_numbers[:5]
        second_half = phone_numbers[5:]
        formatted_numbers = "+91" +" "+ first_half + " " + second_half
        formatted.append(formatted_numbers)

    

print(f"Valid Numbers : {formatted}")

