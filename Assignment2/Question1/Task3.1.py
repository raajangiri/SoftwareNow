import csv
from collections import Counter
import re

# Function to read the file and return the top 30 word frequencies
def calculateWordFrequencies(fileLocation):
    with open(fileLocation, 'r', encoding='utf-8') as file:
        documentContent = file.read()

    # Tokenize and clean the content (remove punctuation and convert to lowercase)
    wordList = re.findall(r'\b\w+\b', documentContent.lower())

    # Count occurrences of each word using Counter
    wordFrequency = Counter(wordList)

    # Extract the 30 most frequent words
    topWords = wordFrequency.most_common(30)
    
    return topWords

# Function to save the word frequency data to a CSV file
def exportToCsv(wordData, outputFileName):
    with open(outputFileName, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Word', 'Count'])  # Write the CSV header
        writer.writerows(wordData)  # Write each word and its corresponding count

# Example usage: specify the input text file and the output CSV file
fileLocation = r'C:\Users\Acer\Downloads\Assignment 2\Question1\rajan.txt'  # Path to the text file to process
outputFileName =  r'C:\Users\Acer\Downloads\Assignment 2\Question1\rajanOutput.csv'  # Path to save the CSV with word frequencies

# Calculate the top 30 words and export the results to a CSV file
topWords = calculateWordFrequencies(fileLocation)
exportToCsv(topWords, outputFileName)

print(f'Top 30 words have been saved to {outputFileName}')
