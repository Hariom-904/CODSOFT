import re

rules = {
    "hello": "Hi there!",
    "hi":"hello, How can I help you?",
    "what's your name?": "My name is Bot!",
    "what can you do?": "I can chat with you!"
    
}

def match_rule(rules, statement):
    for pattern, response in rules.items():
        if re.search(pattern, statement):
            return response

while True:
    statement = input("You: ")
    response = match_rule(rules, statement)
    if response:
        print("Bot:", response)
    else:
        print("Bot: I'm sorry, I don't understand")
