import os
import requests
from country_list import countries_for_language
from bs4 import BeautifulSoup
import re

def soup(response):
    return BeautifulSoup(response.text, 'html.parser')

# make code in terminal look more colorful
def addColor(status_code):
    if status_code == 200:
        return '\033[92m' + 'OK' + '\033[0m'
    else:
        return '\033[91m' + 'ERROR' + '\033[0m'

def get_file_path(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, file_name)

def search_in_wikipedia(user_input, country_list):
    # Make a list of countries in Latvian with underscores instead of spaces (for wiki URL, that uses underscores)
    new_list = []
    for key, value in country_list.items():
        new_list.append(value.replace(' ', '_'))

    for index, value in enumerate(new_list):
        total_findings = 0
        #  Make a request to each wiki page
        req = requests.get(f'https://lv.wikipedia.org/wiki/{value}')
        # Loading screen for seeing progress, because it takes quite a while
        # If response code is 200, then it is OK, if not(404), then there is an ERROR (probably no such page)
        print(f"Loading: {index + 1}/{len(new_list)}  {value} {addColor(req.status_code)}")

        # Here is all we need (html)
        soup_obj = soup(req)

        # for this, we need only p (paragraphs) tags
        paragraphs = soup_obj.find_all('p')
        for paragraph in paragraphs:

            #get_text() method returns only text from html tags (with no links etc.)
            text = paragraph.get_text()

            # to find all occurrences of the user_input
            matches = re.finditer(re.escape(user_input), text, re.IGNORECASE)
            plain_text_before = ''
            for match in matches:
                start = match.start()
                end = match.end()
                total_findings += 1
                # to highlight the text
                highlighted_text = text[:start] + '\033[92m' + text[start:end] + '\033[0m' + text[end:]
                # no highlighting, for storing in the file
                plain_text = text[:start] + text[start:end] + text[end:]
                print(f"Found {value}:")
                print(highlighted_text)
                print("="*40)
                # put in a separate file
                if plain_text_before != plain_text:
                    file_path = get_file_path('wiki_data.txt')
                    with open(file_path, 'a', encoding='utf-8') as f:
                        f.write(value + '\n' + plain_text + '\n' + '='*40 + '\n')
                # had bug, that it was writing the same text multiple times, so this is to prevent that
                plain_text_before = plain_text

        # add total findings to the file for each country
        if total_findings > 0:
            file_path = get_file_path('wiki_data.txt')
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(f"Found {total_findings} words {user_input} in {value} \n \n \n")

def delete_wiki_data_file():
    file_path = get_file_path('wiki_data.txt')
    if os.path.exists(file_path):
        os.remove(file_path)
        print("The 'wiki_data.txt' file has been deleted.")
    else:
        print("The 'wiki_data.txt' file does not exist.")

    # make a list of countries in Latvian
countries = dict(countries_for_language('lv'))

while True:
    user_input = input("Enter word you are searching (in Latvian): ")

    # search in wiki
    search_in_wikipedia(user_input, countries)

    # ask for the next action and take action
    action = input("Enter 'y' to continue searching, 'q' to quit, or 'd' to delete the 'wiki_data.txt' file: ")
    if action.lower() == 'q':
        break
    elif action.lower() == 'd':
        delete_wiki_data_file()
    else:
        print("Continuing the search.")