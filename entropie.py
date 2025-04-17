import math
import re

def entropy(password):
    char_set = set(password)
    char_set_size = len(char_set)
    password_size = len(password)
    entropy = math.log2(char_set_size ** password_size)
    return entropy

def password_recommendations(password):
    recommendations = []
    if len(password) < 14:
        recommendations.append("Le mot de passe est trop court. Utilisez au moins 14 caractères.")
    if not re.search(r'[A-Z]', password):
        recommendations.append("Ajoutez des lettres majuscules.")
    if not re.search(r'[a-z]', password):
        recommendations.append("Ajoutez des lettres minuscules.")
    if not re.search(r'\d', password):
        recommendations.append("Ajoutez des chiffres.")
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        recommendations.append("Ajoutez des caractères spéciaux.")
    return recommendations

while True:
    password = input("Entrez votre mot de passe :")
    e = entropy(password)
    recommendations = password_recommendations(password)

    if recommendations :
        print("Suggestions d'amélioration :")
        for rec in recommendations:
            print(f"- {rec}")
        continue

    if e <= 80 :
        print(f"L'entropie de votre mot de passe est trop faible : {e:.2f} bits\r\nIl faut au minimum 80 bits d'entropie. ")
        continue

    print(f"L'entropie de votre mot de passe est : {e:.2f} bits")
        
    break