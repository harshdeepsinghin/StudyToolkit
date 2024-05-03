import requests
import json
import time
import os
import platform
import click
from colorama import Fore, Style
from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv
from notifypy import Notify
from simple_term_menu import TerminalMenu
import random


# Environments loading
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Variables Declaration

TOPICS = set()  #LATER
TERM_DEFINITION = dict()
TOPIC_DESCRIPTION = dict()
QUESTION_ANSWER = dict()
MISC_NOTES = list()

console = Console()
PLATFORM = platform.system()

# FUNCTIONS DEFINITION
## Menu function
def menu(submenu):
    '''Display menus by taking submenu as arguments.'''

    if ( submenu == 0 ):
        options = ["Main Menu", "Study", "Note", "Retain", "Utilities", "Exit"]
        terminal_menu = TerminalMenu(options, title="Main Menu")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index == 0):
            menu(0)
        elif (menu_entry_index == 1):
            menu(1)
        elif (menu_entry_index == 2):
            menu(2)
        elif (menu_entry_index == 3):
            menu(3)
        elif (menu_entry_index == 4):
            menu(4)
        elif (menu_entry_index == 5):
            Exit()

    elif ( submenu == 1 ):
        options = ["Previous Menu", "Ask AI", "Study notes", "Exit"]
        terminal_menu = TerminalMenu(options, title="Main -> Study Menu")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index == 0):
            menu(0)
        elif (menu_entry_index == 1):
            askai()
        elif (menu_entry_index == 2):
            menu(12)
        elif (menu_entry_index == 3):
            Exit()

    elif ( submenu == 12 ):
        options = ["Previous Menu", "Term-Definition", "Topic-Description", "Question-Answer", "Miscellaneous Notes", "All Notes", "Exit"]
        terminal_menu = TerminalMenu(options, title="Main -> Study -> Study Notes Menu")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index == 0):
            menu(1)
        elif (menu_entry_index == 1):
            study_notes(1)
        elif (menu_entry_index == 2):
            study_notes(2)
        elif (menu_entry_index == 3):
            study_notes(3)
        elif (menu_entry_index == 4):
            study_notes(4)
        elif (menu_entry_index == 5):
            study_notes(5)
        elif (menu_entry_index == 6):
            Exit()

    elif ( submenu == 2 ):
        options = ["Previous Menu", "Term-Definition", "Topic-Description", "Question-Answer", "Miscellaneous Notes", "Exit"]
        terminal_menu = TerminalMenu(options, title="Main -> Note Menu")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index == 0):
            menu(0)
        elif (menu_entry_index == 1):
            note(1)
        elif (menu_entry_index == 2):
            note(2)
        elif (menu_entry_index == 3):
            note(3)
        elif (menu_entry_index == 4):
            note(4)
        elif (menu_entry_index == 5):
            Exit()

    elif ( submenu == 3 ):
        options = ["Previous Menu", "Term-Definition", "Topic-Description", "Question-Answer", "Exit"]
        terminal_menu = TerminalMenu(options, title="Main -> Retain")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index == 0):
            menu(0)
        elif (menu_entry_index == 1):
            retain_notes(1)
        elif (menu_entry_index == 2):
            retain_notes(2)
        elif (menu_entry_index == 3):
            retain_notes(3)
        elif (menu_entry_index == 4):
            Exit()

    elif ( submenu == 4 ):
        options = ["Previous Menu", "Pomodoro Timer", "Exit"]
        terminal_menu = TerminalMenu(options, title="Main -> Utilities Menu")
        menu_entry_index = terminal_menu.show()
        if (menu_entry_index == 0):
            menu(0)
        elif (menu_entry_index == 1):
            options = ["Previous Menu", "Customized", "25m Work - 5m Break - 8 Cycles (POPULAR)", "50m Work - 10m Break - 4 Cycles", "Exit"]
            terminal_menu = TerminalMenu(options, cursor_index=2, title="Main -> Utilities -> Pomodoro Timer Menu")
            menu_entry_index = terminal_menu.show()
            if (menu_entry_index == 0):
                menu(4)
            elif (menu_entry_index == 1):
                WORK = int(input("Enter minutes for work: "))
                BREAK = int(input("Enter minutes for break: "))
                CYCLES = int(input("Enter number of cycles/rounds: "))
                pomodoro_timer(WORK, BREAK, CYCLES)
            elif (menu_entry_index == 2):
                pomodoro_timer(25,5,8)
            elif (menu_entry_index == 3):
                pomodoro_timer(50,10,4)
            elif (menu_entry_index == 4):
                Exit()

        elif (menu_entry_index == 2):
            Exit()

    return 0

