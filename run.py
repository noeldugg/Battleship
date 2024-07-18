from random import randint
    
    
def user_input(min_value: int = 1,max_value: int = 10) -> int:
    """
    Reads an integer that will provide a min and max value
     """
    while True:
        line = input(prompt)
        try: 
            value = int(line)
            if value < min_value:
                print(f"The minium value is {min_value}. Try again.")
            elif value > max_value:
                print(f"The maxium value is {max_value}. Try again.")
            else: 
                return value
        except ValueError:
            print("Not a number, try again")
             


