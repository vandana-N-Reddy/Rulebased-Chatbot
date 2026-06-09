print("===================================")
print("      Rule Based AI Chatbot")
print("===================================")
print("Type 'bye' to exit.\n")

while True:

    user_input = input("You: ").lower()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    # Asking name
    elif "your name" in user_input:
        print("Bot: My name is AI ChatBot.")

    # Asking age
    elif "how old are you" in user_input:
        print("Bot: I don't have an age like humans.")

    # Asking about AI
    elif "what is ai" in user_input:
        print("Bot: AI stands for Artificial Intelligence.")

    # Asking time
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    # Exit command
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break
    elif "course" in user_input:
        print("Bot: I can help with MCA and AI/ML topics.")

    elif "python" in user_input:
        print("Bot: Python is a popular programming language.")

    elif "weather" in user_input:
        print("Bot: Sorry, I don't have live weather data.")

    elif "thank you" in user_input:
        print("Bot: You're welcome!")

    # Default response
    else:
        print("Bot: Sorry, I don't understand that.")