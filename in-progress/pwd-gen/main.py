from input_tools import lenght, pwd_conditions, menu_input
from password_tools import generate_password
from utils import pwd_title, title_separator, goodbye


def show_title():
    title_separator()
    print(pwd_title())
    title_separator()
    
def handle_pwd_gen():
    pwd_len = lenght()
    numbers_in_pwd = pwd_conditions()
    password = generate_password(pwd_len,numbers_in_pwd)
    print('Your generated password is: ' + password)
    

def menu():
    choice = menu_input()
    if choice == 1:
        handle_pwd_gen()
    return choice 

def main_loop():
    while True:
        show_title()
        choice = menu()
        if choice == 2:
            goodbye()
            break
        
if __name__ == '__main__':
    main_loop()