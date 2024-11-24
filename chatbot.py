def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. How can I help you?")
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hi there! How can I assist you today?")
    elif "how are you" in user_input:
        print("Chatbot: I'm just a program, but I'm functioning perfectly! How about you?")
    elif "what is your name" in user_input:
        print("Chatbot: I am your friendly chatbot. You can call me Bot.")
    elif "bye" in user_input or "goodbye" in user_input:
        print("Chatbot: Goodbye! Have a great day!")
    else:
        print("Chatbot: I'm sorry, I don't understand that. Can you rephrase it?")

# Call the chatbot function
chatbot()
