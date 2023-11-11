# Leetcode Generation Code
from read_file import getLC_files
from openai import OpenAI
import os
apikey = "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"

def getGPTCode(input, withSetting):
    client = OpenAI(api_key=apikey)
    contentCollect = f"The question prompt is as follows:\n{input['question']}"
    contentCollect += f"\nYou are provided with the sample inputs/outputs and explainations\n{input['input_output']}"
    if withSetting:
        contentCollect += f"\nPlease consider the following constraints\n{input['constraints']}"
    contentCollect+= f"\nNow, provided with the following python3 code function declaration, complete the implementation\n{input['initial_code']}"
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
    

if __name__ == "__main__":
    # run arbitrary amount of code generation.
    apikey = input("What is your API Key: ")
    start, end, ctr = int(input("Start reading from: ")), int(input("End reading at: ")), 1
    cur_path = os.getcwd()
    data = getLC_files()
    for key in data.keys():
        if ctr < start:
            continue
        if ctr > end:
            break
        ctr += 1
        f = open(f"{cur_path}/LC_Gen_Codes/{key}_setting.py", "w")
        f.write(getGPTCode(data[key], True))
        f.close()   
        f = open(f"{cur_path}/LC_Gen_Codes/{key}_no_setting.py", "w")
        f.write(getGPTCode(data[key], False))
        f.close()   