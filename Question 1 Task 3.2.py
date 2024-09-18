from transformers import AutoTokenizer
from collections import Counter

# Function to count unique tokens in text and return top 30
def count_unique_tokens(text_file):
    # Load pre-trained tokenizer (e.g., 'bert-base-uncased')
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

    # Read the text file
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text
    tokens = tokenizer.tokenize(text)

    # Count occurrences of each token
    token_counts = Counter(tokens)

    # Get the top 30 most common tokens
    top_30_tokens = token_counts.most_common(30)

    return top_30_tokens

# Path to the extracted text file
input_txt_file = r'C:/Users/Dell/OneDrive/Desktop/HIT137/Assignment2/Hit137/extracted_texts.txt'

# Get the top 30 unique tokens
top_30_tokens = count_unique_tokens(input_txt_file)

# Print the result
for token, count in top_30_tokens:
    print(f"{token}: {count}")
