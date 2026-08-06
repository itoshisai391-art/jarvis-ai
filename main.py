import sys
import time
import os

try:
    import google.generativeai as genai
except ImportError:
    print("Installing google-generativeai...")
    os.system("pip install google-generativeai")
    import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY", "AQ.Ab8RN6IgQ1p1zBDnu8ZBHsC3ZlrwmR4DbPG12_BCy7aQXC2wtQ")
genai.configure(api_key=API_KEY)

def initialize_jarvis():
    print("--------------------------------------------------")
    print("       JARVIS AI ASSISTANT INITIALIZED            ")
    print("--------------------------------------------------")
    print("Type your prompt or use safety commands: 'stop', 'exit'")
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    chat = model.start_chat(history=[])
    
    while True:
        try:
            user_input = input("\nJarvis > ").strip()
            
            if user_input.lower() in ["stop", "exit", "shutdown", "quit"]:
                print("Shutting down Jarvis. Goodbye!")
                break
                
            if not user_input:
                continue
                
            response = chat.send_message(user_input)
            print(f"\nJarvis: {response.text}")
            
        except KeyboardInterrupt:
            print("\nJarvis session interrupted. Shutting down safely.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    initialize_jarvis()
