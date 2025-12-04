#Error management and user input

def menu_input() -> int:
    while True:
        answer = input('Choose an alternative: ')
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