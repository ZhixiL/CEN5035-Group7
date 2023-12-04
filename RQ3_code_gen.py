import csv
import os
from openai import OpenAI
import itertools as it

apikey = input("Please provide ChatGPT API Key:")
def getNewGPTCode(input, withSetting, lang):
    client = OpenAI(api_key=apikey)
    contentCollect = f"The provided this python3 code as follows:\n{input['pyCode']}"
    contentCollect+= f"\nNow, convert the provided code to {lang}. Complete the implementation with the following {lang} code declaration: \n{input['InitialCode']}"
    contentCollect += "Make sure your response should be code only"
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": contentCollect
            }
        ]
    )
    return resp.choices[0].message.content.replace('```', '').replace('python','').strip()
def getInputs():
    default = []
    setting = []
    with open('SoftwareProjectDataSheet.csv', mode='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            if lines[3] == '1':
                default.append(lines[0]+'_no')
            if lines[6] == '1':
                setting.append(lines[0]+'_setting')
    return [default, setting]
def getFileNames(inputs):
    out = []
    allfiles = [f for f in os.listdir('./LC_Gen_Codes')]
    for fn in allfiles:
        if fn[:7] in inputs[0]:
            out.append(fn)
        if fn[:12] in inputs[1]:
            out.append(fn)
    
    return out
if __name__ == "__main__":
    inputs = getInputs()
    fileInputs = getFileNames(inputs)
    for files in fileInputs:
        gptInput = dict()
        setting = True
        if files[5:7] == 'no':
            setting = False
        with open('./LC_Gen_Codes/'+files) as f:
            data = f.read()
            gptInput['pyCode'] = data
        
        with open('./InputDataCPlusPlus/'+files[:4]) as f:
            data = f.read()
            gptInput['InitialCode'] = data
        
        key = files[:4]
        if files[5:7] == 'no':
            f = open(f"./LC_Gen_Codes_CPlusPlus/{key}_no_setting.cpp", "w")
            f.write(getNewGPTCode(gptInput, setting, 'Java'))
            f.close()
        else:
            f = open(f"./LC_Gen_Codes_CPlusPlus/{key}_setting.cpp", "w")
            f.write(getNewGPTCode(gptInput, setting, 'C++'))
            f.close()