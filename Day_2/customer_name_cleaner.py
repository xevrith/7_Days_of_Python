# Customer Name Cleaner
# A CRM export has names typed by 20 different people.

raw = [" rAHul sHARMA ", "PRIYA singh", "amit kumar verma", " ", "sneha"]
print(f"Orginal List : {raw}")

clean_list = [name.strip().title() for name in raw]
print(f"Clean List : {clean_list}")



