# Initiate an array
# Ask user for full name
# Open txt file
# Search full name on txt file
# Ask user if they want to search another

entry = []

def name_lookup():
    while True:
        full_name = input("Enter full name of the person you're looking for: ") 
        if full_name == "":
            print("Please Enter a Name")
                 
        try:
            with open("personal_info.txt", "r") as file:
                for line in file:
                    if full_name in line:
                        entry.append(line)

                    else:
                        print(f"{full_name}'s Information was not found")
        
        except FileNotFoundError:
            print("File was not found")
        except Exception:
            print("An error occured")

        choice = input("Do you want to lookup for another person? (Y/N): ")
        if choice == "Y":
            continue
        else:
            print("Now Leaving the Program :D")
            break
        
name_lookup()
print(entry)