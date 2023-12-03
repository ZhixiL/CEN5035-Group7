import csv
import os
from openai import OpenAI
import itertools as it
from time import sleep

apikey = "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"

def getNewGPTCode(input, withSetting, lang):
    client = OpenAI(api_key=apikey)
    contentCollect = f"The provided this python3 code as follows:\n{input['pyCode']}"
    contentCollect+= f"\nNow, convert the provided code to {lang}. Complete the implementation with the following {lang} code declaration: \n{input['InitialCode']}"
    # contentCollect += f"\nYou are provided with the sample inputs/outputs and explainations\n{input['input_output']}"
    # if withSetting:
    #     contentCollect += f"\nPlease consider the following constraints\n{input['constraints']}"
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
    # inputs = getInputs()
    # fileInputs = getFileNames(inputs)

    # for files in fileInputs:
    #     gptInput = dict()
    #     setting = True
    #     if files[5:7] == 'no':
    #         setting = False

    #     with open('./LC_Gen_Codes/'+files) as f:
    #         data = f.read()
    #         gptInput['pyCode'] = data
        
    #     with open('./InputDataCPlusPlus/'+files[:4]) as f:
    #         data = f.read()
    #         gptInput['InitialCode'] = data
        
    #     # with open('./CustomInputData/'+files, 'r') as f:
    #     #     counter = 0
    #     #     for key,group in it.groupby(f,lambda line: line.startswith('-----PARTBREAKER-----')):
    #     #         if not key:
    #     #             group = list(group)
    #     #             group_str = ''.join(map(str,group)).strip()
                    
    #     #             if counter == 1:
    #     #                 gptInput['input_output'] = group_str
    #     #             elif counter == 4:
    #     #                 gptInput['constraints'] = group_str
    #     #             counter += 1
    #     key = files[:4]
    #     if files[5:7] == 'no':
    #         f = open(f"./LC_Gen_Codes_CPlusPlus/{key}_no_setting.cpp", "w")
    #         f.write(getNewGPTCode(gptInput, setting, 'Java'))
    #         f.close()
    #     else:
    #         f = open(f"./LC_Gen_Codes_CPlusPlus/{key}_setting.cpp", "w")
    #         f.write(getNewGPTCode(gptInput, setting, 'C++'))
    #         f.close()