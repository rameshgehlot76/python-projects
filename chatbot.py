# Enhanced Python Chatbot 
import random 
import datetime 

responses = {
    "hi": ["Hello!", "Hey there!", "Hii! How are you today?", "Hey 👋"],
        "hello": ["Hii!", "Hello!", "Hey!", "Hi there!"],
        "how are you": ["I'm doing great! Thanks for asking.", "All good here 😄 How about you?", "Feeling awesome today!"],
        "what is your name": ["I'm PyBot!", "People call me PyBot — your Python buddy 🤖", "I'm your friendly chatbot."],
        "who created you": ["I was created by a Python developer just like you!", "A curious coder built me using Python."],
        "bye": ["Goodbye!", "See you soon!", "Take care!", "Bye 👋"],
        "thanks": ["You're welcome!", "No problem!", "Glad to help 😊"],
        "thank you": ["You're welcome!", "Happy to help!", "Anytime!"],
        "time": ["The current time is " + datetime.datetime.now().strftime("%H:%M:%S")],
        "date": ["Today's date is " + datetime.datetime.now().strftime("%d %B %Y")],
        "joke": [
            "Why do programmers hate nature? Too many bugs 😂",
            "I told my computer I needed a break... and it froze 🥶",
            "Why do Java developers wear glasses? Because they don’t C#! 😆"
        ],
        "your age": ["I’m timeless!", "Age is just a number... and I’m infinite 😎"],
        "what can you do": [
            "I can chat, tell jokes, show the time/date, and keep you company!",
            "I can make your day a little better by chatting 😁",
            "I’m learning new skills every day — soon I’ll help you code too!"
        ],
        "where are you from": [
            "I live inside your computer 🖥️",
            "From the cloud ☁️ — not the rainy one though 😄",
            "I was born in Python land 🐍"
        ],
        "love": ["Aww, that’s sweet ❤️", "Love makes the world go round 💞", "That’s deep 😌"],
        "weather": ["I can’t feel it, but I hope it's nice where you are ☀️", "I don’t need an umbrella, but you might 😄"],
        "default": [
            "I'm not sure I understand 🤔",
            "Can you rephrase that?",
            "Hmmm... that’s interesting! Tell me more.",
            "Sorry, I didn’t get that."
        ]
} 

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key]) 
    return random.choice(responses["default"]) 

print("       🤖 PyBot: Hi! I'm your friendly chatbot. Type 'bye' to exit. \n") 
print(" ") 
print("     Say:  hi|hello|how are you|what is your name|who created you|thanks|thank you|") 
print("        time|date|joke|your age|what can you do|where are you from|love|weather|default|")    
while True: 
    user = input("You: ") 
    if "bye" in user.lower():
        print("PyBot:", random.choice(responses["bye"])) 
        break 
    print("PyBot:", get_response(user))  

