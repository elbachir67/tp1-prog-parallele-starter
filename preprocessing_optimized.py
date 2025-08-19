"""
Version optimisée du module de préprocessing
TP1 - Programmation Parallèle
"""

import re
import time
import pandas as pd
from collections import Counter

class TweetPreprocessorOptimized:
    """
    Version optimisée du preprocessor avec regex pré-compilés
    """
    
    def __init__(self):
        """Initialise avec des regex pré-compilés pour la performance"""
        # Stop words (identiques à la version de base)
        self.stop_words = {
            'le', 'la', 'de', 'et', 'un', 'une', 'les', 'des',
            'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that',
            'is', 'it', 'for', 'on', 'with', 'as', 'was', 'are'
        }
        
        # PRÉ-COMPILATION des patterns regex (optimisation clé!)
        self.url_pattern = re.compile(r'http\S+|www.\S+')
        self.mention_pattern = re.compile(r'@\w+')
        self.hashtag_pattern = re.compile(r'#(\w+)')
        self.emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"
            u"\U0001F300-\U0001F5FF"
            u"\U0001F680-\U0001F6FF"
            u"\U0001F1E0-\U0001F1FF"
            "]+", flags=re.UNICODE)
        self.special_chars_pattern = re.compile(r'[^\w\s]')
        self.multiple_spaces_pattern = re.compile(r'\s+')
    
    # ========================================================================
    # TODO-OPT1: Optimisez la méthode clean_tweet_optimized
    # ========================================================================
    # Instructions :
    # 1. Utilisez les patterns pré-compilés (self.url_pattern, etc.)
    #    au lieu d'appeler re.sub() directement
    # 2. Syntaxe : self.url_pattern.sub('', text)
    # 3. Appliquez les substitutions dans cet ordre :
    #    - URLs (self.url_pattern)
    #    - Mentions (self.mention_pattern)
    #    - Hashtags (self.hashtag_pattern) - attention au groupe de capture
    #    - Emojis (self.emoji_pattern)
    #    - Caractères spéciaux (self.special_chars_pattern)
    #    - Espaces multiples (self.multiple_spaces_pattern)
    # 4. Ne faites la conversion en minuscules qu'une seule fois à la fin
    # ========================================================================
    
    def clean_tweet_optimized(self, text):
        """
        Version optimisée du nettoyage de tweet
        
        Args:
            text (str): Texte à nettoyer
            
        Returns:
            str: Texte nettoyé
        """
        # À IMPLÉMENTER
        # Utilisez les patterns pré-compilés pour optimiser
        pass
    
    def tokenize_fast(self, text):
        """Tokenisation rapide (déjà optimisée)"""
        return text.split()
    
    # ========================================================================
    # TODO-OPT2: Optimisez extract_features_optimized
    # ========================================================================
    # Instructions :
    # 1. Tokenisez une seule fois au début avec self.tokenize_fast()
    # 2. Évitez de parcourir les tokens plusieurs fois
    # 3. Calculez toutes les features en un seul parcours si possible :
    #    - word_count = len(tokens)
    #    - char_count = len(text)
    #    - Pour avg_word_length et stop_word_ratio, utilisez une seule boucle
    # 4. Utilisez une compréhension de liste pour compter les stop words :
    #    stop_count = sum(1 for token in tokens if token in self.stop_words)
    # ========================================================================
    
    def extract_features_optimized(self, text):
        """
        Version optimisée de l'extraction de features
        
        Args:
            text (str): Texte nettoyé
            
        Returns:
            dict: Features extraites
        """
        # À IMPLÉMENTER
        # Optimisez les calculs pour éviter les parcours multiples
        pass
    
    def process_batch_optimized(self, tweets):
        """
        Version optimisée du traitement par batch
        Utilise les méthodes optimisées
        """
        start_time = time.time()
        processed = []
        
        for tweet in tweets:
            # Utiliser les méthodes optimisées
            cleaned = self.clean_tweet_optimized(tweet)
            features = self.extract_features_optimized(cleaned)
            
            processed.append({
                'original': tweet,
                'cleaned': cleaned,
                'features': features
            })
        
        execution_time = time.time() - start_time
        return processed, execution_time


# Test de la version optimisée
if __name__ == "__main__":
    processor = TweetPreprocessorOptimized()
    
    test_tweets = [
        "Check out this amazing article! 😍 https://example.com #AI #MachineLearning",
        "@john_doe This is incredible! Thanks for sharing 🙏",
        "Just finished my Python project 💻 #coding #python"
    ]
    
    print("Test de la version optimisée:")
    print("-" * 60)
    
    # Tester seulement si les méthodes sont implémentées
    try:
        for tweet in test_tweets:
            cleaned = processor.clean_tweet_optimized(tweet)
            if cleaned:  # Si la méthode retourne quelque chose
                features = processor.extract_features_optimized(cleaned)
                print(f"\nOriginal: {tweet}")
                print(f"Nettoyé:  {cleaned}")
                print(f"Features: {features}")
    except:
        print("\n⚠️  Méthodes optimisées non implémentées")
        print("   Complétez TODO-OPT1 et TODO-OPT2")
