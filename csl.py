import requests
from bs4 import BeautifulSoup
import pickle

def format_citation_title(filename):
    # Retire l'extension ".csl" et remplace les tirets par des espaces
    title_without_extension = filename[:-4].replace('-', ' ')
    # Capitalize chaque mot
    formatted_title = title_without_extension.title()
    return formatted_title

citation_titles = []

url = "https://github.com/citation-style-language/styles"

# Effectue une requête GET
response = requests.get(url)

# Vérifie si la requête a réussi (code 200)
if response.status_code == 200:
    # Utilise BeautifulSoup pour analyser le HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Sélectionne tous les éléments <a> avec le titre se terminant par ".csl"
    links_with_csl = soup.find_all('a', {'title': lambda title: title and title.endswith('.csl')})

    # Récupère les titres, les formate et les ajoute à la liste citation_titles
    for link in links_with_csl:
        citation_titles.append(format_citation_title(link['title']))

    # Enregistre la liste dans un fichier .pkl
    with open('formatted_citation_titles.pkl', 'wb') as file:
        pickle.dump(citation_titles, file)
else:
    # Affiche un message d'erreur si la requête a échoué
    print(f"Erreur lors de la requête : {response.status_code}")
