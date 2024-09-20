import spacy
import pandas as pd

# Load data and NER model
data = pd.read_csv('review/dl_p.csv').dropna()
nlp = spacy.load("en_ner_bc5cdr_md")

# Extract biomedical terms function
def extract_biomedical_terms(text):
    return ', '.join(set([ent.text for ent in nlp(text).ents])) or 'None'

# Apply extraction and save results
data['biomedical_terms'] = data['Abstract'].apply(extract_biomedical_terms)
data.dropna(subset=['biomedical_terms']).to_csv('updated_file_with_scispacy_diseases.csv', index=False)
