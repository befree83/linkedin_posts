from pydantic import BaseModel, Field

class LinkedinPost(BaseModel):
    """Pydantic model representing a structured LinkedIn post."""
    title: str = Field(..., description="Un título atractivo para el post de LinkedIn en castellano.")
    content: str = Field(..., description="El cuerpo principal del post, formateado profesionalmente en castellano.")
    hashtags: list[str] = Field(..., description="Una lista de hashtags relevantes sin el símbolo '#'.")
    category: str = Field(..., description="La categoría profesional o industria a la que pertenece el post.")