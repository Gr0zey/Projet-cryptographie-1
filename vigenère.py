
def vigenere(c, cle, mode="encode"):
    indice_cle = 0
    msg_code = ""

    for i in range(len(c)):
        if 'A' <= c[i] <= 'Z':
            decalage = (ord(cle[indice_cle]) - ord('A'))
            if mode == "decode":
                decalage = -decalage
            lettre = chr(((ord(c[i]) - ord('A') + decalage) %26) + ord('A'))
            msg_code += lettre
            indice_cle = (indice_cle + 1) % len(cle)
        else:
            msg_code += c[i]
    return msg_code

while True:
    phrase = input("Entrez la phrase à encoder (en MAJUSCULES uniquement) : ")
    cle = input("Entrez la clé (en MAJUSCULES uniquement) : ")
    mode = input("Voulez-vous encoder ou décoder? ('encode' ou 'decode') : ")

    print("Message codé :", vigenere(phrase, cle, mode))

    continuer = input("Voulez-vous continuer? (O/n) : ")
    if continuer != 'O' and continuer != 'o' :
        break