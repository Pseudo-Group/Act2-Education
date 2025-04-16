"""조건부 라우팅 함수 모듈

이 모듈은 LangGraph의 조건부 에지에서 사용할 라우팅 함수들을 포함합니다.
각 함수는 상태를 입력으로 받아 다음에 실행할 노드를 결정합니다.
"""

# from typing import Literal
# from agents.source_person_interview.modules.state import SourcePersonInterviewState

# 주석 처리된 예시 라우팅 함수들입니다. 필요에 따라 주석을 해제하고 구현하세요.

# def should_extract_insights(state: SourcePersonInterviewState) -> Literal["extract_insights", "end"]:
#     """
#     통찰 추출 여부를 결정하는 라우팅 함수
#
#     이 함수는 상태에서 responses의 길이를 확인하여
#     충분한 응답이 수집되었는지 판단합니다.
#
#     Args:
#         state (SourcePersonInterviewState): 현재 워크플로우 상태
#
#     Returns:
#         Literal["extract_insights", "end"]: 다음 실행할 노드 이름
#     """
#     # 응답이 있는지 확인
#     if "responses" in state and len(state["responses"]) > 0:
#         # 응답이 있으면 통찰 추출 노드로 라우팅
#         return "extract_insights"
#     else:
#         # 응답이 없으면 종료 노드로 라우팅
#         return "end"
#
#
# def need_questions(state: SourcePersonInterviewState) -> Literal["prepare_questions", "collect_responses"]:
#     """
#     질문 준비 필요 여부를 결정하는 라우팅 함수
#
#     이 함수는 상태에서 questions의 존재 여부와 길이를 확인하여
#     질문 준비가 필요한지 판단합니다.
#
#     Args:
#         state (SourcePersonInterviewState): 현재 워크플로우 상태
#
#     Returns:
#         Literal["prepare_questions", "collect_responses"]: 다음 실행할 노드 이름
#     """
#     # 질문이 있는지 확인
#     if "questions" not in state or not state["questions"] or len(state["questions"]) == 0:
#         # 질문이 없으면 질문 준비 노드로 라우팅
#         return "prepare_questions"
#     else:
#         # 질문이 있으면 응답 수집 노드로 라우팅
#         return "collect_responses"
