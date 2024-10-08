from bs4 import BeautifulSoup
import pandas as pd

# Define the file path to the HTML file
file_path = 'in/NOTREVIEW_precision medicine.html'

# Open and read the content of the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
# Initialize lists to store extracted data
title_list = []      # List to store extracted titles
abstract_list = []   # List to store extracted abstracts

# Extract Titles and Abstracts
# Find all <div> tags that have a specific inline style attribute
title_divs = soup.find_all('div', style='padding:10px 10px 10px 0')
for div in title_divs:
    # Find the <h1> tag within the <div> for the title
    title_tag = div.find('h1')
    if title_tag:
        # Extract the text content of the <h1> tag and add it to the title list
        title = title_tag.text.strip()
        title_list.append(title)
    
    # Find the <h2> tag within the <div> and check if it contains the word "Abstract"
    h2_tag = div.find('h2')
    if h2_tag and "Abstract" in h2_tag.text:
        # Find all <p> tags after the <h2> that contains "Abstract"
        p_tags = div.find_all('p')

        if p_tags:
            # Combine the text from all <p> tags into one string
            abstract = ' '.join([p.text for p in p_tags])
            abstract_list.append(abstract)  # Add the abstract text to the abstract list
        else:
            abstract_list.append(None)
    else:
        abstract_list.append(None)          # Append None if there's no <h2> with "Abstract"

# Ensure both lists (titles and abstracts) have the same length for a 1:1 correspondence
min_length = min(len(title_list), len(abstract_list))

# Create a DataFrame using the lists of titles and abstracts
df = pd.DataFrame({
    'Title': title_list[:min_length],       # Take only the first 'min_length' elements from the title list
    'Abstract': abstract_list[:min_length], # Take only the first 'min_length' elements from the abstract list
})

