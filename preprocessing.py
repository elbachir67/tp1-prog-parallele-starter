"""
Module de préprocessing de tweets
TP1 - Programmation Parallèle
"""

import re
import time
import pandas as pd
from collections import Counter

class TweetPreprocessor:
    """
    Classe pour le préprocessing de tweets
    Version de base non optimisée
    """
    
    def __init__(self):
        """Initialise le preprocessor avec les stop words et patterns"""
        # Stop words français et anglais les plus fréquents
        self.stop_words = {
            'le', 'la', 'de', 'et', 'un', 'une', 'les', 'des',
            'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that',
            'is', 'it', 'for', 'on', 'with', 'as', 'was', 'are'
        }
        
        # Pattern pour détecter les emojis (Unicode)
        self.emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map
            u"\U0001F1E0-\U0001F1FF"  # flags
            "]+", flags=re.UNICODE)
    
    def clean_tweet(self, text):
        """
        Nettoie un tweet en enlevant URLs, mentions, emojis, etc.
        
        Args:
            text (str): Texte du tweet à nettoyer
            
        Returns:
            str: Texte nettoyé
        """
        # Enlever les URLs (http, https, www)
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'www.\S+', '', text)
        
        # Enlever les mentions (@username)
        text = re.sub(r'@\w+', '', text)
        
        # Enlever les hashtags (mais garder le texte)
        text = re.sub(r'#(\w+)', r'\1', text)
        
        # Enlever les emojis
        text = self.emoji_pattern.sub('', text)
        
        # Enlever les caractères spéciaux (garder lettres et espaces)
        text = re.sub(r'[^\w\s]', '', text)
        
        # Enlever les espaces multiples
        text = re.sub(r'\s+', ' ', text)
        
        # Convertir en minuscules et nettoyer les espaces
        return text.lower().strip()
    
    def tokenize(self, text):
        """
        Découpe le texte en mots (tokens)
        
        Args:
            text (str): Texte à tokenizer
            
        Returns:
            list: Liste des tokens
        """
        return text.split()
    
    def extract_features(self, text):
        """
        Extrait des features basiques du texte
        
        Args:
            text (str): Texte nettoyé
            
        Returns:
            dict: Dictionnaire contenant les features
        """
        tokens = self.tokenize(text)
        
        if not tokens:
            return {
                'word_count': 0,
                'char_count': 0,
                'avg_word_length': 0,
                'stop_word_ratio': 0
            }
        
        # Calculer les features basiques
        word_count = len(tokens)
        char_count = len(text)
        avg_word_length = sum(len(token) for token in tokens) / word_count
        stop_words_count = sum(1 for token in tokens if token in self.stop_words)
        stop_word_ratio = stop_words_count / word_count if word_count > 0 else 0
        
        return {
            'word_count': word_count,
            'char_count': char_count,
            'avg_word_length': avg_word_length,
            'stop_word_ratio': stop_word_ratio
        }
    
    # ========================================================================
    # TODO-PERF1: Implémentez la méthode process_batch
    # ========================================================================
    # Cette méthode doit :
    # 1. Mesurer le temps de début avec time.time()
    # 2. Pour chaque tweet dans la liste 'tweets' :
    #    a. Le nettoyer avec self.clean_tweet()
    #    b. Extraire les features avec self.extract_features()
    #    c. Stocker le résultat dans une liste avec un dictionnaire contenant :
    #       - 'original': le tweet original
    #       - 'cleaned': le tweet nettoyé
    #       - 'features': les features extraites
    # 3. Calculer le temps total d'exécution
    # 4. Retourner un tuple : (liste_des_tweets_traités, temps_execution)
    #
    # Signature : process_batch(self, tweets) -> tuple
    # ========================================================================

    
    def process_batch(self, tweets):
        """
        Traite un batch de tweets et mesure le temps d'exécution
        
        Args:
            tweets (list): Liste de tweets (strings)
            
        Returns:
            tuple: (processed_tweets, execution_time)
                   - processed_tweets: liste de dictionnaires
                   - execution_time: temps en secondes
        """
        # À IMPLÉMENTER
        pass


# Code de test
if __name__ == "__main__":
    # Test rapide du preprocessing
    processor = TweetPreprocessor()
    
    test_tweets = [
        "Check out this amazing article! 😍 https://example.com #AI #MachineLearning",
        "@john_doe This is incredible! Thanks for sharing 🙏",
        "Just finished my Python project 💻 #coding #python"
    ]
    
    print("Test du module preprocessing:")
    print("-" * 60)
    
    for tweet in test_tweets:
        cleaned = processor.clean_tweet(tweet)
        features = processor.extract_features(cleaned)
        print(f"\nOriginal: {tweet}")
        print(f"Nettoyé:  {cleaned}")
        print(f"Features: {features}")
