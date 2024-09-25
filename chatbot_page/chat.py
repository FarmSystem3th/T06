import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# 환경 변수 로드
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 모델 설정 (gpt-4-turbo)
# llm = ChatOpenAI(api_key=OPENAI_API_KEY, model_name="gpt-4-turbo")

# 모델 설정 (gpt-4o)
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model_name="gpt-4o")

output_parser = StrOutputParser()

def chat_bot(user_input, conversation_history):
    # 대화 기록을 프롬프트에 전달
    history_str = '\n'.join(conversation_history)

    # 프롬프트 설정
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",
             "당신은 학대 아동 상담 전문가입니다. 아이들이 안심할 수 있도록 존댓말과 순화된 표현을 사용하며, 학대 아동을 판별하기 위한 특화된 질문을 합니다. 불필요한 말은 하지 않고, 초등학생을 대상으로 하므로 너무 깊거나 어려운 질문은 피합니다. 특정 부분에만 집중하지 않고 다양한 질문을 하며, 아이의 감정을 상하게 하지 않도록 주의합니다. 동일하거나 비슷한 질문을 반복하지 말아주세요. 당신이 말할 수 있는 횟수는 총 6번임을 명심하세요. 법적 및 윤리적 규정을 준수하며, 응답은 한 가지 질문이나 위로의 말로 구성합니다."),
            ("user", f"지금까지의 대화:\n{history_str}\n사용자: {user_input}\n상담사로서 다음에 어떻게 응답하시겠습니까?")
        ]
    )
    chain = prompt | llm | output_parser

    # GPT 호출
    response = chain.invoke(input={"input": user_input})

    return response
