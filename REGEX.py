#Convertir tout tag dans un texte en lien HTML
import re

def HashtagToLink(tèks):
    IdantifyeMo = r"#(\w+)"
    ranplase = r'<a href="https://www.linkedin.com/in/wilnise-meus-721baa22a">#\1</a>'
    return re.sub(IdantifyeMo, ranplase, tèks)

tèks = "Ceci est un #lien emmenant à mon profil LinkedIn."
print(HashtagToLink(tèks))