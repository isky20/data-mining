Title_Abstract_Extractor.py

This code is designed to extract titles and abstracts from an HTML document using the BeautifulSoup library. It specifically looks for titles within < h1 > tags and abstracts within < p > tags following an < h2 > tag containing the word "Abstract." The extracted data is then stored in lists and organized into a Pandas DataFrame for easy analysis and visualization. This tool is useful for processing and structuring unstructured HTML data into a more accessible format.


detect_diseases.py

This script processes a CSV file of textual data (such as abstracts), applies a pre-trained biomedical Named Entity Recognition (NER) model from SciSpacy to extract biomedical terms (like diseases and chemicals), and saves the updated data with extracted terms into a new CSV file

