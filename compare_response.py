from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from scipy.spatial import distance

from openai import OpenAI
import os
apikey = "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"

# Jaccard index to get similarity between texts
def jaccard_similarity(text1, text2):
    text1_set = set(text1.lower().split(' '))
    text2_set = set(text2.lower().split(' '))
    print(text1_set)
    print(text2_set)
    intersection = len(text1_set.intersection(text2_set))
    union = len(text1_set.union(text2_set))

    return intersection/union

def cos_similarity(text1, text2):
    text1_c = Counter(text1.split(' '))
    text2_c = Counter(text2.split(' '))
    words  = list(text1_c.keys() | text2_c.keys())
    a_vect = [text1_c.get(word, 0) for word in words]       
    b_vect = [text2_c.get(word, 0) for word in words]  
    print(words)
    print(a_vect)
    print(b_vect)
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
    print(matrix)

if __name__ == "__main__":
    t1 = '''The expression ${GITHUB_REF#refs/heads/} is a parameter expansion in a shell script, often used in GitHub Actions workflows. In the context of GitHub Actions, GITHUB_REF is an environment variable that contains the branch or tag ref that triggered the workflow.

The expression ${GITHUB_REF#refs/heads/} is used to remove the prefix refs/heads/ from the value of GITHUB_REF. This is necessary because when a pull request is opened, the GITHUB_REF might contain the branch reference in the form refs/heads/branch-name. Removing this prefix leaves you with just the branch name.

So, if GITHUB_REF is refs/heads/develop, then ${GITHUB_REF#refs/heads/} would result in develop.

In your case, if you have a pull request for merging develop to main, ${GITHUB_REF#refs/heads/} would give you main because the base branch of the pull request is typically the target branch (main in this case). The workflow is triggered by the pull request event, and GITHUB_REF points to the branch reference of the base branch.

This expression is commonly used in GitHub Actions workflows to dynamically determine the branch names and perform actions based on the branch where the workflow is running.
'''

    t2 = '''The expression ${GITHUB_REF#refs/heads/} is used in GitHub Actions workflows to extract the branch name from the GITHUB_REF environment variable. This expression removes the prefix refs/heads/ from the branch reference, leaving only the branch name.

For example, if GITHUB_REF is refs/heads/develop, then ${GITHUB_REF#refs/heads/} would result in develop. In the context of pull requests, where the workflow is triggered by events like merging from develop to main, this expression helps dynamically obtain the target branch name (main in this case) for workflow actions.'''
    # print(cos_similarity(t1, t2))
    # print(jaccard_similarity(t1, t2))
    print(euclidean_distance(t1, t2))