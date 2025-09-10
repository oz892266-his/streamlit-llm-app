from dotenv import load_dotenv

load_dotenv()


from langchain.schema import SystemMessage, HumanMessage
#from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

#llm = ChatOpenAI()  # 必要に応じて引数を追加

import streamlit as st

# Streamlitのタイトルと説明
st.title("課題提出アプリ: スポーツ・料理の専門家チャットボット")

st.write("##### スポーツモード: スポーツの専門家として質問に答えます。")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで質問に対して応答します。")
st.write("##### 料理モード: 料理の専門家として質問に答えます。")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで質問に対して応答します。")

# ラジオボタンでモード選択
selected_item = st.radio(
    "質問モードを選択してください。",
    ["スポーツモード", "料理モード"]
)

st.divider()

# 入力フォーム
user_input = st.text_input("質問を入力してください:")

# LLMの準備
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# 実行ボタン
if st.button("実行"):
    if user_input.strip() != "":
        # 選択されたモードに応じてシステムメッセージを切り替え
        if selected_item == "スポーツモード":
            system_message = "あなたはスポーツの専門家です。専門家の立場で答えてください。"
        else:
            system_message = "あなたは料理の専門家です。専門家の立場で答えてください。"

# LLMに渡すメッセージ
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=user_input),
        ]
# LLMに問い合わせ
        result = llm(messages)

        # 結果を画面に表示
        st.write("### 回答:")
        st.write(result.content)

    else:
        st.warning("質問を入力してください。")