## Note function
def note(TYPE):
    '''Takes notes of different types.'''

    if ( TYPE == 1 ):    # 2.1 - Term-Definition
        TERM = input("Term: ")
        DEFINITION = input("Definition: ")
        TERM_DEFINITION.update({TERM:DEFINITION})

    elif ( TYPE == 2 ):  # 2.2 - Topic-Description
        TOPIC = input("Topic: ")
        DESCRIPTION = input("Description: ")
        TOPIC_DESCRIPTION.update({TOPIC:DESCRIPTION})

    elif ( TYPE == 3 ):  # 2.3 - Question-Answer
        QUESTION = input("Question: ")
        ANSWER = input("Answer: ")
        QUESTION_ANSWER.update({QUESTION:ANSWER})

    elif ( TYPE == 4 ):  # 2.4 - Miscellaneous Notes
        if ( PLATFORM in ('Darwin','Linux','Unix')):
            print("Unix/Linux/Darwin")
            click.edit(filename='misc_notes.txt')

        elif ( PLATFORM == 'Windows' ):
            print("To be implemented.") #TODO

    print("\nNoted!\n")
    save_data()
    menu(1)
    return 0


## View Formatting Function
def print_with_color_and_format(text, color, bold=False, underline=False):
    style = ''
    if bold:
        style += '\033[1m'
    if underline:
        style += '\033[4m'
    style += color
    print(style + text + Style.RESET_ALL)

## Study Notes function
def study_notes(TYPE):
    '''Displays the existing notes of different types.'''

    if TYPE == 1:    # 2.1 - Term-Definition
        print_with_color_and_format("Term Definitions:", Fore.YELLOW, bold=True)
        for term, definition in TERM_DEFINITION.items():
            print_with_color_and_format(f"\t{term}", Fore.YELLOW, bold=True)
            print_with_color_and_format(f"\t►  {definition}\n", Fore.YELLOW)
    elif TYPE == 2:  # 2.2 - Topic-Description
        print_with_color_and_format("Topic Descriptions:", Fore.GREEN, bold=True)
        for topic, description in TOPIC_DESCRIPTION.items():
            print_with_color_and_format(f"\t{topic}", Fore.GREEN, bold=True)
            print_with_color_and_format(f"\t►  {description}\n", Fore.GREEN)
    elif TYPE == 3:  # 2.3 - Question-Answer
        print_with_color_and_format("Question-Answers:", Fore.CYAN, bold=True)
        for question, answer in QUESTION_ANSWER.items():
            print_with_color_and_format(f"\t{question}", Fore.CYAN, bold=True)
            print_with_color_and_format(f"\t►  {answer}\n", Fore.CYAN)
    elif TYPE == 4:  # 2.4 - Miscellaneous Notes
        print_with_color_and_format("Miscellaneous Notes:", Fore.MAGENTA, bold=True)
        with open("misc_notes.txt", 'r') as MN:
            for line in MN:
                print_with_color_and_format(f"\t• {line.strip()}", Fore.MAGENTA)
    elif TYPE == 5:  # 2.5 - All Notes
        print_with_color_and_format("Term Definitions:", Fore.YELLOW, bold=True)
        for term, definition in TERM_DEFINITION.items():
            print_with_color_and_format(f"\t{term}", Fore.YELLOW, bold=True)
            print_with_color_and_format(f"\t►  {definition}\n", Fore.YELLOW)

        print_with_color_and_format("Topic Descriptions:", Fore.GREEN, bold=True)
        for topic, description in TOPIC_DESCRIPTION.items():
            print_with_color_and_format(f"\t{topic}", Fore.GREEN, bold=True)
            print_with_color_and_format(f"\t►  {description}\n", Fore.GREEN)

        print_with_color_and_format("Question-Answers:", Fore.CYAN, bold=True)
        for question, answer in QUESTION_ANSWER.items():
            print_with_color_and_format(f"\t{question}", Fore.CYAN, bold=True)
            print_with_color_and_format(f"\t►  {answer}\n", Fore.CYAN)

        print_with_color_and_format("Miscellaneous Notes:", Fore.MAGENTA, bold=True)
        with open("misc_notes.txt", 'r') as MN:
            for line in MN:
                print_with_color_and_format(f"\t• {line.strip()}", Fore.MAGENTA)
    menu(12)
    return 0


