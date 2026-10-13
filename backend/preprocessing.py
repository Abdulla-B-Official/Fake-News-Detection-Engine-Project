"""
Preprocessing Pipeline Module
Handles text cleaning, missing value checks, and feature formatting.
"""
import pandas as pd

def clean_news_text(title, text):
    """
    Cleans and combines title and text inputs for model ingestion.
    Args:
        title (str): News article headline.
        text (str): News article body text.
    Returns:
        str: Cleaned and merged text string.
    """
    title_str = str(title) if title is not None else ""
    text_str = str(text) if text is not None else ""
    
    # Merge headline and text for optimal semantic representation
    combined = f"{title_str} {text_str}".strip()
    return combined