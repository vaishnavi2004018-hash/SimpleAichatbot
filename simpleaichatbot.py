print("Hello! I am your Simple AI Chatbot")
print("Type 'bye' to exit")
while True:
    user = input("You: ").lower()
    if user == "bye":
        print("Bot: Bye! Nice talking to you!")
        break
    elif "hello" in user or "hi" in user:
        print("Bot: Hello! How are you?")
    elif "your name" in user:
        print("Bot: My name is SimpleAichatbot")
    elif "how are you" in user:
        print("Bot: I am good! What about you?")
    else:
        print("Bot: Sorry, I didn't understand.")
