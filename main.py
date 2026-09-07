import os 
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

response = completion(
    model="gemini/gemini-2.5-flash",
    messages=[
        {
            "role":"user",
            "content":"write a 2 sentace mindset to become million simple action but huge result"
        }
    ],
    api_key=os.getenv("GOOGLE_API_KEY")
)

print(response.choices[0].message.content)