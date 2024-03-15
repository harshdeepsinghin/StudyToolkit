import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
api_hash = os.getenv('API_HASH')

TOPICS = set()
TERM_DEFINITION = dict()
TOPIC_DESCRIPTION = dict()
QUESTION_ANSWER = dict()
MISC_NOTES = list()

# FUNCTIONS DEFINITION

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

def note(TYPE):
    if ( TYPE == 1 ):
        TERM = input("Term: ")
        DEFINITION = input("Definition: ")
        TERM_DEFINITION.update({TERM:DEFINITION})
    elif ( TYPE == 2 ):
        TOPIC = input("Topic: ")
        DESCRIPTION = input("Description: ")
        TOPIC_DESCRIPTION.update({TOPIC:DESCRIPTION})
    elif ( TYPE == 3 ):
        QUESTION = input("Question: ")
        ANSWER = input("Answer: ")
        QUESTION_ANSWER.update({QUESTION:ANSWER})
    elif ( TYPE == 4 ):
        NOTE = input("Note: ")
        MISC_NOTES.append(NOTE)

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


def main():
    menu(0)
    while True:

        try:
            Q = -1
            Q=int(input("\nSelect an option: "))
            if ( Q == 0 ) :
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
                    if ( Q == 1 ):
                        Q = -1
                        print(TERM_DEFINITION)

                    elif ( Q == 2 ):
                        Q = -1
                        print(TOPIC_DESCRIPTION)

                    elif ( Q == 3 ):
                        Q = -1
                        print(QUESTION_ANSWER)

                    elif ( Q == 4 ):
                        Q = -1
                        print(MISC_NOTES)

                    elif ( Q == 5 ):
                        Q = -1
                        print(TERM_DEFINITION, TOPIC_DESCRIPTION, QUESTION_ANSWER, MISC_NOTES)

            if ( Q == 2 ):      # 2 - Note
                Q = -1
                menu(2)
                Q=int(input("\nSelect an option: "))
                if ( Q == 0 ):
                    Q = -1
                    menu(2)

                elif ( Q == 1 ):
                    Q = -1
                    note(1)

                elif ( Q == 2 ):
                    Q = -1
                    note(2)

                elif ( Q == 3 ):
                    Q = -1
                    note(3)

                elif ( Q == 4 ):
                    Q = -1
                    note(4)

            elif ( Q == 5 ):
                Q = -1
                return 0

        except: # to except errors
            print(EOFError())
            print('\n' + 'Oops! Something went wrong, please try again...' + '\n')



main()
