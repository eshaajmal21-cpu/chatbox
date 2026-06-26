print("Welcome to the chatbox!\nType 'exit' to leave the chat.")
while True:
    user = input("You: ")
    if user == "Hello" or user == "Hi":
        print("Bot: Hello! How can I assist you today?")
    elif user == "How are you?":
        print("Bot: I'm doing great, thank you! ")
    elif user == "What is your name?":
        print("Bot: I am a simple chatbox created to assist you.")
    elif user == "What can you do?":
        print("Bot: I can answer simple questions and have a basic conversation with you.")
    elif user == "who created you?":
        print("Bot: I was created by a python programmer.")
    elif user == "Byee":
        print("Bot: Goodbye! Have a great day!")
        break
    elif user.lower() == "exit":
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot: I'm sorry, I don't understand that. Can you please rephrase?")
