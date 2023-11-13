from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from scipy.spatial import distance
from helper import readCSV, writeToCSV
from openai import OpenAI

apikey = "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"

def getChatGPTScore(response1, response2):
    client = OpenAI(api_key=apikey)
    query = "Analyze the following two inputs and determine the similarity score of the inputs based on factors like structure and logic. ONLY respond in number between 0 to 100, do not include anything else in your message:\n" + response1 + "\n" + response2
    resp = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )
    return resp.choices[0].message.content.strip()
    
def processGPTScore():
    queries = readCSV("output2.csv")
    queries.extend(readCSV("output1.csv"))
    h = ["Prompt", "ChatGPTScore"]
    chatGPTResult = []
    for i in range(len(queries)):
        curQuery = [queries[i][0]]      #append prompt first
        curQuery.append(getChatGPTScore(queries[i][1], queries[i][3]))      #get GPT Score and then append it
        chatGPTResult.append(curQuery)
    writeToCSV(chatGPTResult, "ChatGPT_Score.csv", h)
        

if __name__ == "__main__":
    processGPTScore()