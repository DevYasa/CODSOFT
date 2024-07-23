import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r"\bhello\b|\bhi\b", user_input):
        return "Hello! I am YasaBot.How can I assist you today?"
    elif re.search(r"\bhow are you\b", user_input):
        return "I'm just a chatbot, but I'm here to help you!"
    elif re.search(r"\bbye\b|\bgoodbye\b", user_input):
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

def main():
    print("Welcome to YasaBot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
