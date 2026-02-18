import random

Quotees = ["Abdullah Ibrahim","Miriam Makeba", "Nelson Mandela", "Eleanor Roosevelt",
 "Anne Frank", "Alexander Graham Bell","Thomas Edison","Estee Lauder","Maya Angelou", "Walt Disney"]



def ask_file_name(user_input):
    """
    TODO: Step 1 - Handle file name selection based on user input.
    
    This function should:
    - Return the user_input if it's provided and not empty
    - Return 'quotes.txt' as the default for blank or empty input
    
    Args:
        user_input (str or None): The filename provided by the user
        
    Returns:
        str: The filename to use - either user_input or 'quotes.txt' as default
        
    Examples:
        ask_file_name('myfile.txt') should return 'myfile.txt'
        ask_file_name('') should return 'quotes.txt'
        ask_file_name(None) should return 'quotes.txt'
    """
    

    return ''



def read_file(file_name):
    """
    TODO: Step 2 - Complete the file reading functionality.
    
    This function should:
    - Open and read the entire file content
    - Print "File successfully opened..." when successful
    - Return the file content as a string
    - Handle FileNotFoundError properly in the except block
    - Print error information and return empty string on error
    
    Args:
        file_name (str): Name of the file to read
        
    Returns:
        str: File content if successful, empty string if file not found
        
    Expected behavior:
        - On success: prints success message and returns file content
        - On FileNotFoundError: prints error message and returns ""
    """
    
    try:
        pass

    except:
        pass

    return ""



def select_random_quotee(Quotees):
    
    """
    TODO: Step 3 - Implement random quotee selection.
    
    This function should:
    - Use random.choice() to select a random item from the list
    - Return the selected quotee
    
    Args:
        quotees_list (list): List of quotee names to choose from
        
    Returns:
        str: A randomly selected quotee name from the list
        
    Example:
        select_random_quotee(['Person A', 'Person B']) returns either 'Person A' or 'Person B'
        
    Note: random.choice() requires a non-empty list
    """
    
    
    return ""


def find_quote(random_quotee,quotes):
    
    """
    TODO: Step 4 - Implement quote searching functionality.
    
    This function should:
    - Search through the quotes list to find a quote for the given quotee
    - Return the complete quote string when found
    - Return exactly "Quote/quotee does not exist." when not found
    
    Quote format: Each quote in the list follows the pattern "Quotee Name ~ Quote text"
    
    Args:
        quotee_name (str): Name of the person to find a quote for
        quotes_list (list): List of quote strings in format "Name ~ Quote text"
        
    Returns:
        str: The complete quote string if found, or "Quote/quotee does not exist." if not found
        
    Examples:
        find_quote("Thomas Edison", ["Thomas Edison ~ \"I failed my way to success.\""]) 
        should return "Thomas Edison ~ \"I failed my way to success.\""
        
        find_quote("Unknown Person", ["Thomas Edison ~ \"Quote\""]) 
        should return "Quote/quotee does not exist."
    """

    return ""



def final_output(quote,quotee):
    
    """
    TODO: Step 5 - Format and display the final quote output.
    
    This function should:
    - Split the quote string on "~" to separate the quotee name and quote text
    - Print "Quote found in file:" as the first line
    - Print the quotee name and quote text in a readable format
    - Handle whitespace properly (strip extra spaces from the quote text)
    
    Args:
        quote_string (str): Complete quote in format "Quotee Name ~ Quote text"
        quotee_name (str): Name of the quotee
        
    Expected output format:
        Quote found in file:
        Quotee Name: Quote text here
        
    Example:
        final_output("Einstein ~ E=mc²", "Einstein") should print:
        Quote found in file:
        Einstein: E=mc²
    """
    
    pass
 
if __name__ == "__main__":
    """
     You can leave this code as is, and only implemented above where the code comments prompt you.
     """
    user_input = input("Desired file? [leave empty to use quotes.txt] :")
    quotes_file = ask_file_name(user_input)
    print(repr(str(quotes_file)) + ': is your chosen file.\n')
    quotes = read_file(quotes_file).split("\n\n")
    random_quotee = select_random_quotee(Quotees)
    if random_quotee == "":
        print('Empty list.\n')
    else:
        print(str(random_quotee) + ' has randomly been chosen.\n')
    true_quote = find_quote(random_quotee,quotes)
    if true_quote == "":
        print(str(random_quotee) + ' is not present in the file\n')
        quit()
    else:
        print(str(random_quotee) + ' is present in the file\n')
        final_output(true_quote,random_quotee)
