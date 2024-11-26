from functions import (connexion,clear,
                       add_client, 
                       pret_en_cours,
                       findTelephone,
                       creer_fichier_pret,
                       versement)
from consts import *
def header(title,subtitle,motif="-"):
    clear()
    print("*"*SCREEN)
    print(title.upper().center(SCREEN,motif))   
    print("{:*>60}".format(subtitle.upper()))

def page_connexion():
    header(APP_NAME,"CONNEXION","*")
    login=input("{:>30}".format("Login: "))
    password=input("{:>30}".format("Mot de passe : "))
    return connexion(login,password)



def page_menu_general(user):
    header(APP_NAME,user,"+")
    print("1 Créer un compte")
    print("2 Faire un prêt")
    print("3 Faire Versement")
    print("4 Quitter ")
    choix=input("Entrez votre choix : ")
    return choix

def page_nouveau_client(user):
    header(APP_NAME,user,"~")
    nomCli = input("{:>30}".format("Nom du client : "))
    prenomCli = input("{:>30}".format("Prenom du client : "))
    telCli = input("{:>30}".format("Telephone du client : "))
    adresseCli = input("{:>30}".format("Adresse du client : "))
    return add_client(nomCli,prenomCli,telCli,adresseCli)

def page_pret(user):
    header(APP_NAME,user,"$")
    tel = input("{:>30}".format("Telephone du client : "))
    # 1. Verifier si le numero existe dans nos donnees
    if findTelephone(tel) == True:
        # 2. Verifier si le client n'a pas de pret en cours
        restant,nbreRembs = pret_en_cours(tel)
        if int(restant) > 0: # Pres en cours
            print(f"Le client a un pret en cours de {restant} CFA, il reste {nbreRembs} versements.")
        else: # Pas en cours
            # 3. Saisir le montant du pret
            montant = input("{:>30}".format("Montant du pret : "))
            creer_fichier_pret(tel,montant)
    # 4. Enregistrer le pret
    else:
        print("❌Le client n'existe pas!❌")
def page_versement(user):
    header(APP_NAME,user,"$")
    tel = input("{:>30}".format("Telephone du client : "))
    # 1. Verifier si le numero existe dans nos donnees
    if findTelephone(tel) == True:
        versement(tel)
    
    
    
