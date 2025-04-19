"""
유틸리티 및 보조 함수 모듈

이 모듈은 포커스 그룹 인터뷰 Workflow에서 사용할 수 있는 다양한 유틸리티 함수를 제공합니다.
포커스 그룹 인터뷰 데이터 처리, 결과 분석, 보고서 생성 등에 필요한 유틸리티 함수들을 포함합니다.

아래는 예시 코드입니다. 참고용으로 남겨둡니다.
"""

# from typing import List, Dict, Any
# from langchain_core.messages import BaseMessage
# import re
# import json


# def get_message_text(msg: BaseMessage) -> str:
#     """메시지의 텍스트 내용을 가져옵니다."""
#     content = msg.content
#     if isinstance(content, str):
#         return content
#     elif isinstance(content, dict):
#         return content.get("text", "")
#     else:
#         txts = [c if isinstance(c, str) else (c.get("text") or "") for c in content]
#         return "".join(txts).strip()


# def extract_themes_from_responses(responses: List[str]) -> List[str]:
#     """
#     인터뷰 응답에서 주요 테마를 추출합니다.
#
#     이 함수는 간단한 키워드 빈도 분석을 사용하여 응답에서
#     반복적으로 언급되는 주요 테마를 식별합니다.
#
#     Args:
#         responses: 인터뷰 응답 목록
#
#     Returns:
#         추출된 주요 테마 목록
#     """
#     # 실제 구현에서는 더 정교한 NLP 기법을 사용할 수 있음
#     # 예시 구현
#     all_text = " ".join(responses).lower()
#
#     # 불용어 제거 및 단어 빈도 계산 로직
#     # ...
#
#     # 예시 결과
#     return ["학습 경험", "교육 콘텐츠 품질", "상호작용성"]


# def format_interview_report(
#     themes: List[str],
#     insights: List[str],
#     recommendations: List[str]
# ) -> str:
#     """
#     포커스 그룹 인터뷰 결과를 보고서 형식으로 포맷팅합니다.
#
#     Args:
#         themes: 식별된 주요 테마 목록
#         insights: 도출된 통찰 목록
#         recommendations: 권장사항 목록
#
#     Returns:
#         포맷팅된 보고서 문자열
#     """
#     report = "# 포커스 그룹 인터뷰 결과 보고서\n\n"
#
#     report += "## 주요 테마\n"
#     for i, theme in enumerate(themes, 1):
#         report += f"{i}. {theme}\n"
#
#     report += "\n## 주요 통찰\n"
#     for i, insight in enumerate(insights, 1):
#         report += f"{i}. {insight}\n"
#
#     report += "\n## 권장사항\n"
#     for i, recommendation in enumerate(recommendations, 1):
#         report += f"{i}. {recommendation}\n"
#
#     return report


# def parse_structured_response(response: str) -> Dict[str, Any]:
#     """
#     LLM의 구조화된 응답을 파싱합니다.
#
#     이 함수는 LLM이 생성한 텍스트에서 JSON 형식의 데이터를 추출합니다.
#
#     Args:
#         response: LLM의 응답 텍스트
#
#     Returns:
#         파싱된 구조화 데이터
#     """
#     # JSON 블록 찾기
#     json_match = re.search(r"```json\s*([\s\S]*?)\s*```", response)
#
#     if json_match:
#         try:
#             return json.loads(json_match.group(1))
#         except json.JSONDecodeError:
#             # JSON 파싱 실패 시 빈 딕셔너리 반환
#             return {}
#
#     # JSON 블록을 찾지 못한 경우 빈 딕셔너리 반환
#     return {}
