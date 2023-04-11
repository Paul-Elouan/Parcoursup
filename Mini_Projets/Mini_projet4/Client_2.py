from microbit import *
import radio 

def on(): ##on s'assure que la carte s'allume
    On = Image("99999:99999:99999:99999:99999") 

    display.show(On)
    sleep(500)
    display.clear()
    sleep(100)
    display.show(On)
    sleep(250)

on()

radio.config(group=23) ##on initie la communication des carte sur le channel 23
radio.on()

def chiffrer_rsa(cle, message):
    """ Chiffre une message à l'aide de la clé publique suivant l'algorithme RSA. 
        Entrées :
            cle (tuple) --> tuple d'entier formant la clé publique
            message (str) --> message à chiffrer 
        Sortie :
            val_chiffre (int) --> entier representant la message chiffrée
    """
    # Vérifier que la clé publique est bien sous la forme d'un tuple (e, n)
    assert (cle, tuple) and len(cle) == 2 and (cle[0], int) and (cle[1], int), "La clé publique doit être un tuple d'entiers de la forme (e, n)"
    
    # Vérifier que la message est bien un caractère

    
    # Chiffrer la message à l'aide de la clé publique
    e, n = cle
    liste1= []

    for i in range(0, len(message)): ##boucle permettant de parcourir le mot
        val =ord(message[i])
        val_chiffre = (e*val)%n
        liste1.append(val_chiffre)
    
    return liste1

def codagecesar(message, cle, sens):
    """ Chiffre ou déchiffre un message en fonction la clé. 
        Entrées : 
            message (str) --> message clair ou chiffré
            cle (int) --> nombre de décalage de lettre
            sens (int signé) -->  +1 pour chiffrement, -1 pour déchiffrement
        Sortie :
            resultat (str) --> message chiffré ou déchiffré selon le cas
    """

    resultat = ""

    for caractere in message :
        if caractere == " ":
            resultat = resultat + " "

        else :
            code_lettre = ord(caractere) + sens*cle     # Décalage du nombre de lettre correspondant à la clé
                                                        # (ord renvoie le code ASCII du caractère)
            if code_lettre > 90 : # on a depasse vers la droite le code du Z
                code_lettre = code_lettre - 26 # donc on repart du A vers la droite (boucle)

            if code_lettre < 65 : # on a dépasse vers la gauche le code du A
                code_lettre = code_lettre + 26 # on repart du Z vers la gauche

            resultat = resultat + chr(code_lettre) # on concatene la lettre obtenue

    return resultat



while True:
    
    display.clear() ##remise à 0
    
    if button_a.is_pressed() and button_b.is_pressed(): ##équivalent au handshake
        radio.send("www.client.fr") ##message du début de la requête
        display.scroll("Connexion...") ##on "affiche" l'envoie du message 
    
    """phase de réception du client"""
    cle_publique = radio.receive() ##on récupère la clé publique encrypté du serveur 
    cle_publique_décrypté = codagecesar(cle_publique, 9, -1) ##notre numéro de session choisi est 9, on décrypte la cle_publique  
    message = "index.html" ##message qu'on souhaite envoyer
    message_crypté = chiffrer_rsa(tuple(cle_publique_décrypté), message) ##on encrypte le message avec la cle publique 
    
    """phase d'émission du client"""
    radio.send(message_crypté) ## on envoi le messahe crypté au serveur 


    