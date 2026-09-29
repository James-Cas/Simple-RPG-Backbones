#!/usr/bin/env python3
import time
import json
import os
import sys
from Game_Functions import *

# Intro to Simple-RPG
# A game about nothing
# First made by J.C on July 30, 2026

# The code was created on July 30, 2026 but it wasn't until September 26
# When the idea was created

# Starting Up
os.system("cls" if os.name == "nt" else "clear")
print("Welcome to the game called Simple-RPG.")
print("This is a very simple and light RPG written in Python.")
print()
print("Lets start the game now. Do you want to boot up Simple-RPG?")
start_up = input("Yes, No, or Save Files: ")
start_up_clean = start_up.strip().lower()

print()
player_data = None

if start_up_clean == "yes":
    # Player
    print()
    print("Create your player. Very simple stuff right now.")
    name_player = input("Name: ").lower()

    while True:
        age_input = input("Age: ")
        if age_input.isdigit():
            age_player = int(age_input)
            break
        print("Please enter a whole number for age.\n")

    gender_player = input("Gender: ").lower()
    print()

    # Skills
    print("Moving on to skills. You can choose 3 (THREE) skills and one useless skill.")
    print("Useless skills do nothing to help you but they do help to make the game a bit more fun.")
    print()

    list_skills = ("Fighting", "Reading and Writing", "Stealing", "Running", "Math and Money", "Leading")
    useless_skill = ("Computer Science", "More Reading and Writing", "Chess")

    for number in list_skills:
        print(number)

    while True:
        print()
        one_skill = input("First Skill: ").lower()
        two_skill = input("Second Skill: ").lower()
        three_skill = input("Third Skill: ").lower()

        print()
        for number_number in useless_skill:
            print(number_number)

        useless_player = input("Useless Skill: ").lower()

        if (one_skill in [s.lower() for s in list_skills]
                and two_skill in [s.lower() for s in list_skills]
                and three_skill in [s.lower() for s in list_skills]
                and useless_player in [s.lower() for s in useless_skill]):
            print()
            print("You can pass to the next step")
            print("If you type the same three things I don't care.")
            print()
            break
        else:
            print("Your inputs does not match the list.\n")

    player_data = {
        "name": name_player,
        "age": age_player,
        "gender": gender_player,
        "jobs": "Useless Man",
        "one_skill": one_skill,
        "two_skill": two_skill,
        "three_skill": three_skill,
        "useless_skill": useless_player,
        "kills_player": 0,
        "death_player": 0,
        "food_eat": 100,
        "water_ate": 100,
        "money_bank": 100,
    }

    print(f"Here is your player: {name_player}, age {age_player}, {gender_player}")
    print(f"Here is your list of skills: {one_skill}, {two_skill}, {three_skill}, {useless_player}")

    with open("data_game.json", "w") as file:
        json.dump(player_data, file, indent=4)

elif start_up_clean == "save files":
    try:
        with open("data_game.json", "r") as file:
            player_data = json.load(file)
        print("Welcome back!")
        print()
        show_player(player_data)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No save file was found. Please start a new game instead.")
        sys.exit()

# THIS IS ONLY FOR ME
# IF I SEE ANYONE ELSE USE THIS I WILL END THEM
elif start_up == "SKIP PROGRAM":
    print("Welcome to the testing mode for pure testing only.")
    player_data = {
        "name": "tester",
        "age": 0,
        "gender": "n/a",
        "jobs": "Useless Man",
        "one_skill": "SKIP PROGRAM",
        "two_skill": "SKIP PROGRAM",
        "three_skill": "SKIP PROGRAM",
        "useless_skill": "SKIP PROGRAM",
        "kills_player": 0,
        "death_player": 0,
        "food_eat": 100,
        "water_ate": 100,
        "money_bank": 100,
    }

else:
    print("Programm has ended.")
    for number_no_start in range(100000000000000000000000000000000000000000000000000000000000000000000000000001):
        print(number_no_start)
    sys.exit()

