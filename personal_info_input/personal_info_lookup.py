# Initiate an array
# Ask user for full name
# Open txt file
# Search full name on txt file
# Ask user if they want to search another

entry = []

def name_lookup():
    full_name = input("Enter full name of the person you're looking for: ") 

    with open("personal_info.txt", "r") as file:
        for line in file:
            if full_name in line:
                entry.append(line)

name_lookup()
print(entry)



