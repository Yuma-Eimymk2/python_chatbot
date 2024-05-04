from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPEN_AI_KEY"])

# 会話履歴を管理する変数
messages = [
    {'role': 'system', 'content': 'あなたは心優しい癒やし系の恋人です'}
]

# chatgptAPIを呼び出す
def chat_completion(messages):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    # 応答からChatGPTの返答を取り出して返す
    content = response.choices[0].message.content
    return content

print('ChatGPTと会話します。終了したいときはCtrl+Cを押してください。')

# 連続で会話を繰り返す
while True:
    print('---') 
    # ユーザーからの入力を取得
    prompt = input(">>> ")
    # ユーザーの入力会話履歴に追加
    messages.append({'role': 'user', 'content': prompt})
    # ChatGPTによる応答を取得
    response = chat_completion(messages)
    # ChatGPTの応答を表示
    print("(^o^): ", response)
    # ChatGPTの応答履歴を追加
    messages.append({'role': 'assistant', 'content': response})