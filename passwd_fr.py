import random
import string
import os

def generer_mot_de_passe(debut, fin, longueur, inclure_majuscules, inclure_minuscules, inclure_chiffres, inclure_caracteres_speciaux):
    caracteres_centraux = ''
    if inclure_majuscules:
        caracteres_centraux += string.ascii_uppercase
    if inclure_minuscules:
        caracteres_centraux += string.ascii_lowercase
    if inclure_chiffres:
        caracteres_centraux += string.digits
    if inclure_caracteres_speciaux:
        caracteres_centraux += string.punctuation

    # Générer une séquence aléatoire de caractères pour la partie centrale
    caracteres_centraux = ''.join(random.choices(caracteres_centraux, k=longueur))

    # Concaténer les parties pour former le mot de passe complet
    mot_de_passe = debut + caracteres_centraux + fin
    return mot_de_passe

def enregistrer_dans_fichier(donnees, chemin_fichier):
    with open(chemin_fichier, 'a') as fichier:
        fichier.write(donnees + '\n')

def main():
    fichier_debut = 'debut.txt'
    fichier_fin = 'fin.txt'
    fichier_sortie_base = 'mot_de_passe_'
    extension_fichier_sortie = '.txt'

    debut = None
    fin = None

    try:
        with open(fichier_debut, 'r') as fichier:
            debut = fichier.read().strip()
    except FileNotFoundError:
        pass

    try:
        with open(fichier_fin, 'r') as fichier:
            fin = fichier.read().strip()
    except FileNotFoundError:
        pass

    if debut is None:
        debut = input("Entrez le mot pour le début du mot de passe : ")
        with open(fichier_debut, 'w') as fichier:
            fichier.write(debut)

    if fin is None:
        fin = input("Entrez le mot pour la fin du mot de passe : ")
        with open(fichier_fin, 'w') as fichier:
            fichier.write(fin)

    longueur = int(input("Entrez le nombre de caractères entre les deux mots : "))

    inclure_majuscules = input("Voulez-vous inclure des majuscules ? (Oui/Non) ").lower() == 'oui'
    inclure_minuscules = input("Voulez-vous inclure des minuscules ? (Oui/Non) ").lower() == 'oui'
    inclure_chiffres = input("Voulez-vous inclure des chiffres ? (Oui/Non) ").lower() == 'oui'
    inclure_caracteres_speciaux = input("Voulez-vous inclure des caractères spéciaux ? (Oui/Non) ").lower() == 'oui'

    fichier_sortie = fichier_sortie_base + extension_fichier_sortie
    compteur = 1

    while os.path.exists(fichier_sortie):
        compteur += 1
        fichier_sortie = f"{fichier_sortie_base}_{compteur:02d}{extension_fichier_sortie}"

    with open(fichier_sortie, 'w') as fichier:
        for i in range(1, 6):
            mot_de_passe = generer_mot_de_passe(debut, fin, longueur, inclure_majuscules, inclure_minuscules, inclure_chiffres, inclure_caracteres_speciaux)
            enregistrer_dans_fichier(mot_de_passe, fichier_sortie)
            print(f"Mot de passe généré {i} : {mot_de_passe}")

    print(f"Mots de passe enregistrés dans {fichier_sortie}")

if __name__ == "__main__":
    main()
