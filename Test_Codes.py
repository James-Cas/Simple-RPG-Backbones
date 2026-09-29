import time
import json
import os

# Functions
def show_player():
    print("---- Player Info ----")
    for three_num in player_player:
        print(three_num)
    print("---- Skills Info ----")
    for four_num in skills_player:
        print(four_num)
    for after_six_num in game_states:
        print(after_six_num)
    print()

# A Text Editor
def text_editor():
    if "reading and writing" in skills_player:
        print("Do not name your page one of these names.")
        for five_num in book_list:
            print(five_num)

        while True:
            print()
            file_soon = input("Enter filename: ")

            print()

            if file_soon in [s.lower() for s in book_list]:
                filename = file_soon
                break
            else:
                print("What did I tell you about names?\n")

        try:
            with open(filename, "r") as file:
                text = file.read()
            print("\nCurrent file contents:")
            print()
            print(text)

        except FileNotFoundError:
            text = ""
            print("\nFile does not exist. Creating a new file.")

        print("\nType your text below.")
        print("Type SAVE on a new line when finished.\n")
        print()
        new_text = []
        while True:
            line = input()
            if line == "SAVE":
                break
            new_text.append(line)

        with open(filename, "w") as file:
            file.write("\n".join(new_text))
        print("\nText is Saved.")

# Opens a .txt file
def open_book():
    for six_number in book_list:
        print(six_number)
    
    print()
    file_soon = input("Type a file you want read:")
    if file_soon in [s.lower() for s in book_list]:
        with open(filename, "r") as file:
            content = file.read()
        print(content)
    else:
        print("That book hasn't been opened yet, or you SUCK at spelling just like me.")
        for number_books in range(101):
            print("You SUCK at spelling")

# Waits
def wait(long):
    time.sleep(long)

# Save Point
def save_point(kills_now, death_now, food_now, water_now, money_now):
    print("Saving Point......")
    wait(2.5)
    print("Five More Seconds......")
    wait(5)
    print("I forgot something, wait some more......")
    wait(2.5)
    print("I got it")

    with open("data_game.json", "r") as file:
        data = json.load(file)
    data["kills_player"] = kills_now
    data["death_player"] = death_now
    data["food_eat"] = food_now
    data["water_ate"] = water_now
    data["money_bank"] = money_now

def time_counter(long):
    elapsed = 0

    while elapsed < long:
        time.sleep(0.5)
        elapsed += 0.5
        print(f"Elapsed: {elapsed:.1f} seconds")

    print("Done!")

time_counter(10)