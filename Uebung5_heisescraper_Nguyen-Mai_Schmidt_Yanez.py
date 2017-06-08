import requests
from bs4 import BeautifulSoup
from operator import itemgetter
import lxml

# Ausgabe eines Soup Page Objektes
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj


def heisescraper():

    datastore = {}    # Erstellung eines Datenspeichers
    #for page in range(1,2,1): # Seite 1 und 2 werden durchsucht

    # Alle https Themen
    all_https = "https://www.heise.de/thema/https" #+ str(page), falls weitere Seiten durchsucht werden sollen

    # https Themen
    content = getPage(all_https).find("div", {"class":"keywordliste"})
    content = content.findAll("header")

    # Wortlisten in Wörter trennen
    for line in content:
        inhalt_line = line.text.encode('utf-8')
        wortliste = inhalt_line.split()

        # Speicherung der Wörter in Datenspeicher
        for word in wortliste:
            if word not in datastore:
                datastore[word] = 1
            if word in datastore:
                datastore[word] = datastore[word] + 1

    print("HTTPS Themen auf heise.de wurden extrahiert")

    # Top 3 Wörter des Datenspeichers
    topdrei = sorted(datastore, key=datastore.get,reverse=True)[:3]
    print(topdrei)

# Test
heisescraper()

