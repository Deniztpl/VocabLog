import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def get_word_meaning_in_sentence(sentence, word):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. When given a word and the sentence it appears in, provide a brief and clear definition of that word based on the context. Do not quote the original word or fully restate the sentence. Instead, offer a concise contextual definition in one or two short sentences.",
            },
            {
                "role": "user",
                "content": f"Can you explain the meaning of the word '{word}' in the sentence: \"{sentence}\"?",
            },
        ],
    )
    return response.choices[0].message.content


sentence = "they are only a portion of the benefit that the integrated debugger brings to the table."
word = "portion"
meaning = get_word_meaning_in_sentence(sentence, word)
print(f"Sentence: {sentence}")
print(f"Word: {word}")
print(f"\t{meaning}")
