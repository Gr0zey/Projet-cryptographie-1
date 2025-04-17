import numpy as np
from egcd import egcd

alphabet = "abcdefghijklmnopqrstuvwxyz "

lettre_vers_index = dict(zip(alphabet, range(len(alphabet))))
index_vers_lettre = dict(zip(range(len(alphabet)), alphabet))

def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = egcd(det, modulus)[1] % modulus
    matrix_modulus_inv = det_inv * np.round(det*np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_modulus_inv

def encrypt(message, K):
    if not message:
        return ""
    
    encrypted = ''
    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(lettre_vers_index[letter])

    split_P = [message_in_numbers[i:i+int(K.shape[0])] for i in range(0, len(message_in_numbers), int(K.shape[0]))]

    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]
        
        if P.shape[0] != K.shape[0]:
            P = np.append(P, lettre_vers_index[' '])[:, np.newaxis]

        numbers = np.dot(K, P) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_vers_lettre[number]

    return encrypted

def decrypt(cipher, Kinv):
    if not cipher:
        return ""
    
    decrypted = ''
    cipher_en_nombres = []

    for letter in cipher:
        cipher_en_nombres.append(lettre_vers_index[letter])

    split_c = [cipher_en_nombres[i:i + int(Kinv.shape[0])] for i in range(0, len(cipher_en_nombres), int(Kinv.shape[0]))]

    for C in split_c:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_vers_lettre[number]

    return decrypted

def main():
    # K = np.array([[3,3],[2,5]]) matrice de 2x2
    K = np.matrix([[3,10,20], [20,19,17], [23,78,17]]) #matrice de 3x3
    Kinv = matrix_mod_inv(K, len(alphabet))

    while True:
            message = input("Entrez le message : ")
            mode = input("Voulez-vous encoder ou décoder? ('encode' ou 'decode') : ").lower()
            
            if mode == 'encode':
                result = encrypt(message, K)
                print("Message codé :", result)
            elif mode == 'decode':
                result = decrypt(message, Kinv)
                print("Message décodé :", result)
            else:
                print("Mode non reconnu. Utilisez 'encode' ou 'decode'")

            continuer = input("Voulez-vous continuer? (O/n) : ")
            if continuer != 'O' and continuer != 'o' :
                break

if __name__ == "__main__":
    main()