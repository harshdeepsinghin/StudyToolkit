# StudyToolkit Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
   - [Clone the Repository](#clone-the-repository)
   - [Virtual Environment Setup](#virtual-environment-setup)
   - [Install Dependencies](#install-dependencies)
3. [Google API Setup](#google-api-setup)
4. [Usage](#usage)
5. [Running the Program](#running-the-program)
6. [Main Menu Navigation](#main-menu-navigation)
   - [Submenu Functions](#submenu-functions)
     - [1. Study Menu](#1-study-menu)
     - [2. Note Menu](#2-note-menu)
     - [3. Retain Menu](#3-retain-menu)
     - [4. Utilities Menu](#4-utilities-menu)
7. [Detailed Functionality](#detailed-functionality)
   - [Note Functionality](#note-functionality)
   - [AI Interaction](#ai-interaction)
   - [Pomodoro Timer](#pomodoro-timer)
   - [Data Management](#data-management)
   - [Platform Compatibility](#platform-compatibility)
8. [Troubleshooting](#troubleshooting)
9. [Conclusion](#conclusion)

## Introduction
**StudyToolkit** is a Python-based program designed to assist users in studying more efficiently. Featuring a menu-driven interface, it provides tools and functionalities that help streamline the study process.

## Installation

### Clone the Repository
To get started, clone the repository and navigate into the project directory:

```bash
git clone https://github.com/harshdeepsinghin/StudyToolkit.git
cd StudyToolkit
```

### Virtual Environment Setup
Set up a virtual environment to manage dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies
Once inside the virtual environment, install the necessary packages:

```bash
pip3 install -r requirements.txt
```

## Google API Setup

To enable certain features, **StudyToolkit** requires a Google Gemini API key:

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey) to generate a Gemini API key.
2. In the project root directory, create a `.env` file and add the API key as shown:

   ```
   API_KEY = "AI**************************************"
   ```

## Usage

Run the program with the following command:

```bash
python3 StudyToolkit.py
```

The toolkit provides a menu-driven interface, guiding users through various options to support their study activities effectively.

## Running the Program

To start the application, run the following command in your terminal:
```bash
python study_toolkit.py
```

## Main Menu Navigation

Once the application starts, you'll be presented with the **Main Menu**. Here’s what you can do:

- **Study**: Access the Study submenu to ask AI questions or view your study notes.
- **Note**: Take different types of notes, such as term definitions, topic descriptions, and more.
- **Retain**: Quiz yourself on the notes you've taken to reinforce your memory.
- **Utilities**: Use the Pomodoro timer to manage your study sessions effectively.
- **Exit**: Exit the application.

### Submenu Functions

#### 1. Study Menu

In the Study submenu, you can choose to:
- **Ask AI**: Interact with the AI by asking questions related to your study material. You can type your question and receive responses from the AI.
- **Study Notes**: View your stored notes, which can include term definitions, topic descriptions, question-answer pairs, and miscellaneous notes.

#### 2. Note Menu

The Note submenu allows you to:
- **Term-Definition**: Add a term and its definition to your notes.
- **Topic-Description**: Add a topic and its description.
- **Question-Answer**: Add a question and its corresponding answer.
- **Miscellaneous Notes**: Open a text editor to add miscellaneous notes (currently implemented for Unix/Linux/Darwin systems).

#### 3. Retain Menu

In the Retain submenu, you can:
- **Quiz Yourself**: The program will randomly select a term, topic, or question from your notes and prompt you to match it with the correct answer through multiple-choice options.

#### 4. Utilities Menu

The Utilities submenu provides:
- **Pomodoro Timer**: Manage your study sessions with customizable work and break cycles. You can choose predefined options or enter your own settings.

## Detailed Functionality

### Note Functionality

**Taking Notes**
- You can add notes in different categories. After entering a term, topic, or question, the program will save this information for future reference. It will also prompt you that your note has been successfully recorded.

**Viewing Notes**
- The study notes can be viewed in their respective categories (term definitions, topic descriptions, question-answers, and miscellaneous notes). The program will format and display these notes in a color-coded manner for clarity.

### AI Interaction

**Asking AI**
- When using the Ask AI feature, simply type your question. You can exit this feature by typing "quit" or "exit." The program will send your query to the configured AI service and display the response in a formatted way.

### Pomodoro Timer

**Using the Timer**
- The Pomodoro timer allows you to set work and break intervals. You can choose predefined settings or customize them. Notifications will be sent at the start of each work and break session, helping you manage your time effectively.

### Data Management

**Loading and Saving Data**
- The program loads existing data from JSON files at startup, allowing you to retain your notes between sessions. Data is saved automatically whenever you add new notes, ensuring your work is always up-to-date.

### Platform Compatibility

- The program is designed to run on various platforms (Windows, Linux, macOS). Some functionalities (like editing miscellaneous notes) may have platform-specific implementations.

## Troubleshooting

- If you encounter issues running the program, check for missing dependencies and ensure your API key is correctly configured in the `.env` file.
- Ensure that the JSON files for storing notes (term_definition.json, topic_description.json, question_answer.json) exist in your working directory. If they do not exist, the program will create them automatically.

## Conclusion

The Study Toolkit is a versatile application for managing your study notes, interacting with AI, and enhancing your study efficiency through quizzes and timers. Feel free to explore all the menus and functionalities to make the most of your study sessions!