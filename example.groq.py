from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()

chat_completions = (
    client.chat
    .completions.create(
        messages=[
            {"role": "user", "content": "Explain me what is Groq"}
        ],
        model="llama-3.3-70b-versatile",
    )
)

print(chat_completions.choices[0].message.content)
# Groq is a start-up company that specializes in the development of
# application-specific integrated circuits (ASICs) and software for artificial
# intelligence (AI) and machine learning (ML) workloads. The company is focused
# on creating custom-designed chips that can efficiently run AI and ML models,
# with the goal of improving performance, reducing power consumption, and
# lowering costs.
#
# Groq was founded in 2016 by Jonathan Ross, who previously worked at Google on
# the company's Tensor Processing Unit (TPU) project. The company is
# headquartered in Mountain View, California, and has received funding from
# investors such as GV (formerly Google Ventures), Intel Capital, and TPG Growth.
#
# Groq's products and technologies are designed to support a wide range of AI and
# ML applications, including computer vision, natural language processing, and
# recommender systems. The company's ASICs are optimized for specific AI and ML
# workloads, allowing them to achieve higher performance and lower power
# consumption compared to general-purpose CPUs and GPUs.
