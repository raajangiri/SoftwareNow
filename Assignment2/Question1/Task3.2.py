

from collections import Counter
from transformers import AutoTokenizer

# Function to count unique tokens and return top 30, processing file in chunks
def count_unique_tokens_in_chunks(file_path, tokenizer_name='bert-base-uncased'):
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    
    token_counts = Counter()

    # Read the file content line by line to avoid memory issues
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Tokenize the line
            tokens = tokenizer.tokenize(line)
            # Update the token counter
            token_counts.update(tokens)

    # Get the top 30 most common tokens
    top_30 = token_counts.most_common(30)
    
    return top_30

# Example usage
file_path = r'C:\Users\Acer\Downloads\Assignment 2\Question1\rajan.txt'  # Path to your .txt file
top_30_tokens = count_unique_tokens_in_chunks(file_path)

# Display the top 30 tokens and their counts
for token, count in top_30_tokens:
    print(f"{token}: {count}")







