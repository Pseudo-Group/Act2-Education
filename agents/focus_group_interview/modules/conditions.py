"""조건부 라우팅 함수 모듈

이 모듈은 LangGraph의 조건부 에지에서 사용할 라우팅 함수들을 포함합니다.
각 함수는 상태를 입력으로 받아 다음에 실행할 노드를 결정합니다.
"""

# from typing import Literal
# from agents.focus_group_interview.modules.state import FocusGroupInterviewState


# def should_analyze_responses(state: FocusGroupInterviewState) -> Literal["analyze", "end"]:
#     """
#     응답을 분석할지 여부를 결정하는 라우팅 함수
#
#     이 함수는 상태에서 responses의 길이를 확인하여
#     충분한 응답이 수집되었는지 판단합니다.
#
#     Args:
#         state (FocusGroupInterviewState): 현재 워크플로우 상태
#
#     Returns:
#         Literal["analyze", "end"]: 다음 실행할 노드 이름
#     """
#     # 응답이 있는지 확인
#     if "responses" in state and len(state["responses"]) > 0:
#         # 응답이 있으면 분석 노드로 라우팅
#         return "analyze"
#     else:
#         # 응답이 없으면 종료 노드로 라우팅
#         return "end"


# def need_more_questions(state: FocusGroupInterviewState) -> Literal["generate_questions", "collect_responses"]:
#     """
#     추가 질문이 필요한지 여부를 결정하는 라우팅 함수
#
#     이 함수는 상태에서 questions의 존재 여부와 길이를 확인하여
#     질문 생성이 필요한지 판단합니다.
#
#     Args:
#         state (FocusGroupInterviewState): 현재 워크플로우 상태
#
#     Returns:
#         Literal["generate_questions", "collect_responses"]: 다음 실행할 노드 이름
#     """
#     # 질문이 있는지 확인
#     if "questions" not in state or not state["questions"] or len(state["questions"]) == 0:
#         # 질문이 없으면 질문 생성 노드로 라우팅
#         return "generate_questions"
#     else:
#         # 질문이 있으면 응답 수집 노드로 라우팅
#         return "collect_responses"
