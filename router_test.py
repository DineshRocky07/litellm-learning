import os
from dotenv import load_dotenv

load_dotenv()

from litellm import Router, completion

router = Router(
    model_list=[
    {
        "model_name":"gemini",
        "litellm_params": {
            "model": "gemini/gemini-2.5-flash",
            "api_key": os.getenv("GOOGLE_API_KEY")
        }
    },
    {
            "model_name":"gemini",
            "litellm_params": {
                "model": "gemini/gemini-2.5-flash-lite",
                "api_key": os.getenv("GOOGLE_API_KEY")
            }
        }
    ]
)

response = router.completion(
    model="gemini",
    messages=[
        {
            "role":"user",
            "content": "write a pickup line to impress a girl"
        }
    ]
)

print(response.choices[0].message.content)