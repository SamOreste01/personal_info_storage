# Ask user for full name
# Open txt file
# Initiate an array
# Search full name on txt file
# Append the found info into the array
# Ask user if they want to search another

def name_lookup():
    while True:
        full_name = input("Enter full name of the person you're looking for (e.g. Juan Dela Cruz): ") # Input full name who you want to look up
        if full_name == "":
            print("Please Enter a Name")
            continue
                 
        try:
            with open("personal_info.txt", "r") as file:
                entry = []
                for line in file:
                    if full_name in line:
                        fullname_in_file = line.split(",")[0].strip() # Assigns fullname_in_file as the fullname from the txt file
                        if fullname_in_file == full_name: # Compares fullname in file to fullname input
                            entry.append(line.strip()) 
                           
                if not entry:
                    print(f"{full_name}'s Information was not found")

                else:
                    print("Format: [Full Name, Id Number, Phone Number, City Address, Sex, Birthdate, Marital Status]")
                    print(f"{full_name}'s Information was found: {entry}")
        
        except FileNotFoundError:
            print("File was not found")
            break
        except Exception:
            print("An error occured")
            break

        choice = input("Do you want to lookup for another person? (Y/N): ")
        if choice == "Y":
            continue
        else:
            print("Now Leaving the Program :D")
            break
        
name_lookup()