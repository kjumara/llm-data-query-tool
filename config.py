"""
Utility Script to
1. Provide centralized configuration for managing environment variables.
2. Ensure sensitive credentials (like API keys) are never hard-coded into the codebase or pushed to git
"""

import os
from dotenv import load_dotenv

#load variables from .env file
load_dotenv()

#access key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API_KEY environment variable is not set")