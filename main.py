from openai import OpenAI
import json

_Token = str(open("./GPTToken", "r").readline())
client = OpenAI(api_key=_Token)


def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return json.loads(response.model_dump_json())["choices"][0]["message"]["content"]


while True:
    prompt = input()
    if prompt == "exit":
        exit()
    response = chat_with_gpt(prompt)
    print(response)
