Explanation:
HTML Parsing with BeautifulSoup: We begin by reading the content of an HTML file and parsing it using BeautifulSoup. This allows us to navigate and search the HTML content.

Extracting Titles: We search for all <div> tags with a specific style attribute. Inside these <div> tags, we look for <h1> tags, which typically contain the titles. The titles are extracted and stored in a list.
Extracting Abstracts: We then search within the same <div> tags for <h2> tags containing the word "Abstract". If found, we assume that the corresponding abstract is contained in the following <p> tag.
Handling Missing Data: If no <p> tag is found or if there is no <h2> with "Abstract", we append None to the list to keep the lists aligned in length.
DataFrame Creation: After ensuring that both the title_list and abstract_list have the same length, we create a Pandas DataFrame to organize the extracted titles and abstracts.
Displaying the DataFrame: Finally, we display the DataFrame, which gives a tabular view of the extracted data.
