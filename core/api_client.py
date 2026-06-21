import os
from openai import OpenAI
from models.linkedin_post import LinkedinPost

class OpenAIClient:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("La variable de entorno OPENAI_API_KEY no está configurada.")
        self.client = OpenAI(api_key=self.api_key)

    def generate_structured_post(self, user_prompt: str) -> LinkedinPost:
        """
        Llama a la API usando la nueva Responses API con Structured Outputs 
        para generar un post de LinkedIn validado en castellano.
        """
        system_prompt = (
            "Eres un experto redactor (copywriter) para LinkedIn. "
            "Convierte la idea del usuario en un post de LinkedIn altamente atractivo y profesional. "
            "El contenido generado debe estar redactado íntegramente en castellano. "
            "Asegúrate de que la salida cumpla estrictamente con el esquema JSON requerido."
        )

        response = self.client.responses.parse(
            model="gpt-4o-2024-08-06",
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            text_format=LinkedinPost
        )

        if not response.output_parsed:
            raise RuntimeError("Error interno: No se pudo parsear la salida estructurada de OpenAI.")

        return response.output_parsed