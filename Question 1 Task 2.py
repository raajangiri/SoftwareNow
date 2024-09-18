import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import os

# Path to the text file
input_txt_file = r'C:/Users/Dell/OneDrive/Desktop/HIT137/Assingment2/Hit137/extracted_texts.txt'

# Check if the file exists
if os.path.exists(input_txt_file):
    with open(input_txt_file, 'r', encoding='utf-8') as file:
        text = file.read()
else:
    print(f"File not found: {input_txt_file}")
    exit()

# Load SciSpacy models
nlp_sci_sm = spacy.load("en_core_sci_sm")  # Small biomedical model
nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")  # Disease and chemical detection model

# Load BioBERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
ner_biobert = pipeline("ner", model=model, tokenizer=tokenizer)

# Extract entities using SciSpacy (en_core_sci_sm)
doc_sci_sm = nlp_sci_sm(text)
sci_sm_diseases = [ent.text for ent in doc_sci_sm.ents if ent.label_ == "DISEASE"]
sci_sm_drugs = [ent.text for ent in doc_sci_sm.ents if ent.label_ == "CHEMICAL"]

print(f"SciSpacy (en_core_sci_sm) Disease Entities: {sci_sm_diseases}")
print(f"SciSpacy (en_core_sci_sm) Drug Entities: {sci_sm_drugs}")

# Extract entities using SciSpacy (en_ner_bc5cdr_md)
doc_bc5cdr = nlp_bc5cdr(text)
bc5cdr_diseases = [ent.text for ent in doc_bc5cdr.ents if ent.label_ == "DISEASE"]
bc5cdr_drugs = [ent.text for ent in doc_bc5cdr.ents if ent.label_ == "CHEMICAL"]

print(f"SciSpacy (en_ner_bc5cdr_md) Disease Entities: {bc5cdr_diseases}")
print(f"SciSpacy (en_ner_bc5cdr_md) Drug Entities: {bc5cdr_drugs}")

# Extract entities using BioBERT
biobert_entities = ner_biobert(text)
biobert_diseases = [ent['word'] for ent in biobert_entities if 'B-Disease' in ent['entity']]
biobert_drugs = [ent['word'] for ent in biobert_entities if 'B-Drug' in ent['entity']]

print(f"BioBERT Disease Entities: {biobert_diseases}")
print(f"BioBERT Drug Entities: {biobert_drugs}")

# Compare results
sci_total_entities = len(sci_sm_diseases) + len(sci_sm_drugs)
biobert_total_entities = len(biobert_diseases) + len(biobert_drugs)

print(f"Total Entities Detected by SciSpacy (en_core_sci_sm): {sci_total_entities}")
print(f"Total Entities Detected by BioBERT: {biobert_total_entities}")

# Common and unique entities
sci_common_entities = sci_sm_diseases + sci_sm_drugs
biobert_common_entities = biobert_diseases + biobert_drugs

overlap = set(sci_common_entities) & set(biobert_common_entities)
print(f"Common Entities Detected by Both Models: {overlap}")

sci_unique = set(sci_common_entities) - set(biobert_common_entities)
biobert_unique = set(biobert_common_entities) - set(sci_common_entities)

print(f"Unique Entities Detected by SciSpacy: {sci_unique}")
print(f"Unique Entities Detected by BioBERT: {biobert_unique}")
