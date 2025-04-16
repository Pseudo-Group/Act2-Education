"""
유틸리티 및 보조 함수 모듈

이 모듈은 Source Person Interview Workflow에서 사용할 수 있는 다양한 유틸리티 함수를 제공합니다.
인터뷰 데이터 처리, 통찰 추출, 보고서 생성 등에 필요한 유틸리티 함수들을 포함합니다.

아래는 예시 코드입니다. 참고용으로 남겨둡니다.
"""

# from typing import List, Dict, Any
# from langchain_core.messages import BaseMessage
# import re
# import json
# from datetime import datetime


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


# def clean_transcript(transcript: str) -> str:
#     """
#     인터뷰 녹취록을 정리합니다.
#     
#     이 함수는 녹취록에서 불필요한 요소(반복, 말더듬, 채움말 등)를 
#     제거하고 텍스트를 정리합니다.
#     
#     Args:
#         transcript: 원본 인터뷰 녹취록
#         
#     Returns:
#         정리된 녹취록
#     """
#     # 채움말 제거 (예: 음, 그, 저, 어, 그래서 등)
#     cleaned = re.sub(r'\b(음|그|저|어|그래서|그러니까|뭐랄까|뭐지)\b', '', transcript)
#     
#     # 반복 제거
#     cleaned = re.sub(r'(\b\w+\b)(\s+\1\b)+', r'\1', cleaned)
#     
#     # 여러 공백을 하나로 통합
#     cleaned = re.sub(r'\s+', ' ', cleaned)
#     
#     return cleaned.strip()


# def segment_by_speaker(transcript: str, speakers: List[str]) -> List[Dict[str, str]]:
#     """
#     녹취록을 화자별로 분할합니다.
#     
#     Args:
#         transcript: 인터뷰 녹취록
#         speakers: 화자 목록
#         
#     Returns:
#         화자별로 분할된 녹취록 세그먼트 목록
#     """
#     segments = []
#     
#     # 실제 구현에서는 더 정교한 화자 분할 알고리즘 사용
#     # 예시 구현 (간단한 패턴 매칭)
#     for speaker in speakers:
#         pattern = rf'{speaker}:\s*(.*?)(?=\b(?:{"|".join(speakers)}):|$)'
#         matches = re.findall(pattern, transcript, re.DOTALL)
#         
#         for match in matches:
#             segments.append({
#                 "speaker": speaker,
#                 "text": match.strip()
#             })
#     
#     # 세그먼트를 원래 순서대로 정렬 (실제 구현에서는 타임스탬프 사용)
#     # 여기서는 간단한 예시만 제공
#     
#     return segments


# def extract_quotes(transcript: str, min_length: int = 20, max_length: int = 200) -> List[str]:
#     """
#     인터뷰 녹취록에서 인용할 만한 문장을 추출합니다.
#     
#     Args:
#         transcript: 인터뷰 녹취록
#         min_length: 최소 문장 길이
#         max_length: 최대 문장 길이
#         
#     Returns:
#         추출된 인용구 목록
#     """
#     # 문장 분할
#     sentences = re.split(r'(?<=[.!?])\s+', transcript)
#     
#     # 길이 조건에 맞는 문장 필터링
#     quotes = [s for s in sentences if min_length <= len(s) <= max_length]
#     
#     # 실제 구현에서는 더 정교한 필터링 (중요도, 관련성 등) 적용
#     
#     return quotes


# def format_interview_insights(
#     insights: List[str],
#     key_concepts: Dict[str, str],
#     quotes: List[str],
#     source_person: str,
#     expertise_area: str
# ) -> str:
#     """
#     인터뷰 통찰을 보고서 형식으로 포맷팅합니다.
#     
#     Args:
#         insights: 주요 통찰 목록
#         key_concepts: 핵심 개념 사전
#         quotes: 주요 인용구 목록
#         source_person: 인터뷰 대상자 정보
#         expertise_area: 전문 분야
#         
#     Returns:
#         포맷팅된 보고서 문자열
#     """
#     report = f"# {source_person} 인터뷰 통찰 보고서\n\n"
#     report += f"전문 분야: {expertise_area}\n"
#     report += f"날짜: {datetime.now().strftime('%Y-%m-%d')}\n\n"
#     
#     report += "## 주요 통찰\n"
#     for i, insight in enumerate(insights, 1):
#         report += f"{i}. {insight}\n"
#     
#     report += "\n## 핵심 개념\n"
#     for concept, description in key_concepts.items():
#         report += f"**{concept}**: {description}\n\n"
#     
#     report += "## 주요 인용구\n"
#     for quote in quotes:
#         report += f"> {quote}\n\n"
#     
#     report += "## 교육적 적용\n"
#     report += "이 인터뷰에서 얻은 통찰은 다음과 같은 교육적 맥락에서 적용할 수 있습니다:\n\n"
#     # 실제 구현에서는 LLM을 사용하여 교육적 적용 사항 생성
#     
#     return report
