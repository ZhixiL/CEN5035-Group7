from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from scipy.spatial import distance
from helper import readCSV, writeToCSV

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


if __name__ == "__main__":
    outputs = readCSV("output1.csv")[1:]
    outputs2 = readCSV("output2.csv")[1:]
    h = ["Prompt", "Jaccard", "Cosine", "Euclidean Distance"]
    similarityResult = []
    
    for out in outputs:
        singleOutput = list(out[2])
        singleOutput.append(jaccard_similarity(out[1], out[3]))
        singleOutput.append(cos_similarity(out[1], out[3]))
        singleOutput.append(euclidean_distance(out[1], out[3]))
        similarityResult.append(singleOutput)
    
    writeToCSV(similarityResult, "./simi_output.csv", h)