import spacy
import pandas as pd

# Load the CSV file
file_path = 'review/dl_p.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Load the pre-trained biomedical NER model from SciSpacy
nlp = spacy.load("en_ner_bc5cdr_md")  # Model specifically trained to detect diseases and chemicals

# Function to extract diseases using SciSpacy's NER
def extract_biomedical_terms(text):
    doc = nlp(text)
    terms = [ent.text for ent in doc.ents]  # Extract recognized entities
    unique_diseases = list(set(terms)) 
    return ', '.join(unique_diseases) if unique_diseases else 'None'

data = data.dropna()

#    return ', '.join(unique_diseases) if unique_diseases else 'None'
data['biomedical_terms'] = data['Abstract'].apply(extract_biomedical_terms)
df_cleaned = data.dropna(subset=['biomedical_terms']).reset_index(drop=True)
df_cleaned.to_csv('updated_file_with_scispacy_diseases.csv', index=False)
