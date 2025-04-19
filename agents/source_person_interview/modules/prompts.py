"""프롬프트 템플릿 모듈

이 모듈은 LangChain 프롬프트 템플릿을 정의하고 반환하는 함수들을 포함합니다.
각 함수는 특정 작업에 맞는 프롬프트 템플릿을 생성합니다.
"""

from langchain_core.prompts import PromptTemplate

# 예시 프롬프트 함수들입니다. 참고용으로 남겨둡니다.

# def get_question_preparation_prompt() -> PromptTemplate:
#     """
#     Source Person Interview 질문 준비를 위한 프롬프트 템플릿을 반환합니다.
#
#     이 프롬프트는 인터뷰 주제, 인터뷰 대상자 정보, 전문 분야를 입력으로 받아
#     효과적인 Source Person Interview 질문을 생성하도록 설계되었습니다.
#
#     Returns:
#         PromptTemplate: 질문 준비를 위한 프롬프트 템플릿
#     """
#     template = """
#     당신은 교육 분야의 전문가 인터뷰 전문가입니다.
#     아래 정보를 바탕으로 효과적인 Source Person Interview 질문 목록을 생성해주세요.
#
#     # 인터뷰 주제
#     {interview_topic}
#
#     # 인터뷰 대상자 정보
#     {source_person}
#
#     # 전문 분야
#     {expertise_area}
#
#     # 지침
#     - 개방형 질문을 사용하여 대상자가 자유롭게 의견을 표현할 수 있도록 합니다.
#     - 대상자의 전문성과 경험을 끌어낼 수 있는 질문을 구성합니다.
#     - 교육적 맥락에 맞는 질문을 구성합니다.
#     - 최소 5개, 최대 10개의 질문을 생성합니다.
#     - 질문은 논리적 순서로 배열되어야 합니다.
#     - 질문은 명확하고 이해하기 쉬워야 합니다.
#
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
#
#
# def get_insight_extraction_prompt() -> PromptTemplate:
#     """
#     인터뷰 응답에서 통찰 추출을 위한 프롬프트 템플릿을 반환합니다.
#
#     이 프롬프트는 인터뷰 응답, 질문, 주제, 전문 분야를 입력으로 받아
#     중요한 통찰을 추출하도록 설계되었습니다.
#
#     Returns:
#         PromptTemplate: 통찰 추출을 위한 프롬프트 템플릿
#     """
#     template = """
#     당신은 교육 분야의 인터뷰 분석 전문가입니다.
#     아래 인터뷰 내용을 분석하고 주요 통찰을 추출해주세요.
#
#     # 인터뷰 주제
#     {interview_topic}
#
#     # 전문 분야
#     {expertise_area}
#
#     # 인터뷰 질문
#     {questions}
#
#     # 인터뷰 응답
#     {responses}
#
#     # 지침
#     - 주요 통찰과 핵심 아이디어를 식별하세요.
#     - 교육적 맥락에서 중요한 개념과 원칙을 추출하세요.
#     - 실용적인 조언과 적용 가능한 전략을 찾아내세요.
#     - 데이터에 기반한 객관적인 분석을 제공하세요.
#     - 교육 콘텐츠 개발에 활용할 수 있는 요소를 강조하세요.
#
#     다음 구조로 통찰 목록을 작성해주세요:
#
#     ## 주요 통찰
#     1. [첫 번째 통찰]
#     2. [두 번째 통찰]
#     ...
#
#     ## 핵심 개념
#     - [개념 1]: [설명]
#     - [개념 2]: [설명]
#     ...
#
#     ## 실용적 적용
#     - [적용 방안 1]
#     - [적용 방안 2]
#     ...
#     """
#     return PromptTemplate.from_template(template)
