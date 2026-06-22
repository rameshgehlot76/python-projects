
# Number Guessing Game  
import random

# Function to generate a random number between 1 and 100  
def get_random_number():
    return random.randint(1, 100)   # number between 1 and 100

# Function to check the guess
def check_guess(user_guess, secret_number):
    if user_guess < secret_number:  
        return "Too low! Try again."
    elif user_guess > secret_number: 
        return "Too high! Try again."
    else:
        return "Correct! You guessed it!" 


# Main program 
print("----- Number Guessing Game -----") 
secret_number = get_random_number()
attempts = 0 

while True:
    guess = int(input("Enter your guess (1-100): ")) 
    attempts += 1
    result = check_guess(guess, secret_number)
    print(result) 

    if guess == secret_number:
        print(f"You guessed the number in {attempts} attempts 🎉") 
        break  


 
# To-Do List (Basic Console App) 

tasks = []  # list to store tasks 

def add_task(task):
    tasks.append(task)
    return f"✅ Task added: {task}" 

def view_task():
    if not tasks:
        return "📂 No tasks in the list!"
    result = "\n--- Your To-Do List ---\n"
    for i, task in enumerate(tasks, start=1):
        result += f"{i}. {task}\n"
    return result 

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number -1)
        return f"❌ Task removed: {removed}"
    else:
        return "⚠️ Invalid task number!"


# Main Program 
print("----- Welcome to To-Do List App -----") 

while True:
    print("\nChoose an option: ")
    print("1. Add Task") 
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit") 

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter task: ") 
        print(add_task(task)) 

    elif choice == "2":
        print(view_task()) 

    elif choice == "3":
        try:
            num = int(input("Enter task number to remove: ")) 
            print(remove_task(num)) 
        except ValueError:
            print("⚠️ Please enter a valid number!") 

    elif choice == "4":
        print("👋 Exiting To-Do List App. Goodbye!")
        break 


    else: 
        print("⚠️ Invalid choice! Please try again.") 


 
# Calendar in Python 
import calendar
yy = 2012  # year 
mm = 11    # month 
# display the calendar 
print(calendar.month(yy, mm))



# Internet speed checker 
import speedtest 
st = speedtest.Speedtest()
dl = st.download()
up = st.upload() 
print("Download Speed:", dl/1024/1024, "kbs")
print("Upload Speed:", up/1024/1024, "kbs")



# Phone Number Tracker 

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def track_number(phone_number):
    try:
        # Parse number with country code (e.g. +91 for India, +1 for USA)
        parsed_number = phonenumbers.parse(phone_number)

        # Check validity
        valid = phonenumbers.is_valid_number(parsed_number)
        possible = phonenumbers.is_possible_number(parsed_number)

        # Get details
        country = geocoder.description_for_number(parsed_number, "en")
        sim_carrier = carrier.name_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)

        # Print results
        print(f"\n📞 Phone Number: {phone_number}")
        print(f"✅ Valid: {valid}")
        print(f"❓ Possible: {possible}")
        print(f"🌍 Country/Region: {country}")
        print(f"📡 Carrier: {sim_carrier if sim_carrier else 'Unknown'}")
        print(f"⏰ Timezones: {', '.join(time_zones)}")

    except Exception as e:
        print("Error:", e)


# ------------------------- 
# Example Usage
# -------------------------
if __name__ == "__main__":
    number = input("Enter phone number with country code (e.g. +919876543210): ")
    track_number(number)



# Whatsapp Message to Anyone 
import pywhatkit as kit
kit.sendwhatmsg("+918007844912", "Hello RAMESH this is an Automated message sent using Python!", 16,45) 
# Replace with actual number and time
# Note: The time is in 24-hour format (HH, MM). Make sure to set it a few minutes ahead of the current time.


# Python program to generate password
import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbols = "!@#$%^&*()_+"

all = lower + upper + num + symbols
length = 16 
password = "".join(random.sample(all,length))
print(password) 



# QR Code Generator in Python
import qrcode
data = "https://www.youtube.com/@RameshCummins"
qr = qrcode.make(data)
qr.save("Ramesh.png")  
print("QR Code Generated!")  



# Barcode Generator in Python
import barcode
from barcode.writer import ImageWriter
code_data = "918007844912"  # Example data
code_type = "ean13"  # Barcode type (e.g., ean13, upc, code39, etc.)
barcode_class = barcode.get_barcode_class(code_type)
my_barcode = barcode_class(code_data, writer=ImageWriter())
my_barcode.save("MyBarcode")
print("Barcode Generated!")

  

# Secret Code Language🕵️‍♂️🕵️‍♂️ 
# Secret Code Language Translator 

def encode(message):
    words = message.split() 
    new_words = [] 

    for word in words:
        if len(word) >= 3: 
            # Rule: move first letter to the end, then add a random prefix and suffix
            new_word = word[1:] + word[0] + "rog" 
        else:
            # For short words, just reverse them
            new_word = word[::-1] 
        new_words.append(new_word) 

    return " ".join(new_words) 


def decode(secret):
    words = secret.split() 
    new_words = [] 

    for word in words:
        if len(word) >= 3: 
            # Remove the suffix 'rog' and move the last letter to the front 
            new_word = word[-4] + word[:-4] 
        else:
            # For short words, just reverse them
            new_word = word[::-1] 
        new_words.append(new_word) 

    return " ".join(new_words) 


# Main Program 

print("                   Welcome to the SECRET CODE Translator! 🕵️‍♂️ ") 
print("   ")
print("   ") 
choice = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower() 
message = input("Enter your message: ") 

if choice == 'encode':
    print("Encoded Message: ", encode(message)) 
elif choice == 'decode':
    print("Decoded Message: ", decode(message)) 
else:
    print("Invalid choice. Please type 'encode' or 'decode'.") 



# A Simple Tikinter Window 
# Python program to create a simple window using Tkinter

import tkinter as tk 

# Create the main window 
root = tk.Tk() 
root.title("My First GUI App") 
root.geometry("300x200") 

# Add a label 
label = tk.Label(root, text="Hello, Ramesh! 👋", font=("Arial", 14)) 
label.pack(pady=20) 

# Add a button 
def greet():
    label.config(text="You clicked the buttton! 🎉") 

button = tk.Button(root, text="Click Me", command=greet) 
button.pack(pady =10)   

# Keep the window open running 
root.mainloop() 



# Password Strength Checker 
pwd = input("Enter the password: ") 

if len(pwd) < 8:
    print("Weak: Too short")  
elif not any(c.isdigit() for c in pwd):
    print("Weak: Add a number")
elif not any(c.isupper() for c in  pwd): 
    print("Weak: Add an uppercase letter") 
else: 
    print("Strong Password ✅")  
    
    

# Word and Character Counter 
# Program to count words and characters in a text file 

file_name = input("Enter file name: ") 

try:
    with open(file_name, "r") as file: 
        content = file.read() 

        # Count characters (excluding spaces use: len(content.replace(" ", "")))
        char_count = len(content) 

        # Count words 
        word_count = len(content.split()) 

        print("Total Words: ", word_count) 
        print("Total Characters: ", char_count) 

except FileNotFoundError:
    print("⚠ File not Found! Make sure the file exists in the same folder.") 

