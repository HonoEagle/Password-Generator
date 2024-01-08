import random
import string
import os

def generer_mot_de_passe(debut, fin, longueur, inclure_majuscules, inclure_minuscules, inclure_chiffres, inclure_speciaux):
    caracteres_centraux = ''
    if inclure_majuscules:
        caracteres_centraux += string.ascii_uppercase
    if inclure_minuscules:
        caracteres_centraux += string.ascii_lowercase
    if inclure_chiffres:
        caracteres_centraux += string.digits
    if inclure_speciaux:
        caracteres_centraux += string.punctuation

    # Générer une séquence aléatoire de caractères pour la partie centrale
    caracteres_centraux = ''.join(random.choices(caracteres_centraux, k=longueur))

    # Concaténer les parties pour former le mot de passe complet
    mot_de_passe = debut + caracteres_centraux + fin
    return mot_de_passe

def enregistrer_mot_dans_fichier(mot, fichier):
    with open(fichier, 'w') as f:
        f.write(mot)

def charger_mot_de_fichier(fichier):
    if os.path.exists(fichier):
        with open(fichier, 'r') as f:
            return f.read()
    else:
        return None

def main():
    debut_file = 'debut.txt'
    fin_file = 'fin.txt'

    debut = charger_mot_de_fichier(debut_file)
    fin = charger_mot_de_fichier(fin_file)

    if debut is None:
        debut = input("Entrez le mot pour le début du mot de passe : ")
        enregistrer_mot_dans_fichier(debut, debut_file)

    if fin is None:
        fin = input("Entrez le mot pour la fin du mot de passe : ")
        enregistrer_mot_dans_fichier(fin, fin_file)

    longueur = int(input("Entrez le nombre de caractères entre les deux mots : "))

    inclure_majuscules = input("Voulez-vous inclure des majuscules ? (Oui/Non) ").lower() == 'oui'
    inclure_minuscules = input("Voulez-vous inclure des minuscules ? (Oui/Non) ").lower() == 'oui'
    inclure_chiffres = input("Voulez-vous inclure des chiffres ? (Oui/Non) ").lower() == 'oui'
    inclure_speciaux = input("Voulez-vous inclure des caractères spéciaux ? (Oui/Non) ").lower() == 'oui'

    mot_de_passe = generer_mot_de_passe(debut, fin, longueur, inclure_majuscules, inclure_minuscules, inclure_chiffres, inclure_speciaux)

    print("Mot de passe généré:", mot_de_passe)

if __name__ == "__main__":
    main()
