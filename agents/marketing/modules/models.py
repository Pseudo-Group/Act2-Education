"""LLM 모델 설정 모듈

이 모듈은 LangChain에서 사용할 LLM 모델을 설정하고 반환하는 함수들을 포함합니다.
"""

# from langchain_openai import ChatOpenAI

# 예시 함수들입니다. 참고용으로 남겨둡니다.

# def get_openai_model() -> ChatOpenAI:
#     """
#     OpenAI 모델 인스턴스를 생성하고 반환합니다.
#
#     이 함수는 교육 마케팅 관련 작업에 적합한 설정으로
#     OpenAI의 ChatGPT 모델을 초기화합니다.
#
#     Returns:
#         ChatOpenAI: 초기화된 OpenAI 모델 인스턴스
#     """
#     # OpenAI 모델 초기화 및 반환
#     return ChatOpenAI(
#         model_name="gpt-4",  # 모델 이름 (gpt-4 사용)
#         temperature=0.7,  # 창의성 조절 (0.7은 균형 잡힌 창의성)
#         max_tokens=1500,  # 최대 토큰 수
#     )