# Creating JSON files for Data
# (World data lives here in code and gets written out fresh each run.)
book_data = {
    "dimension_rule": {
        "names": ["Dimension Rule", "DR"],
        "short": [
            "Created by Someone",
            "Eassy on the theory that we live in functions"
        ],
    },
    "changes_in_speed": {
        "names": ["Changes in Speed", "CS"],
        "short": [
            "Created by Someone",
            "Eassy add onto Dimesion Rule"
        ],
    },
    "holy_text": {
        "names": ["Holy Text", "HT"],
        "short": [
            "Placeholder",
            "Placeholder"
        ],
    }
}

town_data = {
    "royse_city": {
        "names": ["Royse City", "RC"],
        "facts": [
            "Founded in 1886",
            "Located in Rockwall County"
        ],
        "population": 20000,
        "neighbors": {
            "fate": 4,
            "nevada": 10
        }
    },
    "fate": {
        "names": ["Fate", "FT"],
        "facts": [
            "Fast growing city",
            "East of Dallas"
        ],
        "population": 25000,
        "neighbors": {
            "royse_city": 4,
            "nevada": 8
        }
    },
    "nevada": {
        "names": ["Nevada", "NV"],
        "facts": [
            "Small rural town",
            "Located in Collin County"
        ],
        "population": 1500,
        "neighbors": {
            "royse_city": 10,
            "fate": 8
        }
    }
}

people_data = {
    "james": {
        "nick-names": ["James", "Smith"],
        "house": "Fate",
        "job": "Read",
        "information": [
            "He likes to read",
            "Placeholder"
        ],
    },
    "tom": {
        "nick-names": ["Tom", "Paul"],
        "house": "Royse City",
        "job": "Make",
        "information": [
            "He bakes food",
            "Placeholder"
        ],
    },
    "alex": {
        "nick-names": ["Alex", "Sam"],
        "house": "Nevada",
        "job": "Music",
        "information": [
            "He likes to make music",
            "Placeholder"
        ],
    }
}

book_list = tuple(book_data.keys())

with open("book_data.json", "w") as file:
    json.dump(book_data, file, indent=4)

with open("town_data.json", "w") as file:
    json.dump(town_data, file, indent=4)

with open("people_data.json", "w") as file:
    json.dump(people_data, file, indent=4)

print()
print("I am very deep in this game now")
wait(1)
print("I have no idea how the output will look")
wait(1)
print("I made it so in 5 seconds I will clean this screen")
print()
print()

time_counter(5)

os.system("cls" if os.name == "nt" else "clear")

# The Game has been started
print("  ____  _                 _                ____  ____   ____")
wait(0.4)
print(" / ___|(_)_ __ ___  _ __ | | ___          |  _ \|  _ \ / ___|")
wait(0.4)
print(" \___ \| | '_ ` _ \| '_ \| |/ _ \  _____  | |_) | |_) | |  _")
wait(0.4)
print("  ___) | | | | | | | |_) | |  __/ |_____| |  _ <|  __/| |_| |")
wait(0.4)
print(" |____/|_|_| |_| |_| .__/|_|\___|         |_| \_\_|    \____|")
wait(0.4)
print("                   |_|")
wait(1)

print()
print("A program by James Cas")
print("About Nothing but Code")
print()

# ---- Main Game Loop ----
current_town = "royse_city"

while True:
    print("\nWhat would you like to do?")
    print("1) View Player Info")
    print("2) Look Around Town")
    print("3) Write/Edit a Page")
    print("4) Read a Book")
    print("5) Save Game")
    print("6) Quit")
    choice = input("> ").strip()

    if choice == "1" or choice.lower() == "view player info":
        show_player(player_data)
    elif choice == "2" or choice.lower() == "look around town":
        show_town(current_town, town_data)
    elif choice == "3" or choice.lower() == "write/edit a page" or choice.lower() == "write" or choice.lower() == "edit":
        text_editor(player_data, book_list)
    elif choice == "4" or choice.lower() == "read a book" or choice.lower() == "read":
        open_book(book_list)
    elif choice == "5" or choice.lower() == "save game" or choice.lower() == "save":
        save_point(player_data)
    elif choice == "6" or choice.lower() == "quit":
        print("Epstein Fuck Niggers!")
        break
    else:
        print("That's not an option.")
