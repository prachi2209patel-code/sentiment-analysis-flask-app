import re
import string

def clean_text(text):
    text = str(text)

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove mentions & hashtags
    text = re.sub(r"@\w+|#\w+", "", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Normalize repeated letters (soooo → soo)
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text