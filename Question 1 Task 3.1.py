import csv
from collections import Counter

# Path to the extracted text file
input_txt_file = r'C:\Users\mahak\OneDrive\Desktop\HIT137\extracted_texts.txt'

# Path for the output CSV file
output_csv_file = r'C:\Users\mahak\OneDrive\Desktop\HIT137\top_30_words.csv'

# Open the text file and read its content
with open(input_txt_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize the text into words (split by whitespace)
words = text.split()

# Count the occurrences of each word (case insensitive)
word_counts = Counter([word.lower() for word in words])

# Get the 30 most common words
top_30_words = word_counts.most_common(30)

# Write the top 30 words and their counts to a CSV file
with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word', 'Count'])  # Writing header
    writer.writerows(top_30_words)  # Writing the words and their counts

print(f"Top 30 words written to {output_csv_file}")
