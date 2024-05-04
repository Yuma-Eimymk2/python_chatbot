from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPEN_AI_KEY"])

# apiキー


def completion(prompt, debug=False):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0,
    )
    if debug:
        print(response)
    content = response.choices[0].message.content
    return content


if __name__ == "__main__":
    result = completion(
        prompt="""
        あなたはサイコロです。
        ランダムに１以上６以下の整数を出力してください。
        """,
        debug=False,
    )
    print(result)
    