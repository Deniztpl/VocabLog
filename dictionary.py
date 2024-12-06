import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

# TODO Add UI.
# TODO Add Database.
# TODO Improve answers.

API_KEY = os.environ["WEBSTER_API_KEY"]
sentence = input("Enter the sentence: ")
word = input("Enter the word: ")
URL = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={API_KEY}"
response = requests.get(URL)
dict_data = response.json()


try:
    definitions = dict_data[0]["shortdef"]
    with open("dictionary.txt", "a") as file:
        text = f"Sentence: {sentence} \nWord: {word}"
        for definiton in definitions:
            text += f"\n\t{definiton.capitalize()}"
        text += "\n\n"
        file.write(text)
except:
    print("No word found. Suggested words:", dict_data)
