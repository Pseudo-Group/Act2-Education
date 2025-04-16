# 마케팅 모듈 (Marketing Module)

## 개요

이 모듈은 Pseudo Education Company의 교육 콘텐츠 마케팅 전략 수립 및 콘텐츠 생성을 담당하는 LangGraph Workflow입니다. 교육 제품/서비스에 대한 효과적인 마케팅 캠페인 전략과 다양한 채널에 맞는 콘텐츠를 생성하는 기능을 제공합니다.

## 주요 노드

<!-- 노드에 대한 설명을 추가해주세요. -->

## 구조

```
marketing/
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
└── workflow.py        # 마케팅 Workflow 정의
```

## 사용 방법

마케팅 Workflow는 다음과 같이 사용할 수 있습니다:

```python
from agents.marketing.workflow import marketing_workflow

# 초기 상태 설정
initial_state = {
    "target_audience": "고등학생",                     # 대상 청중
    "product_name": "AI 학습 플랫폼",                  # 제품/서비스 이름
    "product_description": "AI 기반 맞춤형 학습 시스템",  # 제품/서비스 설명
    "marketing_channels": ["소셜 미디어", "이메일"],     # 마케팅 채널
    "campaign_goals": ["인지도 향상", "사용자 확보"],    # 캠페인 목표
    "messages": []                                  # 메시지 (빈 리스트로 초기화)
}

# Workflow 실행
result = marketing_workflow().invoke(initial_state)
```

## 확장 방법

이 모듈은 확장성을 고려하여 설계되었습니다. 새로운 기능을 추가하려면:

1. `modules/nodes.py`에 새로운 노드 클래스 추가
2. `modules/chains.py`에 필요한 LangChain 체인 정의
3. `workflow.py`에서 새 노드를 Workflow에 연결