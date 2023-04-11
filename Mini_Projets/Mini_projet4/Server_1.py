from microbit import *
import radio

def on():
    On = Image("99999:99999:99999:99999:99999")
    
    display.show(On)
    sleep(500)
    display.clear()
    sleep(100)
    display.show(On)
    sleep(250)
on()

def generer_cle(valeurs): ##Pour coder en RSA
    a1, b1, a2, b2 = valeurs
    M = a1 * b1 - 1
    e = a2 * M + a1
    d = b2 * M + b1
    N = (e * d - 1) // M
    cle_publique = (e, N)
    cle_privee = (d, N)
    return cle_privee, cle_publique ##retourne un tuple de deux couple de valeur

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

def dechiffrer_rsa(cle, val):
    """ Déchiffre une valeur chiffrée à l'aide de la clé privée suivant l'algorithme RSA. 
        Entrées :
            cle (tuple) --> tuple d'entier formant la clé privée
            val (int) --> valeur chiffrée à déchiffrer 
        Sortie :
            lettre (str) --> lettre correspondante à la valeur déchiffrée
    """
    # Vérifier que la clé privée est bien sous la forme d'un tuple (d, n)
    assert (cle, tuple) and len(cle) == 2 and (cle[0], int) and (cle[1], int), "La clé privée doit être un tuple d'entiers de la forme (d, n)"
    
    # Déchiffrer la valeur à l'aide de la clé privée
    d, n = cle
    message=""
    
    for i in range(0, len(val)): ##on parcour le mot encrypté
        val_dechiffre = (d *  int(val[i])) % n
        lettre = chr(val_dechiffre)
        message = message + str(lettre)

    
    return message

radio.config(group=23)
radio.on()


while True:
    
    display.clear()
    
    message = radio.receive() ##Recois le msg de la carte 'Client'
    if message == "www.client.fr": ##début de la procédure
        display.scroll("Connexion...")
        
        """phase d'émission du serveur"""
        cle_publique = generer_cle((1, 2, 3, 4))[1] 
        cle_privee = generer_cle((1, 2, 3, 4))[0]
        cle_publique = codagecesar(str(cle_publique), 9, 1) ##on encrypte la cle publique avec comme numéro de session 9
        radio.send(cle_publique) ##envoie de la cle encrypté au client 
        
        """phase de réception du serveur"""
        message_crypté = radio.recieve() ##réception du message crypté du client 
        message = dechiffrer_rsa(message_crypté, cle_privee) ##on décode le message crypté grâce à la cle privee
        display.scroll(message) ##on affiche le message décode, envoyé par le client


        

