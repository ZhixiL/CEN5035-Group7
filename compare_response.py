from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from scipy.spatial import distance
from helper import readCSV, writeToCSV
from openai import OpenAI

apikey = "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"

# Jaccard index to get similarity between texts
def jaccard_similarity(text1, text2):
    text1_set = set(text1.lower().split(' '))
    text2_set = set(text2.lower().split(' '))
    # print(text1_set)
    # print(text2_set)
    intersection = len(text1_set.intersection(text2_set))
    union = len(text1_set.union(text2_set))

    return intersection/union

def cos_similarity(text1, text2):
    text1_c = Counter(text1.split(' '))
    text2_c = Counter(text2.split(' '))
    words  = list(text1_c.keys() | text2_c.keys())
    a_vect = [text1_c.get(word, 0) for word in words]       
    b_vect = [text2_c.get(word, 0) for word in words]  
    # print(words)
    # print(a_vect)
    # print(b_vect)
    return cosine_similarity([a_vect], [b_vect])

def euclidean_distance(text1, text2):
    texts = [text1, text2]
    count_vectorizer = CountVectorizer(stop_words='english')
    matrix = count_vectorizer.fit_transform(texts)
    table = matrix.todense()
    df = pd.DataFrame(table, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=['1', '2'])

    matrix = distance.cdist(df, df, 'euclidean')
    df_eucl = pd.DataFrame(matrix, 
                  columns= ["Text_1", "Text_2"],
                  index=['1','2'])
    return matrix[0][1]
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
    # outputs = readCSV("output1.csv")
    # outputs2 = readCSV("output2.csv")
    # h = ["Prompt", "Jaccard", "Cosine", "Euclidean Distance"]
    # similarityResult = []
    
    # for out in outputs:
    #     singleOutput = list(out[2])
    #     singleOutput.append(jaccard_similarity(out[1], out[3]))
    #     singleOutput.append(cos_similarity(out[1], out[3]))
    #     singleOutput.append(euclidean_distance(out[1], out[3]))
    #     similarityResult.append(singleOutput)
    
    # writeToCSV(similarityResult, "./simi_output.csv", h)
    processGPTScore()