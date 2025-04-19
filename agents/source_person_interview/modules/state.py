from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated, List, TypedDict

from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph.message import add_messages


@dataclass
class SourcePersonInterviewState(TypedDict):
    """
    Source Person Interview Workflow의 상태를 정의하는 TypedDict 클래스

    교육 콘텐츠 제작을 위한 Source Person Interview Workflow에서 사용되는 상태 정보를 정의합니다.
    LangGraph의 상태 관리를 위한 클래스로, Workflow 내에서 처리되는 데이터의 형태와 구조를 지정합니다.

    아래는 예시 상태 변수들입니다. 실제 구현 시 필요에 따라 수정해서 사용해주세요!
    """

    interview_topic: str  # 인터뷰 주제 (예: "교육 방법론", "학습 경험")
    source_person: str  # 인터뷰 대상자 정보 (예: "교육학 교수", "교육 기관 대표")
    expertise_area: str  # 전문 분야 (예: "이러닝", "교육 심리학")
    questions: List[str]  # 인터뷰 질문 목록
    responses: Annotated[
        List[HumanMessage | AIMessage], add_messages
    ]  # 응답 메시지 목록
    # Annotated는 Python 타입 어노테이션으로, add_messages는 LangGraph에서 사용하는 특별한 함수입니다.
    # add_messages는 메시지 목록에 새로운 메시지를 추가할 때 이전 메시지를 유지하면서 추가하는 기능을 자동으로 처리합니다.
    insights: List[str]  # 인터뷰에서 도출된 통찰
