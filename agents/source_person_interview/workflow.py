from agents.base_workflow import BaseWorkflow
from agents.source_person_interview.modules.state import SourcePersonInterviewState
from langgraph.graph import StateGraph


class SourcePersonInterviewWorkflow(BaseWorkflow):
    """
    Source Person Interview를 위한 Workflow 클래스

    이 클래스는 교육 콘텐츠 제작을 위한 Source Person Interview Workflow를 정의합니다.
    BaseWorkflow를 상속받아 기본 구조를 구현하고, SourcePersonInterviewState를 사용하여 상태를 관리합니다.
    """

    def __init__(self, state):
        super().__init__()
        self.state = state

    def build(self):
        """
        Source Person Interview Workflow 그래프 구축 메서드

        StateGraph를 사용하여 Source Person Interview를 위한 Workflow 그래프를 구축합니다.
        현재는 기본 구조만 포함하고 있으며, 추후 노드와 조건부 에지를 추가하여
        다양한 경로를 가진 Workflow를 구축할 수 있습니다.

        Returns:
            CompiledStateGraph: 컴파일된 상태 그래프 객체
        """
        builder = StateGraph(self.state)
        
        # 노드 추가 예시
        # builder.add_node("prepare_questions", QuestionPreparationNode())
        # builder.add_node("extract_insights", InsightExtractionNode())
        
        # 에지 추가 예시 - 아래 코드는 참고용이며 실제 구현 시 주석을 해제하고 사용할 수 있습니다
        # 1. 단순 에지: 시작 노드에서 need_questions 함수로 연결
        # builder.add_edge("__start__", need_questions)
        #
        # 2. 조건부 에지: need_questions 함수의 반환값에 따라 다른 노드로 분기
        # builder.add_conditional_edges(
        #     "__start__",                # 시작 노드
        #     need_questions,             # 라우팅 함수 - 어떤 노드로 갈지 결정
        #     {                           # 라우팅 함수 반환값에 따른 목적지 노드
        #         "prepare_questions": "prepare_questions",    # 질문 준비 필요 시
        #         "collect_responses": "collect_responses"     # 응답 수집 필요 시
        #     }
        # )

        # 기본 에지 설정 (임시)
        builder.add_edge("__start__", "__end__")

        workflow = builder.compile()  # 그래프 컴파일
        workflow.name = self.name  # Workflow 이름 설정

        return workflow


# Source Person Interview Workflow 인스턴스 생성
source_person_interview_workflow = SourcePersonInterviewWorkflow(SourcePersonInterviewState)