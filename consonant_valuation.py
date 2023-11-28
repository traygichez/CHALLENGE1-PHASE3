# This function calculates the "consonant value" of a given string.

def get_consonant_value(string):
    # Define the alphabet for reference.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Define the vowels to identify them in the string.
    vowels = 'aeiou'

    # Initialize an empty list to store consonant values.
    values = []

    # Initialize a variable to track the current consonant value.
    s_value = 0
    
    # Iterate through each character in the string.
    for i in range(len(string)):
        # Get the current character.
        character = string[i]

        # Check if the character is a vowel.
        if str.__contains__(vowels, character):
            # If it's a vowel and not the first character, add the current consonant value to the list.
            if i != 0 and s_value != 0:
                values.append(s_value)
                # Reset the consonant value for the next sequence.
                s_value = 0
        else:
            # If the character is a consonant, add its position in the alphabet to the current consonant value.
            s_value += alphabet.find(character) + 1
            
        # Check if we are at the last character of the string and there is a pending consonant value.
        if i == (len(string) - 1) and s_value != 0:
            # Add the last consonant value to the list.
            values.append(s_value)
        
    # Sort the list of consonant values in reverse order.
    values.sort(reverse=True)
    
    # Return the highest consonant value, or 0 if there are no consonants.
    return values[0] if len(values) > 0 else 0
