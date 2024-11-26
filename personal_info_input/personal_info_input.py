# Initiate a list for personal data
# Types of data(Full name, student id number, phone number, address(city), Sex, birthdate(mm/dd/yyyy), Marital status)
# Define open/append txt file
# Define main that includes:
# Input standards, ask user for another input

info = []
phone_digits = 11
id_number_digits = 15
birthdate_charac = 10

def main():
    while True:
        try:
            full_name = str(input("Enter Full Name: ")) # Asks user for their full name
        except Exception:
            print("Invalid Input! Enter a valid Name")
        
        while True:
            id_number = input("Enter your Student ID Number (ex. 2024-01234-MN-0): ") # Asks user for their id number and restricts them to obey the given format
            if len(id_number) == id_number_digits:
                break
            else: 
                print("Your id number must have 15 characters, please follow the format given")

        while True:
            phone_num = input("Enter Phone Number: ")  # Asks user for their phone number and restricts them to 11 digits format
            if len(phone_num) == phone_digits:
                break
            else:
                print("Your phone number must be 11 digits")
        
        try:
            address = str(input("Enter your Address(City): ")) # Asks user for address
        except Exception:
            print("Invalid Input! Enter a valid Address")

        while True:
            print("M - male, F - Female, NA - Prefer not to say") #Asks user for sex
            sex = input("Enter your sex (M/F/NA): ")
            if sex in ["M", "F", "NA"]:
                break
            else:
                print("Invalid Input! Choose from M/F/NA")

        while True:
            birthdate = input("Enter your Birthdate(mm/dd/yyyy): ") # Asks user for their birthdate and restricts them to obey the given format
            if len(birthdate) == birthdate_charac:
                break
            else: 
                print("Your birthdate must have 10 characters, please follow the format given")

        while True:
            print("SI - Single, M - Married, W - Widowed, SP - Seperated") 
            marital_stat = input("Enter your Marital Status (SI/M/W/SP): ") # Asks user for marital status
            if marital_stat in ["SI", "M", "W", "SP"]:
                break
            else:
                print("Invalid Input! Choose from SI/M/W/SP")

        user_input = f"{full_name}, {id_number}, {phone_num}, {address}, {sex}, {birthdate}, {marital_stat}\n" 
        info.append(user_input)

        choice = (input("Do you want to enter another entry? (Y/N): ")) # Asks user if they want to input another or leave
        if choice == "Y":
            continue
        else:
            print("Now leaving the program :D")
            break

def file_handle():
    with open("personal_info.txt", "a") as file:
            file.writelines(info)
    print("All information was successfully saved to 'personal_info.txt'")

main()
file_handle()








