import re

# Function to respond to user inputs
def chatbot_response(user_input, context):
    user_input = user_input.lower()
    
    # Greetings
    if re.search(r"\bhello\b|\bhi\b", user_input):
        return "Hello!. How can I assist you today?", context
    # Asking about the chatbot
    elif re.search(r"\bhow are you\b", user_input):
        return "I'm just a chatbot. I'm here to help you!", context
    # Farewells
    elif re.search(r"\bbye\b|\bgoodbye\b", user_input):
        return "Goodbye! Have a great day!", context
    # Asking about the time
    elif re.search(r"\bwhat time is it\b", user_input):
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        return f"The current time is {now}.", context
    # Asking for the chatbot's name
    elif re.search(r"\bwhat is your name\b", user_input):
        return "My name is YasaBot.", context
    # Asking about the weather (placeholder response)
    elif re.search(r"\bwhat is the weather like\b", user_input):
        return "I can't check the weather right now, but you can look outside!", context
    # Responding to thanks
    elif re.search(r"\bthank you\b|\bthanks\b", user_input):
        return "You're welcome! Anything else I can help with?", context
    # Responding to user's name
    elif re.search(r"\bmy name is\b", user_input):
        user_name = re.findall(r"\bmy name is (\w+)\b", user_input)
        if user_name:
            context['user_name'] = user_name[0]
            return f"Nice to meet you, {context['user_name']}!", context
        else:
            return "I didn't catch your name. Can you please repeat?", context
    # Asking for the user's name if known
    elif re.search(r"\bwhat is my name\b", user_input):
        if 'user_name' in context:
            return f"Your name is {context['user_name']}.", context
        else:
            return "I don't know your name yet. You can tell me by saying 'My name is [Your Name]'.", context
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?", context

# Main function to run the chatbot
def main():
    context = {}
    print("Welcome to YasaBot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response, context = chatbot_response(user_input, context)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
