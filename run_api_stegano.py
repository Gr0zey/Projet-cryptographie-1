import requests
import os
from pathlib import Path
import webbrowser
from datetime import datetime

API_BASE_URL = "https://api-anvil.onrender.com"

def upload_image(image_path: str) -> dict:
    """
    Version robuste avec gestion améliorée des erreurs et suivi de progression
    """
    try:
        path = Path(image_path).absolute()
        print(f"\nTraitement du fichier : {path}")

        # Vérifications approfondies
        if not path.exists():
            raise FileNotFoundError("Chemin introuvable")
        if path.is_dir():
            raise IsADirectoryError("Un dossier a été fourni au lieu d'un fichier")
        if path.suffix.lower() not in ['.png', '.jpg', '.jpeg']:
            raise ValueError("Format non supporté (seuls .png/.jpg/.jpeg sont acceptés)")
        if path.stat().st_size > 10 * 1024 * 1024:  # 10MB max
            raise ValueError("Fichier trop volumineux (>10MB)")
        
        print("✓ Vérifications du fichier réussies")

        # Envoi avec barre de progression simulée
        with open(path, 'rb') as img_file:
            files = {'file': (path.name, img_file, f'image/{path.suffix[1:]}')}
            print("Envoi en cours...", end='', flush=True)
            response = requests.post(f"{API_BASE_URL}/upload", files=files)
            print(" ✓")
        
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"\n[ERREUR API] Problème de connexion avec le serveur")
        print(f"Détail : {str(e)}")
    except Exception as e:
        print(f"\n[ERREUR] {type(e).__name__}: {str(e)}")
    return None

def display_results(data: dict):
    """Affichage amélioré des résultats"""
    print("\n" + "="*50)
    print("RÉSULTAT DU TRAITEMENT".center(50))
    print("="*50)
    print(f"ID: {data['id']}")
    print(f"Date: {datetime.fromisoformat(data['message_hidden']).strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"\nFichier original: {data['original_filename']}")
    print(f"Fichier traité: {data['processed_filename']}")
    
    # Générer le lien cliquable (pour certains terminaux)
    processed_url = f"{API_BASE_URL}/uploads/{Path(data['processed_filename']).name}"
    print(f"\nLien direct: {processed_url}")
    
    # Option pour ouvrir dans le navigateur
    if input("\nOuvrir l'image dans le navigateur? (o/n) ").lower() == 'o':
        webbrowser.open(processed_url)

def main():
    print("\n" + "="*50)
    print("CLIENT STÉGANOGRAPHIE ANVIL".center(50))
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Stéganographier une image")
        print("2. Quitter")
        
        choice = input("Votre choix [1-2]: ").strip()
        
        if choice == "1":
            print("\nInstructions:")
            print("- Formats acceptés: PNG, JPG, JPEG")
            print("- Taille max: 10MB")
            print("- Exemple: C:/Users/Jean/Desktop/image.png ou /home/user/images/photo.jpg")
            
            image_path = input("\nChemin complet vers l'image: ").strip('"\' ')
            
            if not image_path:  # Si l'utilisateur ne saisit rien
                continue
                
            result = upload_image(image_path)
            if result:
                display_results(result)
        
        elif choice == "2":
            print("\nMerci d'avoir utilisé le client Anvil!")
            break
            
        else:
            print("\nOption invalide. Veuillez choisir 1 ou 2.")

if __name__ == "__main__":
    main()