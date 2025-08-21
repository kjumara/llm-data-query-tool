"""
Utility Script to verify that the OpenAI API key is:

1. Correctly Configured
2. Accessible from the local environment

Output:
    - If API key is valid, prints a success message and the model's response
    - If API key is not valid or misconfigured, prints an error message for troubleshooting

Notes:
    - This script is intended as a developer sanity check during initial setup
    - It is not required for the main application, but may be helpful for debugging in the event of authentication issues.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    # Simple test request
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # lightweight, cheap test model
        messages=[{"role": "user", "content": "Say hello!"}],
        max_tokens=20
    )

    print("✅ API Key works!")
    print("Response:", response.choices[0].message.content.strip())

except Exception as e:
    print("❌ Something went wrong.")
    print("Error:", str(e))
