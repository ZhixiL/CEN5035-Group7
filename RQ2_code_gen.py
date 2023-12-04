import csv
import os
from openai import OpenAI
import itertools as it
from time import sleep

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

def RQ2_Generate_GPT():
    client = OpenAI(api_key=apikey)
    PassedLC = getInputs()[0]
    fileNames = [x[:-3]+"_no_setting.py" for x in PassedLC]
    settings = {"I want 40 lines of code" : "VS1", "Give me fast and good code" : "VS2"}
    for file in fileNames:
        with open('./LC_Gen_Codes/'+file) as f:
            data = f.read()
            pythonCode = data
            for setting in settings.keys():
                Query = f"{setting} for this python code: \n {pythonCode}"
                resp = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "user",
                            "content": Query
                        }
                    ]
                )

                output = resp.choices[0].message.content.replace('```', '').replace('python','').strip()
                with open(f"./LC_Gen_Codes_RQ2/"+settings[setting]+"_"+file, "w") as outputFile:
                    outputFile.write(output)
                sleep(15)

if __name__ == "__main__":
    RQ2_Generate_GPT()