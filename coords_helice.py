import sys

SQUELETTE = ["C", "N", "CA"]
Donnees = []

def recup_squelette(files):
    with open("Coords squelette.txt", 'w') as fich_SQU:
        for file in files:
            print(f"Processing {file}")
            with open(file, 'r') as fichier:
                # récupération des lignes 1 par 1
                for ligne in fichier:
                    ligne_liste = ligne.split()
                # prise seulement des coordonnées
                    if len(ligne_liste) > 1:
                        if ligne_liste[1] in SQUELETTE:
                            Donnees.append(ligne_liste)
                            fich_SQU.write(f"{ligne_liste}\n")                            
                        #print(ligne)

    #print(f"Squelette peptidique :\n{Donnees}")
    print(len(Donnees))

if __name__ == "__main__":
    files = sys.argv[1:]  # Prends tous les fichiers sauf script
    if not files:
        print("Pas de fichier donné.")
    else:
        recup_squelette(files)