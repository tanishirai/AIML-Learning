# AI Image Caption Generator

A beginner-friendly AI/ML project that generates captions for images using Computer Vision and optionally converts them into Instagram-style captions using NLP.

---

## Project Overview

This project combines:

- Computer Vision (CV) → Understanding image content
- Natural Language Processing (NLP) → Generating text from image understanding
- Transformer Models → State-of-the-art deep learning models
- Hugging Face Transformers → Pretrained AI models

Given an image, the system:

```text
Image
 ↓
BLIP Model
 ↓
Image Caption
 ↓
FLAN-T5 Model
 ↓
Instagram-style Caption
```

Example:

```text
Input Image:
Woman riding a bicycle

Image Caption:
a woman riding a bike down a street

Instagram Caption:
A woman rides a bike down a street in Paris.
```

---

## Features

- Upload any image from your computer
- Automatically generate an image caption
- Generate an Instagram-style caption
- Uses pretrained transformer models
- No training required
- Beginner-friendly implementation

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| PyTorch | Deep Learning Framework |
| Hugging Face Transformers | Pretrained AI Models |
| BLIP | Image Caption Generation |
| FLAN-T5 | Text Generation |
| Pillow (PIL) | Image Processing |

---

## AI Models Used

### 1. BLIP (Bootstrapping Language-Image Pre-training)

Model:

```python
Salesforce/blip-image-captioning-base
```

Purpose:

- Understands image content
- Identifies objects and actions
- Generates natural language descriptions

Example:

```text
Image:
Dog running on grass

Output:
a dog running through a grassy field
```

---

### 2. FLAN-T5

Model:

```python
google/flan-t5-base
```

Purpose:

- Generates text from prompts
- Converts image descriptions into social-media-style captions

Example:

```text
Input:
a dog running through a grassy field

Output:
Enjoying every moment in the sunshine.
```

---

# Project Workflow

## Step 1: User Provides Image

```python
path = input("Enter image path: ")
image = Image.open(path)
```

The image is loaded using Pillow.

---

## Step 2: Image Preprocessing

```python
inputs = processor(
    images=image,
    return_tensors="pt"
)
```

What happens:

```text
Image
 ↓
Pixels
 ↓
Tensor
```

Neural networks cannot understand images directly.

They understand numerical tensors.

---

## Step 3: Caption Generation

```python
output = model.generate(
    **inputs,
    max_new_tokens=30
)
```

BLIP analyzes:

- Objects
- Actions
- Scene context

and predicts words sequentially.

Example:

```text
Woman
Bike
Road
```

becomes

```text
a woman riding a bike down a street
```

---

## Step 4: Decode Output

```python
caption = processor.decode(
    output[0],
    skip_special_tokens=True
)
```

The model outputs token IDs:

```text
[101, 235, 502, 88]
```

which are converted into readable text:

```text
a woman riding a bike down a street
```

---

## Step 5: Generate Instagram Caption

FLAN-T5 receives:

```text
Image description:
a woman riding a bike down a street
```

and generates a more natural caption.

---

# Concepts Learned

## 1. Computer Vision

Computer Vision allows machines to understand images.

In this project:

```text
Image
 ↓
BLIP
 ↓
Caption
```

---

## 2. Natural Language Processing (NLP)

NLP enables machines to understand and generate language.

In this project:

```text
Caption
 ↓
FLAN-T5
 ↓
Instagram Caption
```

---

## 3. Transformers

Both BLIP and FLAN-T5 are Transformer-based models.

Transformers power:

- ChatGPT
- Gemini
- Claude
- Modern Computer Vision Models

---

## 4. Pretrained Models

We did not train models ourselves.

Instead, we used:

```python
from_pretrained(...)
```

to download already trained models.

Benefits:

- Faster development
- No expensive hardware required
- Real-world industry practice

---

## 5. Inference

This project performs Inference.

Inference means:

```text
Input
 ↓
Pretrained Model
 ↓
Prediction
```

Example:

```text
Image
 ↓
BLIP
 ↓
Caption
```

---

## 6. Prompt Engineering

The quality of generated captions depends heavily on prompts.

Example:

```text
Create a short Instagram caption.
```

vs

```text
Create a creative Instagram caption.
Do not invent objects or people.
```

Different prompts produce different outputs.

---

## 7. Hallucination

One important AI limitation observed during development:

Example:

```text
Image Caption:
a woman riding a bike down a street

Instagram Caption:
A woman rides a bike down a street in Paris.
```

The image never mentioned Paris.

This is called:

### Hallucination

When AI generates information that sounds correct but is not supported by the input.

---

# Challenges Faced

## Image Path Errors

Issue:

```text
OSError: Invalid argument
```

Cause:

Path entered with quotes.

Solution:

```text
C:\Users\name\image.jpg
```

instead of

```text
"C:\Users\name\image.jpg"
```

---

## GPT-2 Producing Poor Captions

Issue:

GPT-2 repeated prompts instead of generating Instagram captions.

Solution:

Switched to FLAN-T5.

---

## Hallucinated Outputs

Issue:

Model added locations and details not present in the image.

Learning:

Generative AI models may hallucinate and should not always be trusted blindly.

---

# Key Takeaways

By completing this project, I learned:

- Computer Vision fundamentals
- Natural Language Processing fundamentals
- Transformer architecture usage
- Hugging Face ecosystem
- Image preprocessing
- Model inference
- Prompt engineering
- AI hallucinations
- Working with pretrained models
- Building multimodal AI pipelines

---

# Future Improvements

- Flask Web Application
- Drag-and-drop image upload
- Better caption generation models
- Multiple caption styles
- Social media caption customization
- Deployment on Render/Vercel
- Support for batch image captioning

---

# Sample Output

```text
Enter image path:
C:\Users\himan\Downloads\trial_img.jfif

Image Caption:
a woman riding a bike down a street

Instagram Caption:
A woman rides a bike down a street in Paris.
```

---

# Learning Outcome

This project demonstrates a complete multimodal AI pipeline:

```text
Image
 ↓
Computer Vision
 ↓
Image Understanding
 ↓
Natural Language Generation
 ↓
Human-readable Caption
```

It serves as an excellent beginner project for understanding how modern AI systems combine vision and language models to generate meaningful outputs.