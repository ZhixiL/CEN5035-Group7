import os
import itertools as it
import json

def getLC_files():
    path = "./CustomInputData"
    os.chdir(path)
    lc_prompts = {}
    for file in os.listdir():
        file_path = f"{os.path.join(os.getcwd())}/{file}"
        with open(file_path, 'r') as f:
            input = dict()
            counter = 0
            for key,group in it.groupby(f,lambda line: line.startswith('-----PARTBREAKER-----')):
                if not key:
                    group = list(group)
                    group_str = ''.join(map(str,group)).strip()
                    
                    if counter == 0:
                        input['question'] = group_str
                    elif counter == 1:
                        input['input_output'] = group_str
                    elif counter == 2:
                        input['difficulty'] = group_str
                    elif counter == 3:
                        input['acceptance_rate'] = group_str
                    elif counter == 4:
                        input['constraints'] = group_str
                    elif counter == 5:
                        input['initial_code'] = group_str
                    counter += 1
            lc_prompts[file] = input
    return lc_prompts

def getData(file):
    resList = list()
    with open(file, "r") as f:
        data_dict = json.loads(f.read().encode('UTF8'))
        allMessages = data_dict["Sources"][:]
        for i in range(len(allMessages)):
            try:
                if (allMessages[i]["ChatgptSharing"][0]["NumberOfPrompts"] == 2):
                    if (len(allMessages[i]["ChatgptSharing"][0]["Conversations"]) != 0):
                        resList.append([allMessages[i]["ChatgptSharing"][0]["Conversations"][0]["Prompt"], allMessages[i]["ChatgptSharing"][0]["Conversations"][0]["Answer"]])   
            except KeyError:
                continue
    return resList
