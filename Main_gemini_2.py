import os
import time
from google import genai
from google.genai import types

# Keep your same API Key
API_KEY = "Give your API Key here"

class CyberSecurityAgent:
    def __init__(self):
        try:
            self.client = genai.Client(api_key=API_KEY)
            
            # CHANGED: We are now using the "Pro" model
            # Use "gemini-2.5-pro" for complex reasoning
            # Use "gemini-2.5-flash" if you want it to be super fast
            self.model_id = "gemini-3-flash-preview"
            
            self.system_instruction = (
                "You are a specialized Cyber Security AI Assistant. "
                "Explain security concepts, defensive strategies, and ethical practices. "
                "Focus on protecting systems and defending against threats."
            )
            print(f"[+] Agent initialized with model: {self.model_id}")
        except Exception as e:
            print(f"[-] Initialization Error: {e}")
            exit()

    def start_chat(self):
        print("\n" + "="*40)
        print("   CYBER SECURITY AI PRO ACTIVE")
        print("="*40)
        
        chat = self.client.chats.create(
            model=self.model_id,
            config=types.GenerateContentConfig(
                system_instruction=self.system_instruction,
                temperature=0.7,
            )
        )

        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']: break
            
            # We use a loop here to 'retry' if we hit a rate limit
            success = False
            while not success:
                try:
                    response = chat.send_message(user_input)
                    print(f"\nAgent: {response.text}\n")
                    success = True # Stop the retry loop
                except Exception as e:
                    if "429" in str(e):
                        print("\n[!] Rate limit reached. Waiting 10 seconds to retry...")
                        time.sleep(10)
                    else:
                        print(f"\n[!] Error: {e}")
                        break # Stop if it's a different kind of error

if __name__ == "__main__":
    agent = CyberSecurityAgent()
    agent.start_chat()