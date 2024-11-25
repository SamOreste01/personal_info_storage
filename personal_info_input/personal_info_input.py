# Initiate a list for personal data
# Types of data(Full name, student id number, phone number, address(city), birthdate(mm/dd/yyyy))
# Define open/append txt file
# Define proper input: 
# Define ask user for another input

info = []
phone_digits = 11
id_number_digits = 15

def main():
    while True:
        try:
            full_name = str(input("Enter Full Name: "))
        except ValueError:
            ("Invalid Input!")
        
        while True:
            id_number = input("Enter your Student ID Number (ex. 2024-01234-MN-0): ")
            if len(id_number) == id_number_digits:
                break
            else: 
                print("You're id number must have 15 characters")

        while True:
            phone_num = input("Enter Phone Number: ") 
            if len(phone_num) == phone_digits:
                break
            else:
                print("You're phone number must be 11 digits")
        
        try:
            address = str(input("Enter your Address(City): "))
        except ValueError:
            ("Invalid Input!")

        try:
            birthdate = input("Enter your Birthdate(mm/dd/yyyy): ")
        except ValueError:
            ("Invalid Input!")

        choice = (input("Do you want to enter another entry? (Y/N): "))
        if choice == "Y":
            continue
        else:
            break

    user_input = [full_name, id_number, phone_num, address, birthdate]

    info.append(user_input)

def open_txt_file():
    pass

def ask_input():
    pass

main()
print(info)








