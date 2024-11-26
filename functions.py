import os
from consts import *
from genericpath import exists

def connexion(login,password):
    with open(USER_FILE,"r") as f:
        for u in f:
            nom,log,pas=u.strip().split(":")
            if login==log and password==pas:
                return nom
        return None
def clear():
    if os.name=="nt":
        os.system("cls")
    else :
        os.system("clear")

def pause():
    input("\n\nappuyer sur une touche pour continuer ...")

def add_client(nomCli,prenomCli,telCli,adresseCli):
    if findTelephone(telCli) == False:
        with open(CLIENT_FILE,"a") as f:
            f.write(f"{prenomCli} {nomCli}:{telCli}:{adresseCli}\n")
            print("Client ajoute avec succes ✅")
    else:
        print(f"Ce numero '{telCli}' a deja un compte 🤧")
        
def findTelephone(telToFind):
    with open(CLIENT_FILE,"r") as f:
        for c in f:
            tel = c.strip().split(":")[1]
            if tel == telToFind:
                return True
        return False
    
def creer_fichier_pret(tel,montant):
    # fichier_pret = r"./BD/PRET/"+tel+".txt"
    fichier_pret = f"./BD/PRET/{tel}.txt"
    if not exists(fichier_pret): #Si le fichier n'existe pas (pas de pret pour le client)
        mode = "w"
        content = f"{montant}:"
    else: #Si le fichier existe deja (le client a au moins un fait un pret)
        mode = "a"
        content = f"\n{montant}:"
    with open(fichier_pret,mode) as f:
        f.write(content)
    print(f"Le pret du montant de '{montant}' est effectif✅")
    
    
def versement(tel):
    # 1. Verifier si le client a un fichier
    fichier_pret = f"./BD/PRET/{tel}.txt"
    if not exists(fichier_pret):
        print("Le client n'a pas de pret !")
    else:
        # 2.Verifier si pret en cours
        montant_a_verser = 0
        restant,nbrVersement = pret_en_cours(tel)
        if restant == 0:
            print("Vous n'aves pas de pret en cours!")
        else:
            print(f"Vous devez solder: 💵 {restant} 💵")
            # Verifier si c le dernier versement
            if nbrVersement+1 == MAX_VERSEMENT:
                print("C'est le derniere versment aujourd'hui, vous devez tout solder")
                rep = yesNonQuestion("Confirmez que le client solde tout ")
                if rep == "OUI":
                    montant_a_verser = restant
                else:
                    print(f"Revener avec un montant de : {restant}")
            else:
                while True:
                    montant_a_verser = int(input("Entrer le montant a verser : "))
                    if montant_a_verser >= MIN_MNT_VERSEMENT:
                        break
                    else:
                        print(f"Il faut verser au minimum : {MIN_MNT_VERSEMENT}!")
                if montant_a_verser > restant:
                    print(f"Vous lui devez {montant_a_verser-restant} F")
                    montant_a_verser = restant
            # Enregistrer le versment
            with open(fichier_pret,"a") as f:
                if nbrVersement == 0:
                    f.write(f"{montant_a_verser}")
                else:
                    f.write(f"-{montant_a_verser}")
    
def pret_en_cours(tel):
    fichier_pret = f"./BD/PRET/{tel}.txt"
    with open(fichier_pret,"r") as f:
        prets = f.readlines()
        dernier_pret = prets[-1]
        montant_pret,versements = dernier_pret.strip().split(":")
        liste_versements = versements.strip().split("-")
        somme_versement = 0
        nbr_versments = len(liste_versements)
        for v in liste_versements:
            if v == '':
                somme_versement += 0
                nbr_versments=0
            else:
                somme_versement += int(v)
        
        restant = int(montant_pret) - somme_versement
        return [restant,nbr_versments]
    
def yesNonQuestion(question):
    while True:
        rep = input(f"{question} [Oui/Non]")
        if rep.upper() in ["OUI","NON"]:
            return rep.upper()