import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
def gerar_documento_hipotetico(query_usuario):
    prompt = f"""
    Gere uma resposta técnica detalhada sobre:
    {query_usuario}
    """

    response = client.models.generate_content(
    model = "gemini-3-flash-preview", contents = prompt
    )
    
    return response.text
