def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I'm PyBot — your friendly Python chatbot."
    elif "how are you" in user_input:
        return "I'm just code, but I'm feeling great! How about you?"
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%I:%M %p')}"
    elif "date" in user_input:
        from datetime import date
        return f"Today's date is {date.today().strftime('%B %d, %Y')}"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Try asking something else!"


def main():
    print("=== Welcome to PyBot ===")
    print("Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("PyBot:", response)

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    main()
