import requests
from bs4 import BeautifulSoup
import spacy

# Load the spaCy model
# nlp = spacy.load("./src/model-best")
nlp = spacy.load("en")

def get_page_content(url):
    # Send a GET request to the webpage
    print("get_page_content ", url)
    response = requests.get(url)
    print("get_page_content")
    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Completed fetch ")
    # Extract text from the body and strip any extra whitespace
    body_content = soup.body.get_text(separator='. ', strip=True)
    print("Parsed")
    # print(body_content)
    # tag = soup.body
    # Print each string recursively
    # print(tag)
    return body_content

def extract_locations(text):
    """
    Extract physical locations from the given text using spaCy's NER.

    Args:
    text (str): The text to search within.

    Returns:
    list: A list of unique physical locations found in the text.
    """
    # Process the text with spaCy
    doc = nlp(text)

    locationsWithDetails = []
    # Extract locations
    # locations = [ent.text for ent in doc.ents if ent.label_ == "GPE" or ent.label_ == "LOC" or ent.label_ == "NORP" or ent.label_ == "ORG"]

    for ent in doc.ents:
        # if ent.label_ == "w_countries" or ent.label_ == "w_cities" or ent.label_ == "w_region" or ent.label_ == "w_states":
        if ent.label_ == "GPE" or ent.label_ == "LOC" or ent.label_ == "NORP" or ent.label_ == "ORG":
            print( "   ", {ent,ent.label_})
            locationsWithDetails.append(ent.text)

    return list(set(locationsWithDetails))

def process_and_analyse(url):
    print(url)
    content = get_page_content(url)
    print(content)
    locations = extract_locations(content)
    print("Searched for locations\n")
    return locations

