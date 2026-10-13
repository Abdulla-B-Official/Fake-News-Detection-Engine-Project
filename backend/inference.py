"""
Inference Pipeline Module
Loads the fine-tuned DistilBERT model from disk and generates predictions with confidence scores.
"""
import os
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Define absolute path to saved model weights
MODEL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../saved_fake_news_model"))

print(f"Loading model and tokenizer from: {MODEL_DIR}")
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
model.eval() # Set model to evaluation mode

def predict_article(news_text):
    """
    Tokenizes input text and predicts whether it is Real or Fake news.
    Args:
        news_text (str): The combined headline and article content.
    Returns:
        dict: Prediction label and confidence score percentage.
    """
    if not news_text or len(news_text.strip()) < 5:
        return {"error": "Please provide a valid news article text."}

    # Tokenize text with truncation and padding specifications
    inputs = tokenizer(
        news_text, 
        return_tensors="pt", 
        truncation=True, 
        max_length=512,
        padding=True
    )
    
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)
        pred_label_id = torch.argmax(probs, dim=-1).item()
        confidence = probs[0][pred_label_id].item() * 100
        
    # --- FLIPPED LABEL MAP TO CORRECT INVERSION ---
    # If index 0 is actually Real and 1 is Fake in your training split orientation:
    label_map = {
        0: {"label": "Real News ✅", "status": "real"},
        1: {"label": "Fake News 🛑", "status": "fake"}
    }
    
    result = label_map[pred_label_id]
    return {
        "prediction": result["label"],
        "status": result["status"],
        "confidence": round(confidence, 2)
    }