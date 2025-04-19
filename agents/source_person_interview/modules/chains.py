"""LangChain 체인을 설정하는 함수 모듈

LCEL(LangChain Expression Language)을 사용하여 체인을 구성합니다.
기본적으로 modules.prompt 템플릿과 modules.models 모듈을 사용하여 LangChain 체인을 생성합니다.
"""

# from langchain.schema.runnable import RunnablePassthrough, RunnableSerializable
# from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
# from langchain_core.pydantic_v1 import BaseModel, Field

# from agents.source_person_interview.modules.models import get_openai_model
# from agents.source_person_interview.modules.prompts import (
#     get_question_preparation_prompt,
#     get_insight_extraction_prompt,
# )

# 예시 체인 함수들입니다. 참고용으로 남겨둡니다.


# def set_question_preparation_chain() -> RunnableSerializable:
#     """
#     인터뷰 질문 준비에 사용할 LangChain 체인을 생성합니다.
#
#     이 함수는 LCEL(LangChain Expression Language)을 사용하여 체인을 구성합니다.
#     체인은 다음 단계로 구성됩니다:
#     1. 입력에서 interview_topic, source_person, expertise_area를 추출하여 프롬프트에 전달
#     2. 프롬프트 템플릿에 값을 삽입하여 최종 프롬프트 생성
#     3. LLM을 호출하여 질문 준비 수행
#     4. 결과를 JSON으로 파싱하여 질문 목록 반환
#
#     Returns:
#         RunnableSerializable: 실행 가능한 체인 객체
#     """
#     # 질문 준비를 위한 프롬프트 가져오기
#     prompt = get_question_preparation_prompt()
#     # OpenAI 모델 가져오기
#     model = get_openai_model()
#     # JSON 출력 파서 설정
#     parser = JsonOutputParser(pydantic_object=InterviewQuestions)
#
#     # LCEL을 사용하여 체인 구성
#     return (
#         # 입력에서 필요한 필드 추출 및 프롬프트에 전달
#         RunnablePassthrough.assign(
#             interview_topic=lambda x: x["interview_topic"],  # 인터뷰 주제 추출
#             source_person=lambda x: x["source_person"],  # 인터뷰 대상자 정보 추출
#             expertise_area=lambda x: x["expertise_area"],  # 전문 분야 추출
#         )
#         | prompt  # 프롬프트 적용
#         | model  # LLM 모델 호출
#         | parser  # 결과를 JSON으로 파싱
#     )


# def set_insight_extraction_chain() -> RunnableSerializable:
#     """
#     인터뷰 통찰 추출에 사용할 LangChain 체인을 생성합니다.
#
#     이 함수는 LCEL(LangChain Expression Language)을 사용하여 체인을 구성합니다.
#     체인은 다음 단계로 구성됩니다:
#     1. 입력에서 responses, questions, interview_topic, expertise_area를 추출하여 프롬프트에 전달
#     2. 프롬프트 템플릿에 값을 삽입하여 최종 프롬프트 생성
#     3. LLM을 호출하여 통찰 추출 수행
#     4. 결과를 문자열로 변환
#
#     Returns:
#         RunnableSerializable: 실행 가능한 체인 객체
#     """
#     # 통찰 추출을 위한 프롬프트 가져오기
#     prompt = get_insight_extraction_prompt()
#     # OpenAI 모델 가져오기
#     model = get_openai_model()
#
#     # LCEL을 사용하여 체인 구성
#     return (
#         # 입력에서 필요한 필드 추출 및 프롬프트에 전달
#         RunnablePassthrough.assign(
#             responses=lambda x: x["responses"],  # 인터뷰 응답 추출
#             questions=lambda x: x["questions"],  # 인터뷰 질문 추출
#             interview_topic=lambda x: x["interview_topic"],  # 인터뷰 주제 추출
#             expertise_area=lambda x: x["expertise_area"],  # 전문 분야 추출
#         )
#         | prompt  # 프롬프트 적용
#         | model  # LLM 모델 호출
#         | StrOutputParser()  # 결과를 문자열로 변환
#     )