## Ask AI function
def askai():
    '''Asks Google\'s Gemini-Pro AI to study more effeciently.
    *Requires preconfiguration for API_KEY into .env file  '''

    PROMPT = "foobar"   # placeholder text
    while True:
        print()
        print("Enter \"quit\" or \"exit\" to quit asking AI.")
        PROMPT = input("Ask: ")
        if ( PROMPT in ("quit","exit") ):
            print("\nBye... Come back again...\n")
            break

        data = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": PROMPT
                        }
                    ]
                }
            ]
        }

        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            markdown_text = response.json()['candidates'][0]['content']['parts'][0]['text']
            markdown = Markdown(markdown_text)
            console.print(markdown)
        else:
            print("Error:", response.status_code)

    menu(1)
    return 0


def retain_notes(TYPE):
    '''Retain notes of different types.'''
    while True:
        if TYPE == 1:    # 2.1 - Term-Definition
            # Randomly select a term from TERM_DEFINITION
            definitions = list(TERM_DEFINITION.values())
            ask_term, right_definition = random.choice(list(TERM_DEFINITION.items()))
            print_with_color_and_format(f"Match the definition for the term '{ask_term}':", Fore.YELLOW, bold=True)
            # Generate multiple-choice options with the correct answer included
            options = definitions
            random.shuffle(options)

            # Display MCQ options using TerminalMenu
            terminal_menu = TerminalMenu(options, title="Options:")
            menu_entry_index = terminal_menu.show()

            # Check if the selected option matches the correct answer
            if options[menu_entry_index] == right_definition:
                print("Hooray! You got it right.")
                break
            else:
                print("Sorry, that's incorrect. Please try again.")

        elif TYPE == 2:  # 2.2 - Topic-Description
            # Randomly select a topic from TOPIC_DESCRIPTION
            descriptions = list(TOPIC_DESCRIPTION.values())
            ask_topic, right_description = random.choice(list(TOPIC_DESCRIPTION.items()))
            print_with_color_and_format(f"Match the description for the topic '{ask_topic}':", Fore.GREEN, bold=True)
            # Generate multiple-choice options with the correct answer included
            options = descriptions
            random.shuffle(options)

            # Display MCQ options using TerminalMenu
            terminal_menu = TerminalMenu(options, title="Options:")
            menu_entry_index = terminal_menu.show()

            # Check if the selected option matches the correct answer
            if options[menu_entry_index] == right_description:
                print("Hooray! You got it right.")
                break
            else:
                print("Sorry, that's incorrect. Please try again.")

        elif TYPE == 3:  # 2.3 - Question-Answer
            # Randomly select a question from QUESTION_ANSWER
            answers = list(QUESTION_ANSWER.values())
            ask_question, right_answer = random.choice(list(QUESTION_ANSWER.items()))
            print_with_color_and_format(f"Match the answer for the question '{ask_question}':", Fore.CYAN, bold=True)
            # Generate multiple-choice options with the correct answer included
            options = answers
            random.shuffle(options)

            # Display MCQ options using TerminalMenu
            terminal_menu = TerminalMenu(options, title="Options:")
            menu_entry_index = terminal_menu.show()

            # Check if the selected option matches the correct answer
            if options[menu_entry_index] == right_answer:
                print("Hooray! You got it right.")
                break
            else:
                print("Sorry, that's incorrect. Please try again.")

    menu(3)  # Go back to the retain menu



