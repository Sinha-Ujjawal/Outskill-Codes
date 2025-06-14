from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="What is Gemini",
)

print(response.text)

# Gemini refers to a few different things, but most commonly it refers to:
#
# *   **Google Gemini:** This is a family of large language models (LLMs)
# developed by Google AI. It's designed to be multimodal, meaning it can
# understand and generate text, code, images, audio, and video. It's designed to
# be Google's most powerful and general-purpose AI model, intended to power many
# of their future AI-driven products.
#
# 	*   There are different versions of Gemini, including: *   **Gemini
# Ultra:** The most capable model, designed for complex tasks.  *   **Gemini
# Pro:** A balance of performance and speed, suitable for a wide range of tasks.
# *   **Gemini Nano:** Designed for on-device use (e.g., smartphones) where
# resources are limited.
#
# Besides the LLM, "Gemini" can also refer to:
#
# *   **The astrological sign Gemini:**  One of the twelve signs of the zodiac,
# associated with people born roughly between May 21 and June 20.  *   **The
# constellation Gemini:** A constellation in the northern sky, featuring the
# bright stars Castor and Pollux.  *   **Project Gemini:** An early crewed space
# program of NASA in the mid-1960s, bridging the gap between Project Mercury and
# Project Apollo.
#
# So, when you say "Gemini," it's important to understand the context to know
# which meaning is intended. In most current contexts, it's referring to the
# **Google AI model**.
