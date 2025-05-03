import csv

def sauvegarder_csv(date, categories):
    with open("todo.csv", mode="a", newline='', encoding='utf-8') as fichier_csv:
        writer = csv.writer(fichier_csv)
        # Ligne d’en-tête si le fichier est vide
        if fichier_csv.tell() == 0:
            writer.writerow(["Date", "Catégorie", "Tâche", "Fait ?"])
        for categorie, taches in categories.items():
            for tache, fait in taches.items():
                writer.writerow([date, categorie, tache, fait])



def demander_taches(categorie, taches):
    print(f"\n--- {categorie} ---")
    reponses = {}
    for tache in taches:
        reponses[tache] = input(f"Avez-vous fait {tache} ? ")
    return reponses

def ecrire_section(fichier, titre, taches):
    fichier.write(f"\nObjectifs {titre}\n")
    for tache, reponse in taches.items():
        fichier.write(f"{tache} : {reponse}\n")

def main():
    print("# Essai de Todo en Python V0.1")
    maDate = input("Entrez une date au format jj/mm/aaaa : ")

    espagnol = [
        "Duolingo", "des exercices dele", "lu les noticias", 
        "des mosalingua spanish", "un caféyn vocable", "Mondly"
    ]
    japonais = [
        "Kana", "les drops", "Japonais", 
        "katakanapro", "Minna no Nihongo", "des devoirs japonais"
    ]
    python = [
        "100 jours de code", "Code Academy", "Pybites", 
        "Datacamp", "Kaggle", "Repli", "Real Python", "un projet Python"
    ]
    sport_sante = [
        "du sport", "de l'apprentissage", 
        "des fruits", "des légumes", "des protéines"
    ]
    famille = ["un truc pour la famille"]

    # Collecte des données
    taches_espagnol = demander_taches("Espagnol", espagnol)
    taches_japonais = demander_taches("Japonais", japonais)
    taches_python = demander_taches("Python", python)
    taches_sante = demander_taches("Sport/Santé", sport_sante)
    taches_famille = demander_taches("Famille", famille)

    # Écriture dans le fichier
    with open("todo.txt", "w") as fichier:
        fichier.write(f"Date : {maDate}\n\n")
        fichier.write("Version 01 :\n")

        ecrire_section(fichier, "Espagnol", taches_espagnol)
        ecrire_section(fichier, "Japonais", taches_japonais)
        ecrire_section(fichier, "Python", taches_python)
        ecrire_section(fichier, "Sport/Sante", taches_sante)
        ecrire_section(fichier, "Famille", taches_famille)

    print("\n✅ Les tâches ont été enregistrées dans todo.txt.")


    # Regrouper les catégories
    toutes_les_taches = {
        "Espagnol": taches_espagnol,
        "Japonais": taches_japonais,
        "Python": taches_python,
        "Sport/Sante": taches_sante,
        "Famille": taches_famille
    }

    # Export CSV
    sauvegarder_csv(maDate, toutes_les_taches)

if __name__ == "__main__":
    main()
              
