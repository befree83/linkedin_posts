import sys
from dotenv import load_dotenv
from core.chatbot import Chatbot

def main():
    # Load environment variables
    load_dotenv()
    
    print("🚀 Bienvenido al Generador de Posts para LinkedIn")
    print("Escribe 'salir' o 'exit' en cualquier momento para cerrar la aplicación.\n")
    
    bot = Chatbot()
    
    while True:
        try:
            user_input = input("💡 Introduce tu idea para el post de LinkedIn:\n> ").strip()
            
            # Supporting both Spanish and English exit commands
            if user_input.lower() in ['exit', 'quit', 'salir']:
                print("\n👋 Cerrando el generador. ¡Hasta pronto!")
                sys.exit(0)
                
            if not user_input:
                print("⚠️ Por favor, introduce una idea válida.\n")
                continue
                
            bot.process_idea(user_input)
            
        except KeyboardInterrupt:
            print("\n\n👋 Cerrando el generador. ¡Hasta pronto!")
            sys.exit(0)

if __name__ == "__main__":
    main()