## Pomodoro Timer Function
def pomodoro_timer(WORK=25, BREAK=5, CYCLES=8):
    notification = Notify()
    notification.title = "Pomodoro Timer"
    print("\n\n⏰  POMODORO STARTED  ⏰")

    for i in range(CYCLES):
        print(f"\nROUND {i+1}...")
        notification.message = f"Work Time ({WORK}m) Started!"
        notification.audio = "work_sound.wav"
        notification.send()

        print(f"\n⏰  WORK TIME  ⏰  ROUND {i+1}  ⏰")
        print("(Pres `Ctrl + C` to stop)\n")
        SECONDS=WORK*60
        while SECONDS:
            MIN, SEC = divmod(SECONDS,60)
            timer = '\t{:02d}:{:02d}'.format(MIN,SEC)
            print(timer, end='\r')
            time.sleep(1)
            SECONDS-=1


        print(f"\n\n⌛  BREAK TIME  ⌛  ROUND {i+1}  ⌛")
        print("(Pres `Ctrl + C` to stop)\n")

        notification.audio = "break_sound.wav"

        if ( (i+1) % 4 == 0 ):      # For bigger break after 4 rounds
            SECONDS = BREAK*3*60
            notification.message = f"Break ({BREAK*3}m) Time!"
            notification.send()
        else:
            SECONDS = BREAK*60
            notification.message = f"Break ({BREAK}m) Time!"
            notification.send()

        while SECONDS:
            MIN, SEC = divmod(SECONDS,60)
            timer = '\t{:02d}:{:02d}'.format(MIN,SEC)
            print(timer, end='\r')
            time.sleep(1)
            SECONDS-=1

    print("\n⏰  POMODORO ENDED  ⏰")

    menu(4)
    return 0

## Load Data Function
def load_data():
    '''Loads data from current working directory to the running program.'''

    global TERM_DEFINITION
    global TOPIC_DESCRIPTION
    global QUESTION_ANSWER

    try:
        with open("term_definition.json", 'r') as TED:
            TERM_DEFINITION = json.load(TED)
    except FileNotFoundError:
        pass

    try:
        with open("topic_description.json", 'r') as TOD:
            TOPIC_DESCRIPTION = json.load(TOD)
    except FileNotFoundError:
        pass

    try:
        with open("question_answer.json", 'r') as QA:
            QUESTION_ANSWER = json.load(QA)
    except FileNotFoundError:
        pass
    return 0

## Save Data Function
def save_data():
    '''Saves data to local files in the current working directory from the running program'''

    with open("term_definition.json", 'w') as TED, open("topic_description.json", 'w') as TOD, open("question_answer.json", 'w') as QA:
        json.dump(TERM_DEFINITION, TED, indent=4)
        json.dump(TOPIC_DESCRIPTION, TOD, indent=4)
        json.dump(QUESTION_ANSWER, QA, indent=4)
    return 0

## Quit/Exit function
def Exit():
    save_data()
    print("Bye! Come back soon...")
    exit()

## Main function
def main():
    load_data()
    while True:
        menu(0)

# Main function Calling
main()

# --- LATER WORK ---

def search_term():  #LATER
    while True:
        print()
        TERM = input("What is?: ")
        FIELD = input("In the field/domain of: ")

        data = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": f"Give a breif meaning in one line of the term {TERM} in the field or domain of {FIELD}"
                        }
                    ]
                }
            ]
        }
        if ( TERM == "exit" ):
            print("\nBye... See you...\n")
            break

        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            markdown_text = response.json()['candidates'][0]['content']['parts'][0]['text']

            markdown = Markdown(markdown_text)
            console.print(markdown)
        else:
            print("Error:", response.status_code)

    return 0
