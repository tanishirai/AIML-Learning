from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)
from PIL import Image

# Load BLIP model
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Get image path from user
path = input("Enter image path: ")

# Open image
image = Image.open(path)

# Convert image for AI
inputs = processor(
    images=image,
    return_tensors="pt"
)

# Generate caption
output = model.generate(
    **inputs,
    max_new_tokens=30
)

# Decode caption
caption = processor.decode(
    output[0],
    skip_special_tokens=True
)

print("\nImage Caption:")
print(caption)

# Generate Instagram-style caption

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")            # It converts text into numbers.
text_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")   # Load Text Model

prompt = f"""
Image description: {caption}

Create a short Instagram caption.
Only use information from the image description.
Be creative but do not invent new objects or people.
"""

encoded = tokenizer(
    prompt,
    return_tensors="pt"
)

generated = text_model.generate(
    **encoded,
    max_new_tokens=50,
    do_sample=True,
    temperature=0.9,
    top_p=0.95
)

insta_caption = tokenizer.decode(
    generated[0],
    skip_special_tokens=True
)

print("\nInstagram Caption:")
print(insta_caption)