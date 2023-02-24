import requests
import re
import urllib.request   # MVP
from datetime import date
import sys
import csv

r = requests.get("https://www.merriam-webster.com/word-of-the-day/" + str(date.today()))

def main():
    while True:
        print("\nPress 1 for today's word\nPress 2 to search date\nPress 3 to search for a word\n"
            "Type 'N' to exit\n")
        select = input()
        if select == "1": today_word()
        elif select == "2": new_word()
        elif select == "3": word_search()
        elif select.lower() == "n": sys.exit("Thank you!")


def today_word():
    html = urllib.request.urlopen("https://www.merriam-webster.com/word-of-the-day/" + str(date.today())).read()
    word = re.search(r"<title>Word of the Day: (.+?)(?: \|.+)$", str(html), re.IGNORECASE)
    definition = re.search(r"<h2>What It Means<\/h2>.+?(?:<\/em> )(.+?)(?:<\/p>.+)$", str(html), re.IGNORECASE)
    print(word.group(1))
    print(definition.group(1).replace("\\xe2\\x80\\x9c", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("<em>", "").replace("</em>", ""))


def new_word():
    wotd_date = input("Please enter a date in YYYY-MM-DD format: ")
    html = urllib.request.urlopen("https://www.merriam-webster.com/word-of-the-day/" + wotd_date).read()
    word = re.search(r"<title>Word of the Day: (.+?)(?: \|.+)$", str(html), re.IGNORECASE)
    definition = re.search(r"<h2>What It Means<\/h2>.+?(?:<\/em> )(.+?)(?:<\/p>.+)$", str(html), re.IGNORECASE)
    print(word.group(1))
    print(definition.group(1).replace("\\xe2\\x80\\x9c", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("\\xe2\\x80\\x99", "\'").replace("<em>", "").replace("</em>", ""))


def word_search():
    word_query = input("Please enter a word: ")
    html = urllib.request.urlopen("https://www.merriam-webster.com/dictionary/" + word_query).read()
    definition = re.search(r"<meta property=\"og:description\" content=\"(.+?)(?:\\xe2\\x80\\xa6.+)$", str(html), re.IGNORECASE)
    # definition = re.search(r"<meta property=\"og:description\" content=\"(.+?)(?: \:.+)$", str(html), re.IGNORECASE)
    print(word_query.title())
    print(definition.group(1).replace("\\xe2\\x80\\x94", "- ") + ".")


if __name__ == "__main__":
    main()