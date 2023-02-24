import requests
import re
import urllib.request   # MVP
from datetime import date
import sys
import csv
# should i use pandas?

r = requests.get("https://www.merriam-webster.com/word-of-the-day/" + str(date.today()))

def main():
    print("\nWelcome to your easy-access dictionary!")
    while True:
        print("\nPress 1 for today's word\nPress 2 to search date\nPress 3 to search for a word\n"
            "Press 4 to see your current dictionary\nType 'N' to exit\n")
        select = input()
        if select == "1": today_word()
        elif select == "2": new_word()
        elif select == "3": word_search()
        elif select == "4": read_dict()
        elif select.lower() == "n": sys.exit("\nThank you!\n")


def today_word():
    html = urllib.request.urlopen("https://www.merriam-webster.com/word-of-the-day/" + str(date.today())).read()
    word = re.search(r"<title>Word of the Day: (.+?)(?: \|.+)$", str(html), re.IGNORECASE)
    definition = re.search(r"<h2>What It Means<\/h2>.+?(?:<\/em> )(.+?)(?:<\/p>.+)$", str(html), re.IGNORECASE)
    clean_word = word.group(1)
    clean_def = definition.group(1).replace("\\xe2\\x80\\x9c", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("\\xe2\\x80\\x99", "\'").replace("<em>", "").replace("</em>", "")
    print(clean_word)
    print(clean_def)
    add_dict(clean_word, clean_def)


def new_word():
    wotd_date = input("Please enter a date in YYYY-MM-DD format: ")
    html = urllib.request.urlopen("https://www.merriam-webster.com/word-of-the-day/" + wotd_date).read()
    word = re.search(r"<title>Word of the Day: (.+?)(?: \|.+)$", str(html), re.IGNORECASE)
    definition = re.search(r"<h2>What It Means<\/h2>.+?(?:<\/em> )(.+?)(?:<\/p>.+)$", str(html), re.IGNORECASE)
    clean_word = word.group(1)
    clean_def = definition.group(1).replace("\\xe2\\x80\\x9c", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("\\xe2\\x80\\x99", "\'").replace("<em>", "").replace("</em>", "")
    print(clean_word)
    print(clean_def)
    add_dict(clean_word, clean_def)


def word_search():
    word_query = input("Please enter a word: ")
    html = urllib.request.urlopen("https://www.merriam-webster.com/dictionary/" + word_query).read()
    definition = re.search(r"<meta property=\"og:description\" content=\"(.+?)(?:\\xe2\\x80\\xa6.+)$", str(html), re.IGNORECASE)
    # definition = re.search(r"<meta property=\"og:description\" content=\"(.+?)(?: \:.+)$", str(html), re.IGNORECASE)
    clean_word = word_query.title()
    clean_def = definition.group(1).replace("\\xe2\\x80\\x94", "- ") + "."
    print(clean_word)
    print(clean_def)
    add_dict(clean_word, clean_def)


def add_dict(word, definition):
    add_dict = input("\nAdd to your Word List?\nPlease enter Y/N: ")
    if add_dict.lower() == "y": print("\nAdded to List!")
    with open("words.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([word, definition])


def read_dict():
    with open("words.csv", newline="") as file:
        for n, row in enumerate(file):
            print(n+1, row)
        print(f"You have {n+1} words in your dictionary. Great job!")

if __name__ == "__main__":
    main()