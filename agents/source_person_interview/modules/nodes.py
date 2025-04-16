"""
노드 클래스 모듈

이 모듈은 LangGraph Workflow에서 사용되는 Source Person Interview 관련 노드 클래스들을 정의합니다.
각 노드 클래스는 BaseNode를 상속받아 구현되며, Workflow 그래프에서 특정 기능을 수행하는 단위 컴포넌트입니다.
각 노드는 execute 메서드를 구현하여 상태(state)를 입력받아 처리하고, 처리 결과를 새로운 상태 업데이트로 반환합니다.
"""

from agents.base_node import BaseNode

# from agents.source_person_interview.modules.chains import set_question_preparation_chain, set_insight_extraction_chain

# 아래는 구현 예정인 노드 클래스들입니다. 실제 구현 시 주석을 해제하고 사용하면 됩니다.

# class QuestionPreparationNode(BaseNode):
#     """
#     Source Person Interview를 위한 질문을 준비하는 노드
#     
#     이 노드는 LangChain의 질문 준비 체인을 활용하여 Source Person Interview에 적합한 질문을 생성합니다.
#     인터뷰 주제, 인터뷰 대상자, 전문 분야에 맞게 질문을 생성하여 Workflow의 다음 단계로 전달합니다.
#     """
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)  # BaseNode 초기화
#         # set_question_preparation_chain 함수를 통해 LangChain 체인을 가져와 설정
#         self.chain = set_question_preparation_chain()  # 질문 준비 체인 설정
#
#     def execute(self, state) -> dict:
#         """
#         주어진 상태(state)에서 필요한 정보를 추출하여 인터뷰 질문을 준비하고 결과를 반환합니다.
#         
#         Args:
#             state (dict): Workflow의 현재 상태. interview_topic, source_person, expertise_area 정보를 포함함.
#         
#         Returns:
#             dict: 준비된 질문들을 포함한 상태 업데이트
#         """
#         # 질문 준비 체인 실행 - LLM을 통해 인터뷰 질문 생성
#         prepared_questions = self.chain.invoke(
#             {
#                 "interview_topic": state["interview_topic"],  # 인터뷰 주제
#                 "source_person": state["source_person"],  # 인터뷰 대상자 정보
#                 "expertise_area": state["expertise_area"],  # 전문 분야
#             }
#         )
#
#         # 준비된 질문을 새로운 상태 업데이트로 반환
#         return {"questions": prepared_questions}
#
#
# class InsightExtractionNode(BaseNode):
#     """
#     인터뷰 응답에서 통찰을 추출하는 노드
#     
#     이 노드는 LangChain의 통찰 추출 체인을 활용하여 Source Person Interview에서 수집된 응답에서 중요한 통찰을 추출합니다.
#     인터뷰 질문과 응답을 분석하여 교육 콘텐츠 제작에 활용할 수 있는 핵심 통찰을 추출하고, 이를 Workflow의 다음 단계로 전달합니다.
#     """
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)  # BaseNode 초기화
#         # set_insight_extraction_chain 함수를 통해 LangChain 체인을 가져와 설정
#         self.chain = set_insight_extraction_chain()  # 통찰 추출 체인 설정
#
#     def execute(self, state) -> dict:
#         """
#         주어진 상태(state)에서 인터뷰 응답과 관련 정보를 추출하여 통찰을 추출하고 결과를 반환합니다.
#         
#         Args:
#             state (dict): Workflow의 현재 상태. responses, questions, interview_topic, expertise_area 정보를 포함함.
#         
#         Returns:
#             dict: 추출된 통찰을 포함한 상태 업데이트
#         """
#         # 통찰 추출 체인 실행 - LLM을 통해 인터뷰 응답에서 통찰 추출
#         extracted_insights = self.chain.invoke(
#             {
#                 "responses": state["responses"],  # 인터뷰 응답
#                 "questions": state["questions"],  # 인터뷰 질문
#                 "interview_topic": state["interview_topic"],  # 인터뷰 주제
#                 "expertise_area": state["expertise_area"],  # 전문 분야
#             }
#         )
#
#         # 추출된 통찰을 새로운 상태 업데이트로 반환
#         return {"insights": extracted_insights}
