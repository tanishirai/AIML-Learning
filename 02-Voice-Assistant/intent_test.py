from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

command = input("Enter command: ")

labels = [
    "open application",
    "open website",
    "search google",
    "tell current time"
]

result = classifier(
    command,
    labels
)

print("\nPredicted Intent:")
print(result["labels"][0])