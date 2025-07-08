# 포커스 그룹 인터뷰 모듈 (Focus Group Interview Module)

## 개요

이 모듈은 Act2: Marketing의 포커스 그룹 인터뷰 진행 및 분석을 담당하는 LangGraph Workflow입니다. 교육 콘텐츠 개발을 위한 인터뷰 질문 생성, 응답 분석, 통찰 추출 기능을 제공합니다.

## 주요 노드

<!-- 노드에 대한 설명을 추가해주세요. -->

## 구조

```
focus_group_interview/
├── modules/            # 모듈 구성 요소
│   ├── chains.py      # LangChain 체인 정의
│   ├── conditions.py  # 조건부 라우팅 함수
│   ├── models.py      # 사용하는 LLM 모델 설정
│   ├── nodes.py       # Workflow 노드 클래스들 정의
│   ├── prompts.py     # 프롬프트 템플릿(필요에 따라 변경 가능)
│   ├── state.py       # 상태 정의
│   ├── tools.py       # 도구 함수
│   └── utils.py       # 유틸리티 함수
├── pyproject.toml     # 프로젝트 관리자
├── README.md          # 이 문서
└── workflow.py        # 포커스 그룹 인터뷰 Workflow 정의
```

## 사용 방법

포커스 그룹 인터뷰 Workflow는 다음과 같이 사용할 수 있습니다:

```python
from agents.focus_group_interview.workflow import focus_group_interview_workflow

# 초기 상태 설정
initial_state = {
    "interview_topic": "교육 콘텐츠 개선",  # 인터뷰 주제
    "target_audience": "고등학생",         # 대상 청중
    "questions": [],                     # 질문 목록 (빈 리스트로 초기화)
    "responses": []                      # 응답 메시지 (빈 리스트로 초기화)
}

# Workflow 실행
result = focus_group_interview_workflow().invoke(initial_state)
```

## 확장 방법

이 모듈은 확장성을 고려하여 설계되었습니다. 새로운 기능을 추가하려면:

1. `modules/nodes.py`에 새로운 노드 클래스 추가
2. `modules/chains.py`에 필요한 LangChain 체인 정의
3. `workflow.py`에서 새 노드를 Workflow에 연결
