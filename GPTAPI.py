from openai import OpenAI, AsyncOpenAI

initdi = {'prompt': "You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n. For each index i, names[i] and heights[i] denote the name and height of the ith person.Return names sorted in descending order by the people's heights.",
                    "constraint": "n == names.length == heights.length"}

#works fine
def getOneResponse(dict):
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Generate me a python3 funciton that does the follows: " + dict['prompt']
            },
            {
                "role": "user",
                "content": "Please re-generate providing the following constraints: " + dict['constraint']
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion)

#Doesn't work
def batchReq(dict):
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key="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",
    )
    prompts = ["Generate me a python3 funciton that does the follows: " + dict['prompt'], "Please re-generate providing the following constraints: " +dict['constraint']]
    
    # batched example, with 10 story completions per request
    response = client.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompts,
        max_tokens=100,
    )
    
    # match completions to prompts by index
    stories = [""] * len(prompts)
    for choice in response.choices:
        stories[choice.index] = prompts[choice.index] + choice.text
    
    # print stories
    for story in stories:
        print(story)

# be careful not to exceed 3 request per minute
async def getBunchResponse(dict):
    async_client = AsyncOpenAI()
    stream = await async_client.chat.completions.create(
        prompt="Say this is a test",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    async for part in stream:
        print(part.choices[0].delta.content or "")

if __name__ == "__main__":
    getOneResponse(initdi)