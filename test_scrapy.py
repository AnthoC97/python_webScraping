#pour la requête get (http)
from requests import get

#pour le parsing
from scrapy import Selector

#lien de la page a scraper
url = "https://fr.wikipedia.org/wiki/Star_Wars"
response = get(url)

#code source de la page
source = None
if response.status_code == 200:
    source = response.text

#Parsing(on veut reccuperer les titres du sommaire
#Balise li dans balise ul
if source :
    selector = Selector(text=source)
    titles = selector.css("div.toc ul > li")
    for title in titles:
        level = title.css("span.tocnumber::text").extract_first()
        name = titles.css("span.toctext::text").extract_first()
        print(level + " " + name)
