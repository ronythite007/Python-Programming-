import re

def get_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r'\b(hello|hi|hey)\b', user_input):
        return "Hello! How can I assist you today?"
    
    # Asking about chatbot's well-being
    elif re.search(r'\b(how are you|how are you doing)\b', user_input):
        return "I'm just a bunch of code, but I'm functioning as expected! How about you?"
    
    # Asking for the chatbot's name
    elif re.search(r'\b(your name|who are you)\b', user_input):
        return "I'm an advanced chatbot created to assist you. I don't have a personal name yet."
    
    # Asking for help
    elif re.search(r'\b(help|commands)\b', user_input):
        return ("Here are some things you can ask me:\n"
                "- 'hello' or 'hi' to greet me\n"
                "- 'how are you' to ask about my well-being\n"
                "- 'your name' to know who I am\n"
                "- 'weather' to get information about weather capabilities\n"
                "- 'joke' to hear a joke\n"
                "- 'bye' or 'exit' to end the conversation\n")
    
    # Asking about weather
    elif re.search(r'\b(weather)\b', user_input):
        return "I'm not equipped to provide real-time weather updates yet. But you can check your favorite weather website or app!"
    
    # Asking for a joke
    elif re.search(r'\b(joke|funny)\b', user_input):
        return "Why don't scientists trust atoms? Because they make up everything!"
    
    # Exit conversation
    elif re.search(r'\b(bye|exit|quit)\b', user_input):
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def chatbot():
    print("Hello! I'm your advanced chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        
        print(f"Chatbot: {response}")
        
        if response == "Goodbye! Have a great day!":
            break

# Run the chatbot
chatbot()
