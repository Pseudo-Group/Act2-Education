"""
노드 클래스 모듈

이 모듈은 LangGraph Workflow에서 사용되는 노드 클래스들을 정의합니다.
각 노드 클래스는 BaseNode를 상속받아 구현되며, Workflow 그래프에서 특정 기능을 수행하는 단위 컴포넌트입니다.
각 노드는 execute 메서드를 구현하여 상태(state)를 입력받아 처리하고, 처리 결과를 새로운 상태 업데이트로 반환합니다.
"""

from agents.base_node import BaseNode

# from agents.focus_group_interview.modules.chains import set_question_generation_chain, set_response_analysis_chain


# class QuestionGenerationNode(BaseNode):
#     """
#     인터뷰 주제와 대상 청중에 적합한 질문을 생성하는 노드
#
#     이 노드는 LangChain의 질문 생성 체인을 활용하여 포커스 그룹 인터뷰에 적합한 질문을 생성합니다.
#     주어진 인터뷰 주제와 대상 청중에 맞게 질문을 생성하여 Workflow의 다음 단계로 전달합니다.
#     """

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)  # BaseNode 초기화
#         # set_question_generation_chain 함수를 통해 LangChain 체인을 가져와 설정
#         self.chain = set_question_generation_chain()  # 질문 생성 체인 설정

#     def execute(self, state) -> dict:
#         """
#         주어진 상태(state)에서 필요한 정보를 추출하여 질문을 생성하고 결과를 반환합니다.
#
#         Args:
#             state (dict): Workflow의 현재 상태. interview_topic과 target_audience 정보를 포함함.
#
#         Returns:
#             dict: 새로 생성된 질문들을 포함한 상태 업데이트
#         """
#         # 질문 생성 체인 실행 - LLM을 통해 질문 생성
#         generated_questions = self.chain.invoke(
#             {
#                 "interview_topic": state["interview_topic"],  # 인터뷰 주제
#                 "target_audience": state["target_audience"],  # 대상 청중
#             }
#         )

#         # 생성된 질문을 반환 - 새로운 상태 업데이트로 반환
#         return {"questions": generated_questions}


# class ResponseAnalysisNode(BaseNode):
#     """
#     인터뷰 응답을 분석하는 노드
#
#     이 노드는 LangChain의 응답 분석 체인을 활용하여 포커스 그룹 인터뷰에서 수집된 응답들을 분석합니다.
#     응답을 분석하여 주요 통찰과 패턴을 추출하고, 이를 Workflow의 다음 단계로 전달합니다.
#     """

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)  # BaseNode 초기화
#         # set_response_analysis_chain 함수를 통해 LangChain 체인을 가져와 설정
#         self.chain = set_response_analysis_chain()  # 응답 분석 체인 설정

#     def execute(self, state) -> dict:
#         """
#         주어진 상태(state)에서 인터뷰 응답을 추출하여 분석하고 결과를 반환합니다.
#
#         Args:
#             state (dict): Workflow의 현재 상태. responses, interview_topic, target_audience 정보를 포함함.
#
#         Returns:
#             dict: 분석된 결과를 포함한 상태 업데이트
#         """
#         # 응답 분석 체인 실행 - LLM을 통해 응답 분석
#         analysis_result = self.chain.invoke(
#             {
#                 "responses": state["responses"],  # 인터뷰 응답
#                 "interview_topic": state["interview_topic"],  # 인터뷰 주제
#                 "target_audience": state["target_audience"],  # 대상 청중
#             }
#         )

#         # 분석 결과를 새로운 상태 업데이트로 반환
#         return {"responses": analysis_result}
