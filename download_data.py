#!/usr/bin/env python3
"""
Télécharge et prépare le dataset Sentiment140 pour le TP
"""

import os
import sys
import pandas as pd
import urllib.request
import random

def download_sentiment140_sample():
    """Télécharge un échantillon du dataset Sentiment140"""
    
    print("📥 Téléchargement du dataset Sentiment140 (échantillon)...")
    
    # URL publique d'un échantillon de Sentiment140
    urls = [
        "https://raw.githubusercontent.com/vineetdhanawat/twitter-sentiment-analysis/master/datasets/Sentiment%20Analysis%20Dataset.csv",
        "https://raw.githubusercontent.com/Vasistareddy/sentiment_analysis/master/data/tweet.csv"
    ]
    
    for url in urls:
        try:
            # Télécharger le fichier
            urllib.request.urlretrieve(url, "data/temp_tweets.csv")
            
            # Charger et nettoyer
            df = pd.read_csv("data/temp_tweets.csv", error_bad_lines=False, nrows=50000)
            
            # Identifier la colonne de texte
            text_col = None
            for col in ['text', 'tweet', 'SentimentText', 'Text']:
                if col in df.columns:
                    text_col = col
                    break
            
            if text_col:
                df = df[[text_col]].rename(columns={text_col: 'text'})
                df = df[df['text'].notna()]
                df = df[df['text'].str.len() > 30]
                
                if len(df) > 100:
                    print(f"✅ {len(df)} tweets téléchargés avec succès")
                    return df
                    
        except Exception as e:
            print(f"⚠️  Échec avec {url}: {e}")
            continue
    
    # Si échec, générer des tweets
    print("⚠️  Téléchargement échoué, génération de tweets synthétiques...")
    return generate_fallback_tweets()

def generate_fallback_tweets():
    """Génère des tweets synthétiques si le téléchargement échoue"""
    
    templates = [
        "Just watched {} and it was {} ! 😍 #{} #movies",
        "Can't believe {} is happening {} ! This is {} 🤯",
        "@{} Thanks for {} ! Really {} experience 🙏 #{}",
        "Working on {} today. {} is harder than expected 😅 #coding",
        "New {} just dropped! {} looks {} 🔥 Check it out: http://bit.ly/{}",
        "Why is {} so {} ? Someone explain {} to me please 🤔",
        "{} weather today! Perfect for {} ☀️ #{} #{}",
        "Finally finished {} ! Took {} hours but worth it 💪 #{}",
        "RT @{}: {} is the future of {} ! {} #innovation",
        "Unpopular opinion: {} is overrated. {} is much better IMO 🤷"
    ]
    
    words = ['amazing', 'terrible', 'awesome', 'crazy', 'unbelievable', 'fantastic',
             'Python', 'coding', 'AI', 'machine learning', 'data science', 'web dev',
             'coffee', 'pizza', 'music', 'sports', 'gaming', 'travel', 'food',
             'happy', 'sad', 'excited', 'tired', 'motivated', 'inspired']
    
    tweets = []
    for _ in range(10000):
        template = random.choice(templates)
        count = template.count('{}')
        values = [random.choice(words) for _ in range(count)]
        tweet = template.format(*values)
        tweets.append(tweet)
    
    return pd.DataFrame({'text': tweets})

def prepare_datasets(df):
    """Prépare les datasets de différentes tailles"""
    
    print("\n📊 Préparation des datasets...")
    
    # Small (100 tweets)
    df_small = df.sample(n=min(100, len(df)), random_state=42)
    df_small.to_csv('data/tweets_small.csv', index=False)
    print(f"   ✅ data/tweets_small.csv : 100 tweets")
    
    # Medium (1000 tweets)
    n_medium = min(1000, len(df))
    df_medium = df.sample(n=n_medium, random_state=42)
    df_medium.to_csv('data/tweets_medium.csv', index=False)
    print(f"   ✅ data/tweets_medium.csv : {n_medium} tweets")
    
    # Large (10000 tweets)
    n_large = min(10000, len(df))
    df_large = df.sample(n=n_large, random_state=42)
    df_large.to_csv('data/tweets_large.csv', index=False)
    print(f"   ✅ data/tweets_large.csv : {n_large} tweets")
    
    # Statistiques
    print("\n📈 Statistiques des tweets:")
    lengths = df_small['text'].str.len()
    print(f"   • Longueur moyenne: {lengths.mean():.1f} caractères")
    print(f"   • Min/Max: {lengths.min()}/{lengths.max()} caractères")
    
    # Exemples
    print("\n📝 Exemples de tweets:")
    for i, tweet in enumerate(df_small['text'].head(3), 1):
        print(f"\n   {i}. {tweet[:100]}{'...' if len(tweet) > 100 else ''}")

if __name__ == "__main__":
    random.seed(42)  # Reproductibilité
    
    # Créer le dossier data
    os.makedirs('data', exist_ok=True)
    
    # Télécharger ou générer les données
    df = download_sentiment140_sample()
    
    # Préparer les datasets
    prepare_datasets(df)
    
    print("\n✅ Données prêtes pour le TP!")
