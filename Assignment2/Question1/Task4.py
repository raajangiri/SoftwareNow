

import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
from collections import Counter

def extractMedicalEntitiesSpacy(fileLocation, spacyModel):
    nlpTool = spacy.load(spacyModel)
    nlpTool.max_length = 2000000  # Extending max_length for handling large files

    with open(fileLocation, 'r', encoding='utf-8') as fileData:
        documentText = fileData.read()

    diseasesFound = set()
    drugsFound = set()

    # Processing the text using the spaCy model
    docResult = nlpTool(documentText)

    for entity in docResult.ents:
        if entity.label_ == 'DISEASE':
            diseasesFound.add(entity.text)
        elif entity.label_ == 'CHEMICAL':
            drugsFound.add(entity.text)

    return diseasesFound, drugsFound

def extractMedicalEntitiesBioBert(fileLocation, bioBertModel):
    tokenizerBioBert = AutoTokenizer.from_pretrained(bioBertModel)
    modelBioBert = AutoModelForTokenClassification.from_pretrained(bioBertModel)

    with open(fileLocation, 'r', encoding='utf-8') as fileData:
        documentText = fileData.read()

    tokenizedInputs = tokenizerBioBert(documentText, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputPredictions = modelBioBert(**tokenizedInputs)

    labelPredictions = torch.argmax(outputPredictions.logits, dim=2)

    detectedDiseases = set()
    detectedDrugs = set()
    
    tokensDetected = tokenizerBioBert.convert_ids_to_tokens(tokenizedInputs['input_ids'][0])
    activeEntity = []
    
    for token, prediction in zip(tokensDetected, labelPredictions[0]):
        entityLabel = modelBioBert.config.id2label[prediction.item()]

        if 'B-' in entityLabel:
            if activeEntity:
                entityStr = tokenizerBioBert.convert_tokens_to_string(activeEntity).replace(' ##', '')
                if 'DISEASE' in entityLabel:
                    detectedDiseases.add(entityStr)
                elif 'CHEMICAL' in entityLabel:
                    detectedDrugs.add(entityStr)
            activeEntity = [token]
        elif 'I-' in entityLabel:
            activeEntity.append(token)
        else:
            if activeEntity:
                entityStr = tokenizerBioBert.convert_tokens_to_string(activeEntity).replace(' ##', '')
                if 'DISEASE' in entityLabel:
                    detectedDiseases.add(entityStr)
                elif 'CHEMICAL' in entityLabel:
                    detectedDrugs.add(entityStr)
                activeEntity = []

    if activeEntity:
        entityStr = tokenizerBioBert.convert_tokens_to_string(activeEntity).replace(' ##', '')
        if 'DISEASE' in entityLabel:
            detectedDiseases.add(entityStr)
        elif 'CHEMICAL' in entityLabel:
            detectedDrugs.add(entityStr)

    return detectedDiseases, detectedDrugs

def analyzeEntityOverlap(setA, setB):
    sharedEntities = setA.intersection(setB)
    uniqueInSetA = setA - setB
    uniqueInSetB = setB - setA

    return sharedEntities, uniqueInSetA, uniqueInSetB

def mostFrequentTerms(entityCollection, topCount=10):
    wordList = [term for entity in entityCollection for term in entity.split()]
    wordFrequency = Counter(wordList)
    return wordFrequency.most_common(topCount)

# Sample usage
fileLocation = r'C:\Users\Acer\Downloads\Assignment 2\Question1\rajan.txt'  
# fileLocation = 'app.txt'  

# For spaCy model en_core_sci_sm
spacyModel = 'en_core_sci_sm'
identifiedDiseasesSpacy, identifiedDrugsSpacy = extractMedicalEntitiesSpacy(fileLocation, spacyModel)

# For BioBERT model
bioBertModel = 'monologg/biobert_v1.1_pubmed'
identifiedDiseasesBioBert, identifiedDrugsBioBert = extractMedicalEntitiesBioBert(fileLocation, bioBertModel)

# Comparing the results of spaCy and BioBERT
overlappingDiseases, exclusiveDiseasesSpacy, exclusiveDiseasesBioBert = analyzeEntityOverlap(identifiedDiseasesSpacy, identifiedDiseasesBioBert)
overlappingDrugs, exclusiveDrugsSpacy, exclusiveDrugsBioBert = analyzeEntityOverlap(identifiedDrugsSpacy, identifiedDrugsBioBert)

# Outputting the results in reverse order

# Displaying most frequent terms
print("\nTop terms in common drugs identified by both models:")
print("Most frequent words in common drugs:", mostFrequentTerms(overlappingDrugs))

print("\nTop terms in common diseases identified by both models:")
print("Most frequent words in common diseases:", mostFrequentTerms(overlappingDiseases))

# Outputting unique entities detected by BioBERT only
print("\nBioBERT model identified unique entities:")
print("Unique Diseases (BioBERT):", exclusiveDiseasesBioBert)
print("Unique Drugs (BioBERT):", exclusiveDrugsBioBert)

# Outputting unique entities detected by spaCy only
print("\nspaCy model identified unique entities:")
print("Unique Diseases (spaCy):", exclusiveDiseasesSpacy)
print("Unique Drugs (spaCy):", exclusiveDrugsSpacy)

# Outputting common entities
print("\nCommon entities detected by both models:")
print("Diseases common to both:", overlappingDiseases)
print("Drugs common to both:", overlappingDrugs)

