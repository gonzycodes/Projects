#Error management and user input

def menu_input() -> int:
    while True:
        answer = input('Choose an alternative(1/2) 1 = Continue. 2 = Exit: ')
        try:
            num_answer = int(answer)
        except:
         print('You have to write a number')
         continue
        if num_answer != 1 and num_answer != 2:
            print('You have to choose 1 or 2')
            continue
        else:
            return num_answer
        
def lenght() -> int:
    while True:
        pwd_lenght = input('How long do you want your password to be?(1-20): ')
        try:
            num_lenght = int(pwd_lenght)
        except:
            print('You have to write an integer.')
            continue
        if num_lenght > 20:
            print('Value cannot be more than 20')
            continue
        elif num_lenght > 0:
            return num_lenght
        else:
            print('Value cannot be negative, try again.')
            continue
        
def pwd_conditions():
    Yes = 'Yy'
    No = 'Nn'
    while True:
        condition = input('Do you want numbers in your password? (Y/N): ')
        if condition[0] in Yes:
            condition = True
            return condition
        elif condition[0] in No:
            condition = False
            return condition
        else:
            print('You have to type either Y or N!')
            continue