# 📜 Changelog

Toutes les modifications notables du projet seront documentées ici.

Le format est inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/)  
et ce projet suit la [sémantique de versionnage](https://semver.org/lang/fr/).

---

## [0.5] - 2025-05-05
### Ajouté
- ✅ Fonction `export_csv` pour exporter les réponses dans un fichier CSV (`todo.csv`).
- ✅ Gestion automatique de l'entête dans le CSV si le fichier n'existe pas encore.
- ✅ Formatage du texte de sortie amélioré dans `todo.txt`.
- 📅 Suggestion automatique de la date du jour à l'utilisateur.
- 📊 Score automatique calculé (pourcentage de "Oui").

### Modifié
- ♻️ Organisation plus logique du code avec fonctions réutilisables (`menu_oui_non`, `export_csv`, etc.).
- 📁 Nom du fichier CSV configurable avec une valeur par défaut (`todo.csv`).

### Prochaine étape possible
- ⏳ Ajouter un menu principal avec plusieurs options (afficher les tâches précédentes, exporter manuellement, etc.).
- ⏳ Sauvegarde dans un format JSON ou base de données pour requêtes futures.

## [0.4] - 2025-05-04
### Ajouté
- Saisie Todo simplifiée avec 1 ou 2
- Modification du Readme

## [0.3] - 2025-05-03
### Ajouté
- Export CSV des tâches journalières.
- Structure du fichier CSV : Date, Catégorie, Tâche, Fait ?.
- Support de l'encodage UTF-8 pour compatibilité multi-OS.

## [0.2] - 2025-05-02
### Modifié
- Refactorisation complète du script.
- Ajout de fonctions pour chaque groupe de tâches.
- Meilleure organisation du code (`main()`, modularisation).

## [0.1] - 2024-09-28
### Créé
- Version initiale du script.
- Entrée manuelle de tâches dans différentes catégories.
- Export dans un fichier `todo.txt` formaté.