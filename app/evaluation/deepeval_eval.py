from deepeval.test_case import LLMTestCase

from deepeval.metrics import AnswerRelevancyMetric

from deepeval.models import OllamaModel


ollama_model = OllamaModel(

    model="phi3"
)


test_case = LLMTestCase(

    input="Patient has type 2 diabetes",

    actual_output="E11.9 - Type 2 diabetes mellitus without complications"
)


metric = AnswerRelevancyMetric(

    threshold=0.7,

    model=ollama_model
)


metric.measure(test_case)


print("Score:", metric.score)

print("Reason:")
print(metric.reason)