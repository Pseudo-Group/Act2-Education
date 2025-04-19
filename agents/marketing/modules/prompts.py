"""프롬프트 템플릿 모듈

이 모듈은 LangChain 프롬프트 템플릿을 정의하고 반환하는 함수들을 포함합니다.
각 함수는 특정 작업에 맞는 프롬프트 템플릿을 생성합니다.
"""

# from langchain_core.prompts import PromptTemplate

# 예시 함수들입니다. 참고용으로 남겨둡니다.

# def get_campaign_generation_prompt() -> PromptTemplate:
#     """
#     교육 마케팅 캠페인 생성을 위한 프롬프트 템플릿을 반환합니다.
#
#     이 프롬프트는 대상 청중, 제품 정보, 마케팅 채널, 캠페인 목표를 입력으로 받아
#     효과적인 교육 마케팅 캠페인을 생성하도록 설계되었습니다.
#
#     Returns:
#         PromptTemplate: 캠페인 생성을 위한 프롬프트 템플릿
#     """
#     template = """
#     당신은 교육 분야의 마케팅 전략 전문가입니다.
#     아래 정보를 바탕으로 효과적인 교육 마케팅 캠페인을 개발해주세요.
#
#     # 대상 청중
#     {target_audience}
#
#     # 제품/서비스 정보
#     이름: {product_name}
#     설명: {product_description}
#
#     # 마케팅 채널
#     {marketing_channels}
#
#     # 캠페인 목표
#     {campaign_goals}
#
#     # 지침
#     - 교육적 가치와 학습 효과를 강조하는 캠페인을 개발하세요.
#     - 대상 청중의 요구와 관심사에 맞춘 전략을 구성하세요.
#     - 지정된 마케팅 채널에 적합한 접근 방식을 제안하세요.
#     - 캠페인 목표를 달성하기 위한 구체적인 전략을 포함하세요.
#     - 교육 분야의 최신 트렌드를 고려하세요.
#
#     다음 JSON 형식으로 캠페인 정보를 반환해주세요:
#     ```json
#     {
#       "campaign_name": "캠페인 이름",
#       "campaign_strategy": "캠페인 전략 개요",
#       "key_messages": ["핵심 메시지 1", "핵심 메시지 2", ...],
#       "timeline": "캠페인 타임라인",
#       "success_metrics": ["성공 지표 1", "성공 지표 2", ...]
#     }
#     ```
#     """
#     return PromptTemplate.from_template(template)
#
#
# def get_content_creation_prompt() -> PromptTemplate:
#     """
#     마케팅 콘텐츠 생성을 위한 프롬프트 템플릿을 반환합니다.
#
#     이 프롬프트는 대상 청중, 제품 정보, 마케팅 채널, 캠페인 전략을 입력으로 받아
#     효과적인 마케팅 콘텐츠를 생성하도록 설계되었습니다.
#
#     Returns:
#         PromptTemplate: 콘텐츠 생성을 위한 프롬프트 템플릿
#     """
#     template = """
#     당신은 교육 분야의 마케팅 콘텐츠 전문가입니다.
#     아래 정보를 바탕으로 효과적인 마케팅 콘텐츠를 생성해주세요.
#
#     # 대상 청중
#     {target_audience}
#
#     # 제품/서비스 정보
#     이름: {product_name}
#     설명: {product_description}
#
#     # 마케팅 채널
#     {marketing_channels}
#
#     # 캠페인 전략
#     {messages}
#
#     # 지침
#     - 각 마케팅 채널에 적합한 형식과 톤으로 콘텐츠를 작성하세요.
#     - 교육적 가치와 학습 효과를 강조하는 메시지를 포함하세요.
#     - 대상 청중의 요구와 관심사에 맞춘 콘텐츠를 개발하세요.
#     - 행동 유도(Call to Action)를 명확하게 포함하세요.
#     - 교육 분야의 전문성을 보여주는 언어와 표현을 사용하세요.
#
#     다음 구조로 각 마케팅 채널별 콘텐츠를 작성해주세요:
#
#     ## [채널 이름] 콘텐츠
#     (해당 채널에 적합한 콘텐츠)
#
#     ## [채널 이름] 콘텐츠
#     (해당 채널에 적합한 콘텐츠)
#
#     ...
#     """
#     return PromptTemplate.from_template(template)
