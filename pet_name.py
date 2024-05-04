# ペットの名前を５つ考えて表示する
import openai
import os

# apiキー

# ChatGPTのAPIを呼び出す


def call_chatgpt(prompt, debug=False):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    # 応答内容を表示
    if debug:
        print(response)
    # 応答から返答を取り出す
    content = response.choices[0].message.content
    return content


# ペットの名前を生成して表示
pet_names = call_chatgpt("ペットの名前を5つ考えて", debug=True)
print(pet_names)
