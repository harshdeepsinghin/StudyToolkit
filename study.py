import requests
import json
import time
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
api_hash = os.getenv('API_HASH')


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
2 - What is?
        """)

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

        Q=int(input("\nSelect an option: "))

        try:

            if ( Q == 1) :
                menu(1)
                Q=int(input("\nSelect an option: "))
                if ( Q == 1 ):
                    askai()
                elif ( Q == 2 ):
                    search_term()

            elif ( Q == 5 ):
                return
        except: # to except errors
            print(EOFError())
            print('\n' + 'Oops! Something went wrong, please try again...' + '\n')



main()
