"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Procházka
email: Michael.p.@gmail.com
"""
import hashlib
import string

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password, hashed_password):
    return hash_password(password) == hashed_password

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
    'bob': hash_password('123'),
    'ann': hash_password('pass123'),
    'mike': hash_password('password123'),
    'liz': hash_password('pass123')
}

username = input("username: ")
password = input("password: ")

if username in users and check_password(password, users[username]):
    print("-" * 40)
    print(f"✅ Welcome to the app, {username}.")
    print("We have 3 texts to be analyzed.")
    print("-" * 40)
    
    txtchoice = int(input("Enter a number btw. 1 and 3 to select: "))
    
    if 1 <= txtchoice <= 3:
        text = TEXTS[txtchoice - 1]
        
        wcount = 0
        title = 0
        lower = 0
        num = 0
        sum = 0
        words = text.split()
        wlengths = [0] * 11

        for word in words:
            word = word.strip(string.punctuation)
            wcount += 1
            wlength = len(word)

            if word.istitle():
                title += 1
            elif word.islower():
                lower += 1
            elif word.isdigit():
                num += 1
                sum += int(word)
            
            if 1 <= wlength <= 11:
                wlengths[wlength - 1] += 1

        print("-" * 40)
        print(f"There are {wcount} words in the selected text.")
        print(f"There are {title} titlecase words.")
        print(f"There are {lower} lowercase words.")
        print(f"There are {num} numeric strings.")
        print(f"The sum of all the numbers {sum}.")
        print("-" * 40)

        print("\nLEN|  OCCURENCES  |NR.")
        
        print("-" * 40)
        for i in range(11):
            if wlengths[i] > 0:
                print(f"{i+1}| {'*' * wlengths[i]} {wlengths[i]}")
                
    else:
        print("Wrong choice")
else:
    print("❌ unregistered user, terminating the program.")
    exit()



