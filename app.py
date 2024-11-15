from views import (page_menu_general,
                   page_connexion, 
                   page_nouveau_client,
                   page_pret,
                   page_versement)
from functions import *
while True :
    connected_user=page_connexion()
    if connected_user is not None: #Si l'utilisateur existe
        break
    else:
        print("Login et/ou mot de passe invalide!")
        pause()
    
while True :
    choix=page_menu_general(connected_user)
    if choix=="1":
        page_nouveau_client(connected_user)
        pause()
    elif choix=="2":
        page_pret(connected_user)
        pause()
    elif choix=="3":
        page_versement(connected_user)
        pause()
    elif choix=="4":
        break
    else :
        print("Choix indisponible!")
