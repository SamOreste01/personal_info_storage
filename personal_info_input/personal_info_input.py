# Initiate a list for personal data
# Types of data(Full name, student id number, phone number, address(city), birthdate(mm/dd/yyyy))
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
            full_name = str(input("Enter Full Name: "))
        except Exception:
            ("Invalid Input!")
        
        while True:
            id_number = input("Enter your Student ID Number (ex. 2024-01234-MN-0): ")
            if len(id_number) == id_number_digits:
                break
            else: 
                print("You're id number must have 15 characters, please follow the format given")

        while True:
            phone_num = input("Enter Phone Number: ") 
            if len(phone_num) == phone_digits:
                break
            else:
                print("You're phone number must be 11 digits")
        
        try:
            address = str(input("Enter your Address(City): "))
        except Exception:
            ("Invalid Input!")

        while True:
            birthdate = input("Enter your Birthdate(mm/dd/yyyy): ")
            if len(birthdate) == birthdate_charac:
                break
            else: 
                print("You're birthdate must have 10 characters, please follow the format given")

        choice = (input("Do you want to enter another entry? (Y/N): "))
        if choice == "Y":
            continue
        else:
            break

    user_input = f"{full_name}, {id_number}, {phone_num}, {address}, {birthdate}\n"
    info.append(user_input)

def file_handle():
    with open("personal_info.txt", "a") as file:
            file.writelines(info)
    print("All information was successfully saved to 'personal_info.txt'")


main()
file_handle()








