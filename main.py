import os 
from dotenv import load_dotenv
from litellm import completion

load_dotenv()
#model = os.getenv("model","gemini/gemini-2.5-flash")
model ="gemini/gemini-1.5-flash"

# models = [
#     "primary-model",
#     "backup-model"
# ]
response = completion(
    model=model,
    messages=[
        {
            "role":"user",
            "content":"write a 2 sentace mindset to become million simple action but huge result"
        }
    ],
    api_key=os.getenv("GOOGLE_API_KEY"),
    #add fall back 4.
    fallbacks=["gemini/gemini-2.5-flash-lite"]

)

print("Requested model: gemini")
print("Actual model:", response.model)
print("Answer:", response.choices[0].message.content)