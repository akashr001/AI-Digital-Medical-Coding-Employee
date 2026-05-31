import os

os.environ["RAGAS_TIMEOUT"] = "300"

from datasets import Dataset

from ragas import evaluate

from ragas.metrics import AnswerRelevancy

from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings


llm = ChatOllama(

    model="phi3"
)

embeddings = OllamaEmbeddings(

    model="phi3"
)


data = {

    "question": [

        "Patient has type 2 diabetes"
    ],

    "answer": [

        "E11.9 diabetes"
    ],

    "contexts": [[

        "E11.9 diabetes"
    ]],

    "ground_truth": [

        "E11.9"
    ]
}


dataset = Dataset.from_dict(data)


result = evaluate(

    dataset,

    metrics=[

        AnswerRelevancy()
    ],

    llm=llm,

    embeddings=embeddings
)

print(result)