import requests
import json
import time
import os
import platform
import click
from colorama import Fore, Style
from dotenv import load_dotenv

# Environments loading
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
api_hash = os.getenv('API_HASH')

# Variables Declaration

TOPICS = set()
TERM_DEFINITION = dict()
TOPIC_DESCRIPTION = dict()
QUESTION_ANSWER = dict()
MISC_NOTES = list()

PLATFORM = platform.system()

# FUNCTIONS DEFINITION
## Menu functoin
def menu(submenu):
    if ( submenu == 0 ):
        print("""
    0 - This menu
    1 - Study
    2 - Note
    3 - Retain
    4 - Utilities
    5 - Exit
        """)
    elif ( submenu == 1 ):
        print("""
    0 - This menu
    1 - Ask AI
    2 - Study Notes
        """)
    elif ( submenu == 12 ):
        print("""
    0 - This menu
    1 - Term-Definition
    2 - Topic-Description
    3 - Question-Answer
    4 - Miscellaneous Notes
    5 - All Notes
        """)
    elif ( submenu == 2 ):
        print("""
    0 - This menu
    1 - Term-Definition
    2 - Topic-Description
    3 - Question-Answer
    4 - Miscellaneous Notes
        """)
    return 0

## Note function
def note(TYPE):
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

    save_data()
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
    return 0



def search_term():
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

        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={GOOGLE_API_KEY}"

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            content = response.json()['candidates'][0]['content']['parts'][0]['text']
            print(content)
        else:
            print("Error:", response.status_code)

    return 0


## Ask AI function
def askai():
    while True:
        print()
        PROMPT = input("Ask: ")

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
        if ( PROMPT == "exit" ):
            print("\nBye... See you...\n")
            break

        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={GOOGLE_API_KEY}"

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            content = response.json()['candidates'][0]['content']['parts'][0]['text']
            print(content)
        else:
            print("Error:", response.status_code)

        return 0

## Load Data Function
def load_data():
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
    with open("term_definition.json", 'w') as TED, open("topic_description.json", 'w') as TOD, open("question_answer.json", 'w') as QA:
        json.dump(TERM_DEFINITION, TED, indent=4)
        json.dump(TOPIC_DESCRIPTION, TOD, indent=4)
        json.dump(QUESTION_ANSWER, QA, indent=4)
    return 0

## Main function
def main():
    load_data()
    menu(0)
    while True:

        try:
            Q = -1
            Q=int(input("\nSelect an option: "))
            if ( Q == 0 ) :     # 0 - Menu
                menu(0)
            elif ( Q == 1) :    # 1 - Study
                menu(1)
                Q = -1
                Q=int(input("\nSelect an option: "))
                if ( Q == 1 ):      # 1.1 - Ask AI
                    Q = -1
                    askai()

                elif ( Q == 2 ):    # 1.2 - Study Notes
                    Q = -1
                    menu(12)
                    Q=int(input("\nSelect an option: "))
                    if ( Q == 1 ):    # 1.2.1 - Term-Definition
                        Q = -1
                        study_notes(1)

                    elif ( Q == 2 ):  # 1.2.2 - Topic-Description
                        Q = -1
                        study_notes(2)

                    elif ( Q == 3 ):  # 1.2.3 - Question-Answer
                        Q = -1
                        study_notes(3)

                    elif ( Q == 4 ):  # 1.2.4 - Miscellaneous Notes
                        Q = -1
                        study_notes(4)

                    elif ( Q == 5 ):  # 1.2.5 - All Notes
                        Q = -1
                        study_notes(1)
                        study_notes(2)
                        study_notes(3)
                        study_notes(4)

            elif ( Q == 2 ):    # 2 - Note
                Q = -1
                menu(2)
                Q=int(input("\nSelect an option: "))
                if ( Q == 0 ):
                    Q = -1
                    menu(2)

                elif ( Q == 1 ):    # 2.1 - Term-Definition
                    Q = -1
                    note(1)

                elif ( Q == 2 ):    # 2.2 - Topic-Description
                    Q = -1
                    note(2)

                elif ( Q == 3 ):    # 2.3 - Question-Answer
                    Q = -1
                    note(3)

                elif ( Q == 4 ):    # 2.4 - Miscellaneous Notes
                    Q = -1
                    note(4)

            elif ( Q == 5 ):    # 5 - Exit
                Q = -1
                save_data()
                return 0

        except: # to except errors
            print(EOFError())
            print('\n' + 'Oops! Something went wrong, please try again...' + '\n')

# Main function Calling
main()
