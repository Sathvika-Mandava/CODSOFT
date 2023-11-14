import re

def simple_chatbot(user_input):
    # Convert the user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define rules and responses
    rules = {
        r'hello|hi|hey': 'Hello! How can I help you?',
        r'how are you|how are you doing': 'I am doing well, thank you!',
        r'what is your name|who are you': 'I am a simple rule-based chatbot.',
        r'bye|goodbye': 'Goodbye! Have a great day.',
        r'help': 'I can provide information based on predefined rules. Ask me anything!',
        r'.*': "I'm sorry, I don't understand. Please ask something else or type 'help' for assistance."
    }

    # Check user input against rules
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response

# Simple interaction loop
print("Simple Rule-Based Chatbot: Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
