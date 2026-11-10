# Product Code Parser
# The warehouse uses codes like CAT-SUB-BRAND-YEAR-SERIAL.

codes = ["ELE-LAP-HP-2026-0045", "FAS-SHO-NIK-2025-1203", "ELE-MOB-APL-2026-0007","GRO-RIC-INDIA-2024-0099x", "ELE-LAP-DEL-26-0010"]
valid_code = []
invaid_code = []
for code in codes:
    new_code = code.split("-")
    category = new_code[0]
    sub_category = new_code[1]
    brand = new_code[2]
    year = new_code[3]
    serial = new_code[4]


    if len(category) == 3:
        if len(sub_category) == 3:
            if len(brand) >= 2 and len(brand) <= 5:
                if len(year) == 4:
                    if int(year) >= 2020 and int(year) <= 2026:
                        if len(serial) == 4:
                            new_codes = category + "-" + sub_category + "-" + brand + "-" + year + "-" + serial
                            valid_code.append(new_codes)
                        else:
                            new_codes = category + "-" + sub_category + "-" + brand + "-" + year + "-" + serial
                            invaid_code.append(new_codes)
                    else:
                        new_codes = category + "-" + sub_category + "-" + brand + "-" + year + "-" + serial
                        invaid_code.append(new_codes)
                else:
                    new_codes = category + "-" + sub_category + "-" + brand + "-" + year + "-" + serial
                    invaid_code.append(new_codes)
            else:
                new_codes = category + "-" + sub_category + "-" + brand + "-" + year + "-" + serial
                invaid_code.append(new_codes)
        else:
            new_codes = category + "-" + sub_category + "-" + brand + "-" + year + "-" + serial
            invaid_code.append(new_codes)
    else:
        new_codes = category + "-" + sub_category + "-" + brand + "-" + year + "-" + serial
        invaid_code.append(new_codes)


print(f"Valid Codes : {valid_code}")
print(f"Invalid Codes : {invaid_code}")