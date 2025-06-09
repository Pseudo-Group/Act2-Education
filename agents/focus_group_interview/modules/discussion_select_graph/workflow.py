# structured_output : https://ai.google.dev/gemini-api/docs/structured-output?hl=ko

import enum
from pydantic import BaseModel
from google import genai

client = genai.Client(api_key = "")

class Graphs(enum.Enum):
    BASE_GRAPH = "base_graph",
    STEP_GRAPH = "step_graph",
    FREE_GRAPH = "free_graph",
    ROUND_ROBIN_GRPAH = "round_robin_graph"

class Graph_Type(BaseModel):
    graph: Graphs


def get_graph(input_text):

    response = client.models.generative_content(
        model = "",
        contents = "입력을 보고 적합한 graph type을 정해주세요 <추후에 프롬프트로 따로 관리 예정>",
        config = {
            "response_mime_type" : "application/json",
            "response_schema" : Graph_Type
        }
    )  

    return response