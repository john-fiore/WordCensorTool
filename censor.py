import os
import re
import sys

word_list = []
censor_char = "*"

SPECIAL_CHAR_REGEX = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def setup_words():
    global word_list

    clear()
    word_list.clear()

    try:
        count = int(input("How many words do you want to censor? > "))
    except ValueError:
        print("Please enter a number.")
        input("Press ENTER to continue...")
        return setup_words()

    if count < 1:
        print("Cannot be under 1.")
        input("Press ENTER to continue...")
        return setup_words()

    for _ in range(count):
        word = input("> ").strip()
        if word:
            word_list.append(word)

    setup_char()

def setup_char():
    global censor_char

    clear()
    print("The special character that will censor each letter is '*' by default.")
    print("Enter a single special character or type 'skip'.")

    char = input("> ").strip()

    if char.lower() == "skip":
        check()
        return

    if len(char) == 1 and SPECIAL_CHAR_REGEX.search(char):
        censor_char = char
        check()
    else:
        print("You must enter ONE special character.")
        input("Press ENTER to continue...")
        setup_char()

def censor(text: str, words: list, char: str) -> str:
    for word in words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub(char * len(word), text)
    return text

def playground():
    clear()
    print("Type text to censor:\n")
    
    while True:
        text = input("> ")
        print(censor(text, word_list, censor_char))

def check():
    clear()

    words_display = ", ".join(word_list)

    print(f"Censored Words: {words_display}")
    print(f"Censor Character: {censor_char}")
    print()

    confirm = input("Does this look right? (y/n): ").lower()

    if confirm == "y":
        playground()
    elif confirm == "n":
        print("\nWhat looks wrong?")
        print("1 = Word List")
        print("2 = Censor Character")

        try:
            choice = int(input("> "))
        except ValueError:
            return check()

        if choice == 1:
            setup_words()
        elif choice == 2:
            setup_char()
        else:
            check()
    else:
        check()

def main():
    setup_words()

if __name__ == "__main__":
    main()
