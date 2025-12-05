import random
pool= "abcdefghijklmnopqrstuvwxyz"
pool_numbers = "0123456789"

def generate_password(lenght, include_numbers) -> str:
    password = ""
    if include_numbers == True:
        pool_with_numbers = pool + pool_numbers
        for x in range(lenght):
            password = password + random.choice(pool_with_numbers)
        return password
    elif include_numbers == False:
        for x in range(lenght):
            password = password + random.choice(pool)
        return password
    
