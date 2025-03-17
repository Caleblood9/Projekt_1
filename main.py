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

    try:
        txtchoice = int(input("Enter a number btw. 1 and 3 to select: "))
        if txtchoice not in range(1, 4):
            raise ValueError
    except ValueError:
        print("Wrong choice")
        exit(1)

    text = TEXTS[txtchoice - 1]
    words = [word.strip(string.punctuation) for word in text.split()]

    word_count = len(words)
    word_title = sum(1 for word in words if word.istitle())
    word_lower = sum(1 for word in words if word.islower())
    word_num = sum(1 for word in words if word.isdigit())
    summary = sum(int(word) for word in words if word.isdigit())

    word_lens = [0] * (max(len(word) for word in words) + 1)
    for word in words:
        word_lens[len(word)] += 1

    print("-" * 40)
    print(f"There are {word_count} words in the selected text.")
    print(f"There are {word_title} titlecase words.")
    print(f"There are {word_lower} lowercase words.")
    print(f"There are {word_num} numeric strings.")
    print(f"The sum of all the numbers {summary}.")
    print("-" * 40)

    print("\nLEN|  OCCURRENCES  |NR.")
    print("-" * 40)
    for i, count in enumerate(word_lens, 1):
        print(f"{str(i).rjust(2)} | {'*' * count}".ljust(25) + f"| {count}")

else:
    print("❌ Unregistered user, terminating the program.")