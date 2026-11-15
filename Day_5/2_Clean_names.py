# Clean Names with Comprehension
# Turn the loop from Day 2 into a single comprehension

def clean_list(data):
    clean_data = [name.strip().title() for name in data if len(name) > 1]
    return clean_data


raw = [" rahul SHARMA ", "", "PRIYA singh", " ", "amit verma"]
print(f"Clean Data : {clean_list(raw)}")



