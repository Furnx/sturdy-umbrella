
#QUESTION 1
get_date_of_birth(id_number:str)-> str: 
    """
    Extracts the date of birth from a South African ID number.

    The first 6 digits of the ID represent the date of birth in the format YYMMDD.
    This function converts it to the format DD/MM/YY.

    Args:
        id_number (str): A 13-digit South African ID number.

    Returns:
        str: The date of birth in the format DD/MM/YY.
    """
    date_of_birth = idnumber[4:]
    return date_of_birth


#QUESTION 2    
def get_gender(id_number:str)->str:
    """
    Determines the gender based on digits 7 to 10 of a South African ID number.

    The 7th to 10th digits form a number (SSSS) used to differentiate individuals.
    - If this number is less than 5000, the person is female.
    - If it is 5000 or greater, the person is male.

    Args:
        id_number (str): A 13-digit South African ID number.

    Returns:
        str: 'Male' or 'Female'
    """
    
    # if int() > :
    #     return 'Male'
    # else:
    #     return 'Female'
   return 0

    
#QUESTION 3
def get_citizenship(id_number:str)->str:
    """
    Determines the citizenship status based on the 11th digit of a South African ID number.

    The 11th digit indicates citizenship:
    - 0: South African citizen
    - 1: Non-South African (permanent resident)

    Returns:
        str: 'South African' or 'Non-South African'
    """
    
        return 'South African'
    else:
        return 'Non-South African'


#QUESTION 4

    """
    FizzBuzz is a program that prints the numbers from 1 to n. 
    - For multiples of 3, it prints "Fizz" instead of the number. 
    - For multiples of 5, it prints "Buzz". 
    - For numbers that are multiples of both 3 and 5, it prints "FizzBuzz".

    Args:
        n (int): The upper limit of the sequence (inclusive).

    Returns:
        None: This function prints output to the console and does not return anything.

    TODO: Define a function called `fizzbuzz` that takes an integer `n` as input 
    and prints the FizzBuzz sequence from 1 to n, one item per line.
    """


    

            

#QUESTION 5
def check_weirdness(n: int) -> str:
    """
    Determines the "weirdness" of an integer based on specific rules.

    Args:
        n (int): The integer to evaluate.

    Returns:
        str: A description of the number's weirdness.

    Rules:
    - If n is 0, return 'Neutral'
    - If n is positive and odd, return 'Weird'
    - If n is positive and even:
        - If n is in the range 2 to 5 (inclusive), return 'Not Weird'
        - If n is in the range 6 to 20 (inclusive), return 'Weird'
        - If n is greater than 20, return 'Not Weird'
    - If n is negative and even, return 'Very weird'
    - If n is negative and odd, return 'Extremely Weird'

    Examples:
    - check_weirdness(0) → 'Neutral'
    - check_weirdness(3) → 'Weird'
    - check_weirdness(4) → 'Not Weird'
    - check_weirdness(10) → 'Weird'
    - check_weirdness(22) → 'Not Weird'
    - check_weirdness(-2) → 'Very weird'
    - check_weirdness(-3) → 'Extremely Weird'
    """
    pass

