import os 
from dotenv import load_dotenv
from litellm import completion

load_dotenv()
os.getenv("GOOGLE_API_KEY")
model = os.getenv("model","gemini/gemini-2.5-flash")
response = completion(
    model=model,
    messages=[
        {
            "role":"user",
            "content":"write a 2 sentace mindset to become million simple action but huge result"
        }
    ],
    api_key=os.getenv("GOOGLE_API_KEY")
)

print(response.choices[0].message.content)