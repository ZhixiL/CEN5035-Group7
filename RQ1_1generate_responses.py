from openai import OpenAI
import os
from helper import writeToCSV, getData
apikey = "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"

def get_response_setting(input):
    client = OpenAI(api_key=apikey)
    
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": input
            }
        ]
    )
    return resp.choices[0].message.content.strip()

def gen_new_response(path, start, end, file):
    csv_list = []
    res_list = getData(path)
    setting = "If you have to write code, write it as efficiently as you can. If your response does not involve coding, keep your answer precise and well thought out."

    for i in range(start, end):
        current_element = list(res_list[i])
        new_prompt = res_list[i][0] + ' ' + setting
        current_element.append(new_prompt)
        new_res = get_response_setting(new_prompt)
        current_element.append(new_res)
        csv_list.append(current_element)
    writeToCSV(csv_list, file)   

if __name__ == "__main__":
    path = "./given_datasets/20231012_230826_commit_sharings.json"
    gen_new_response(path, 0, 80, "RQ1_first_half_resp.csv")
    gen_new_response(path, 80, 148, "RQ1_second_half_resp.csv")
    