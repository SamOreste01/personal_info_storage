# Initiate a list for personal data
# Types of data(Full name, student id number, phone number, address(city), birthdate(mm/dd/yyyy))
# Define open/append txt file
# Define proper input: 
# Define ask user for another input

info = []
phone_digits = 11

full_name = str(input("Enter Full Name: "))
id_number = input("Enter your Student ID Number (ex. 2024-01234-MN-0): ")
phone_num = input("Enter Phone Number: ") 
if len(phone_num) != phone_digits:
    print("You're phone number must be 11 digits")
address = str(input("Enter your Address(City): "))
birthdate = input("Enter your Birthdate(mm/dd/yyyy): ")

user_input = [full_name, id_number, phone_num, address, birthdate]

info.append(user_input)

def open_txt_file():
    pass

def ask_input():
    pass

print(info)








