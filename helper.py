import pandas as pd
def writeToCSV(responseList, fileName):
    headers = ["Prompt", "Response", "newPrompt", "newResponse"]
    df = pd.DataFrame(responseList, columns=headers)
    df.to_csv(fileName, index=False)  