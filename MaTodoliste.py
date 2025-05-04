import csv
import os

def export_csv(date, reponses_dict, nom_fichier="todo.csv"):
    entetes = ["Date"] + list(reponses_dict.keys())
    ligne = [date] + list(reponses_dict.values())

    fichier_existe = os.path.isfile(nom_fichier)

    with open(nom_fichier, mode='a', encoding='utf-8', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)
        if not fichier_existe:
            writer.writerow(entetes)
        writer.writerow(ligne)

def menu_oui_non(question):
    while True:
        print(f"{question}\n1. Oui\n2. Non")
        choix = input("Votre choix (1/2) : ")
        if choix == "1":
            return "Oui"
        elif choix == "2":
            return "Non"
        else:
            print("❌ Choix invalide, veuillez entrer 1 ou 2.")


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
    print("# Essai de Todo en Python V0.4")
    maDate = input("Entrez une date au format jj/mm/aaaa : ")

    # Langues
    tacheDuolingo = menu_oui_non("Avez-vous fait Duolingo ?")
    tacheMosalingua = menu_oui_non("Avez-vous fait Mosalingua ?")

    # Espagnol
    tacheExosDele = menu_oui_non("Avez-vous fait des exercices dele ?")
    tacheNoticias = menu_oui_non("Avez-vous vu les noticias ?")
    tacheCafeynVocable = menu_oui_non("Avez-vous lu un article Caféyn Vocable ?")

    # Japonais
    tacheMondly = menu_oui_non("Avez-vous fait Mondly ?")
    tacheKana = menu_oui_non("Avez-vous fait Kana ?")
    tacheDrops = menu_oui_non("Avez-vous fait les Drops ?")
    tacheMinnaNoNihongo = menu_oui_non("Avez-vous fait Minna no Nihongo ?")

    # Python
    tachecommit = menu_oui_non("Avez-vous fait un commit GitHub ?")
    tacheDatacamp = menu_oui_non("Avez-vous fait Datacamp ?")
    tacheRealPython = menu_oui_non("Avez-vous fait Real Python ?")


    # Sport / Santé
    tacheSport = menu_oui_non("Avez-vous fait du sport ?")
    tacheApprentissage = menu_oui_non("Avez-vous fait de l'apprentissage ?")
    tacheFruits = menu_oui_non("Avez-vous mangé des fruits ?")
    tacheLegumes = menu_oui_non("Avez-vous mangé des légumes ?")
    tacheProteines = menu_oui_non("Avez-vous mangé des protéines ?")

    # Famille
    tacheFamille = menu_oui_non("Avez-vous fait un truc pour la famille ?")

    # Écriture dans le fichier
    with open("todo.txt", "w", encoding="utf-8") as fichier:
        fichier.write("Date : " + maDate + "\n\n")
        fichier.write("Version 0.4\n")

        # Espagnol
        fichier.write("Objectifs Langues\n")
        fichier.write(f"Duolingo : {tacheDuolingo}\n")
        fichier.write(f"Mosalingua Spanish : {tacheMosalingua}\n")

        fichier.write(f"Exos DELE : {tacheExosDele}\n")
        fichier.write(f"Noticias : {tacheNoticias}\n")
        
        fichier.write(f"Caféyn Vocable : {tacheCafeynVocable}\n")
        fichier.write(f"Mondly : {tacheMondly}\n")

        # Japonais
        fichier.write("Objectifs Japonais\n")
        fichier.write(f"Kana : {tacheKana}\n")
        fichier.write(f"Drops : {tacheDrops}\n")       
        fichier.write(f"Minna no Nihongo : {tacheMinnaNoNihongo}\n")


        # Python
        fichier.write("Objectifs Python\n")
        fichier.write(f"Datacamp : {tacheDatacamp}\n")
        fichier.write(f"Real Python : {tacheRealPython}\n")


        # Sport / Santé
        fichier.write("Objectifs Sport / Santé\n")
        fichier.write(f"Sport : {tacheSport}\n")
        fichier.write(f"Apprentissage : {tacheApprentissage}\n")
        fichier.write(f"Fruits : {tacheFruits}\n")
        fichier.write(f"Légumes : {tacheLegumes}\n")
        fichier.write(f"Protéines : {tacheProteines}\n")

        # Famille
        fichier.write("Objectifs Famille\n")
        fichier.write(f"Famille : {tacheFamille}\n")
        print("\n✅ Les tâches ont été enregistrées dans todo.txt.")


    reponses = {
    "Duolingo": tacheDuolingo,
    "Exos DELE": tacheExosDele,
    "Noticias": tacheNoticias,
    "Mosalingua Spanish": tacheMosalingua,
    "Caféyn Vocable": tacheCafeynVocable,
    "Mondly": tacheMondly,
    "Kana": tacheKana,
    "Drops": tacheDrops,
    "Minna no Nihongo": tacheMinnaNoNihongo,
    "Datacamp": tacheDatacamp,
    "Real Python": tacheRealPython,
    "Sport": tacheSport,
    "Apprentissage": tacheApprentissage,
    "Fruits": tacheFruits,
    "Légumes": tacheLegumes,
    "Protéines": tacheProteines,
    "Famille": tacheFamille
}
    # Export CSV
    export_csv(maDate, reponses)

if __name__ == "__main__":
    main()
              
