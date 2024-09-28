#Essai de Todo en Python V0.1 ajout de nouvelles taches 
maDate=input("Entrez une date au format jj/mm/aaaa : ")
#Espagnol
tacheDuolingo=input("Avez-vous fait Duolingo : ")
tacheExosDele=input("Avez-vous fait des exercices dele : ")
tacheNoticias=input("Avez-vous lu les noticias : ")
tacheMosalingua=input("Avez-vous fait des mosalingua spanish: ")
tacheCafeynVocable=input("Avez-vous fait un caféyn vocable : ")
tacheMondly=input("Avez-vous fait Mondly : ")
#Japonais
tacheKana=input("Avez-vous fait Kana : ")
tacheDrops=input("Avez-vous fait les drops : ")
tacheMosaJaponais=input("Avez-vous fait Japonais : ")
tachekatakanapro=input("Avez-vous fait katakanapro : ")
tacheMinnaNoNihongo=input("Avez-vous fait Minna no Nihongo : ")
tacheDevoirsJaponais=input("Avez-vous fait des devoirs japonais : ")
#Python
tache100days=input("Avez-vous fait 100 jours de code : ")
tacheCodeAcademy=input("Avez-vous fait Code Academy : ")
tachePybites=input("Avez-vous fait Pybites : ")
tacheDatacamp=input("Avez-vous fait Datacamp : ")
tacheKaggle=input("Avez-vous fait Kaggle : ")
tacherepli=input("Avez-vous fait Repli : ")
tacheRealPython=input("Avez-vous fait Real Python : ")
tacheProjetPython=input("Avez-vous fait un projet Python : ")
#Sport/Sante
tacheSport=input("Avez-vous fait du sport : ")
tacheApprentissage=input("Avez-vous fait de l'apprentissage : ")
tacheFruits=input("Avez-vous mangé des fruits : ")
tacheLegumes=input("Avez-vous mangé des légumes : ")
tacheProteines=input("Avez-vous mangé des protéines : ")
#Famille
tacheFamille=input("Avez-vous fait un truc pour la  famille : ")


#on affiche les résultats dans le fichier todo
fichier=open("todo.txt","w")
#écrire dans le fichier
fichier.write("Date : "+maDate+"\n\n")
fichier.write("Version 01 : ")
#Espagnol
fichier.write("Objectifs Espagnol\n")            
fichier.write("Duolingo : "+tacheDuolingo+"\n")
fichier.write("Exos dele : "+tacheExosDele+"\n")
fichier.write("Noticias : "+tacheNoticias+"\n")
fichier.write("Mosalingua spanish: "+tacheMosalingua+"\n")
fichier.write("Caféyn vocable : "+tacheCafeynVocable+"\n")
fichier.write("Mondly : "+tacheMondly+"\n")
            
#Japonais
fichier.write("Objectifs Japonais\n")
fichier.write("Kana : "+tacheKana+"\n")
fichier.write("Drops : "+tacheDrops+"\n")
fichier.write("Japonais : "+tacheMosaJaponais+"\n")
fichier.write("Katakanapro : "+tachekatakanapro+"\n")
fichier.write("Minna no Nihongo : "+tacheMinnaNoNihongo+"\n")
fichier.write("Devoirs japonais : "+tacheDevoirsJaponais+"\n")
#Python
fichier.write("Objectifs Python\n")
fichier.write("100 jours de code : "+tache100days+"\n")
fichier.write("Code Academy : "+tacheCodeAcademy+"\n")
fichier.write("Pybites : "+tachePybites+"\n")
fichier.write("Datacamp : "+tacheDatacamp+"\n")
fichier.write("Kaggle : "+tacheKaggle+"\n")
fichier.write("Repli : "+tacherepli+"\n")
fichier.write("Real Python : "+tacheRealPython+"\n")
fichier.write("Projet Python : "+tacheProjetPython+"\n")
#Sport/Sante
fichier.write("Objectifs Sport/Sante\n")
fichier.write("Sport : "+tacheSport+"\n")
fichier.write("Apprentissage : "+tacheApprentissage+"\n")
fichier.write("Fruits : "+tacheFruits+"\n")
fichier.write("Legumes : "+tacheLegumes+"\n")
fichier.write("Proteines : "+tacheProteines+"\n")
              
#Famille
fichier.write("Objectifs Famille\n")
fichier.write("Famille : "+tacheFamille+"\n")
#fermer le fichier
fichier.close()

              
