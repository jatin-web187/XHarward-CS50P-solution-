def convert(text):
    """
    Converts emoticons to emojis in the input string.
    """
    # Replace :) with 🙂 and :( with 🙁
    result = text.replace(":)", "🙂").replace(":(", "🙁")
    return result

def main():
    """
    Prompts user for input, calls convert, and prints the result.
    """
    # Get user input
    user_input = input("Enter text: ")

    # Convert emoticons to emojis
    formatted_text = convert(user_input)

    # Print the result
    print(formatted_text)

main()

