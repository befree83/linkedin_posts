from pydantic import ValidationError
from openai import OpenAIError
from core.api_client import OpenAIClient
from models.linkedin_post import LinkedinPost

class Chatbot:
    def __init__(self):
        try:
            self.api_client = OpenAIClient()
        except ValueError as e:
            print(f"\n[Error de Configuración] {e}")
            exit(1)

    def process_idea(self, user_input: str) -> None:
        """
        Processes the user input, calls the API, and handles potential errors gracefully in Spanish.
        """
        print("\n⏳ Generando tu post de LinkedIn... Por favor, espera.")
        try:
            post: LinkedinPost = self.api_client.generate_structured_post(user_input)
            self._display_post(post)
            
        except ValidationError as val_err:
            print(f"\n❌ [Error de Validación / Rechazo de API]: La respuesta no coincide con el formato esperado o el contenido fue bloqueado por seguridad.\nDetalles: {val_err}")
        except OpenAIError as api_err:
            print(f"\n❌ [Error de API]: Falló la comunicación con los servidores de OpenAI.\nDetalles: {api_err}")
        except Exception as e:
            print(f"\n❌ [Error Inesperado]: Ocurrió un fallo desconocido.\nDetalles: {e}")

    def _display_post(self, post: LinkedinPost) -> None:
        """Displays the validated Pydantic model in a clear, readable format."""
        print("\n" + "="*50)
        print(f"📌 TÍTULO: {post.title}")
        print("-" * 50)
        print(f"📝 CONTENIDO:\n{post.content}")
        print("-" * 50)
        
        # Formatting hashtags with '#'
        formatted_hashtags = " ".join([f"#{tag}" for tag in post.hashtags])
        print(f"🏷️  HASHTAGS: {formatted_hashtags}")
        print(f"📂 CATEGORÍA: {post.category}")
        print("="*50 + "\n")