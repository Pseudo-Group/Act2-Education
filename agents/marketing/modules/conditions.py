"""조건부 라우팅 함수 모듈

이 모듈은 LangGraph의 조건부 에지에서 사용할 라우팅 함수들을 포함합니다.
각 함수는 상태를 입력으로 받아 다음에 실행할 노드를 결정합니다.
"""

# 예시 라우팅 함수들입니다. 참고용으로 남겨둡니다.

# from typing import Literal
# from agents.marketing.modules.state import MarketingState


# def should_create_content(state: MarketingState) -> Literal["create_content", "end"]:
#     """
#     콘텐츠 생성 여부를 결정하는 라우팅 함수
#
#     이 함수는 상태에서 messages의 길이를 확인하여
#     캠페인 전략이 생성되었는지 판단합니다.
#
#     Args:
#         state (MarketingState): 현재 워크플로우 상태
#
#     Returns:
#         Literal["create_content", "end"]: 다음 실행할 노드 이름
#     """
#     # 메시지가 있는지 확인 (캠페인 전략이 생성되었는지)
#     if "messages" in state and len(state["messages"]) > 0:
#         # 메시지가 있으면 콘텐츠 생성 노드로 라우팅
#         return "create_content"
#     else:
#         # 메시지가 없으면 종료 노드로 라우팅
#         return "end"
#
#
# def need_campaign_strategy(state: MarketingState) -> Literal["generate_campaign", "create_content"]:
#     """
#     캠페인 전략 생성 필요 여부를 결정하는 라우팅 함수
#
#     이 함수는 상태에서 messages의 존재 여부와 길이를 확인하여
#     캠페인 전략 생성이 필요한지 판단합니다.
#
#     Args:
#         state (MarketingState): 현재 워크플로우 상태
#
#     Returns:
#         Literal["generate_campaign", "create_content"]: 다음 실행할 노드 이름
#     """
#     # 메시지가 있는지 확인 (캠페인 전략이 이미 생성되었는지)
#     if "messages" not in state or len(state["messages"]) == 0:
#         # 메시지가 없으면 캠페인 생성 노드로 라우팅
#         return "generate_campaign"
#     else:
#         # 메시지가 있으면 콘텐츠 생성 노드로 라우팅
#         return "create_content"
