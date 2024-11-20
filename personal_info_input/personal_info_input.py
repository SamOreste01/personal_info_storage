# Initiate a list for personal data
# Types of data(Full name, student id number, phone number, address(city), birthdate(mm/dd/yyyy))
# Define open/append txt file
# Define proper input
# Define ask user for another input

info = {}

full_name = str(input("Enter Full Name: "))
id_number = input("Enter your Student ID Number: ")
phone_num = input("Enter Phone Number: ")
address = input("Enter Address(City): ")
birthdate = input("Enter Birthdate(mm/dd/yyyy): ")

def open_txt_file():
    with open('personal_data', 'a') as file_handle:
        file_handle.write(full_name)
        file_handle.write(id_number)
        file_handle.write(phone_num)
        file_handle.write(address)
        file_handle.write(birthdate)


def valid_input():
    pass

def ask_input():
    pass








