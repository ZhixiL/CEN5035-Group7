import openai
import os
import pandas as pd
openai.api_key = ''

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message["content"]

prompt = '''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
            Return the answer in any order. 
            A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.'''

response = get_completion(prompt)

print(response)