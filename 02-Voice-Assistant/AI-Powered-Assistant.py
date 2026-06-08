from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

command = input("Enter command: ")

labels = [
    "open website",
    "search google",
    "open application"
]

result = classifier(
    command,
    labels
)

print(result["labels"][0])