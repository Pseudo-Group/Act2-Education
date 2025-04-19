"""프롬프트 템플릿 모듈

이 모듈은 LangChain 프롬프트 템플릿을 정의하고 반환하는 함수들을 포함합니다.
각 함수는 특정 작업에 맞는 프롬프트 템플릿을 생성합니다.
"""

# from langchain_core.prompts import PromptTemplate

# def get_question_generation_prompt() -> PromptTemplate:
#     """
#     포커스 그룹 인터뷰 질문 생성을 위한 프롬프트 템플릿을 반환합니다.

#     이 프롬프트는 인터뷰 주제와 대상 청중을 입력으로 받아
#     효과적인 포커스 그룹 인터뷰 질문을 생성하도록 설계되었습니다.

#     Returns:
#         PromptTemplate: 질문 생성을 위한 프롬프트 템플릿
#     """
#     template = """
#     당신은 교육 분야의 포커스 그룹 인터뷰 전문가입니다.
#     아래 주제와 대상 청중에 맞는 효과적인 포커스 그룹 인터뷰 질문 목록을 생성해주세요.

#     # 인터뷰 주제
#     {interview_topic}

#     # 대상 청중
#     {target_audience}

#     # 지침
#     - 개방형 질문을 사용하여 참가자들이 자유롭게 의견을 표현할 수 있도록 합니다.
#     - 교육적 맥락에 맞는 질문을 구성합니다.
#     - 최소 5개, 최대 10개의 질문을 생성합니다.
#     - 질문은 논리적 순서로 배열되어야 합니다.
#     - 질문은 명확하고 이해하기 쉬워야 합니다.

#     다음 JSON 형식으로 질문 목록을 반환해주세요:
#     ```json
#     {
#       "questions": [
#         "질문 1",
#         "질문 2",
#         ...
#       ]
#     }
#     ```
#     """
#     return PromptTemplate.from_template(template)
