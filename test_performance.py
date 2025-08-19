#!/usr/bin/env python3
"""
Script de test des performances
TP1 - Programmation Parallèle
"""

import argparse
import pandas as pd
import os
import sys
from preprocessing import TweetPreprocessor

def test_performance(size='small'):
    """
    Teste les performances du preprocessing
    
    Args:
        size: 'small' (100), 'medium' (1000), ou 'large' (10000) tweets
    """
    
    # Déterminer le fichier à utiliser
    filename = f'data/tweets_{size}.csv'
    
    # Vérifier que le fichier existe
    if not os.path.exists(filename):
        print(f"❌ Erreur: {filename} non trouvé!")
        print("   Exécutez d'abord: python download_data.py")
        return 1
    
    # Charger les données
    print(f"📊 Chargement de {filename}...")
    df = pd.read_csv(filename)
    tweets = df['text'].tolist()
    
    print(f"\n🚀 Test de performance sur {len(tweets)} tweets")
    print("=" * 60)
    
    # Créer le preprocessor
    processor = TweetPreprocessor()
    
    # Tester si process_batch est implémenté
    try:
        processed, exec_time = processor.process_batch(tweets)
        
        if processed is None or exec_time is None:
            print("❌ process_batch retourne None")
            print("   Vérifiez votre implémentation de TODO-PERF1")
            return 1
        
        # Afficher les résultats
        print(f"\n📈 Résultats:")
        print(f"   • Temps total: {exec_time:.3f} secondes")
        print(f"   • Temps par tweet: {exec_time/len(tweets)*1000:.2f} ms")
        print(f"   • Tweets par seconde: {len(tweets)/exec_time:.0f}")
        
        # Afficher quelques exemples
        print(f"\n📝 Exemples de tweets traités:")
        for i in range(min(3, len(processed))):
            print(f"\n   Tweet {i+1}:")
            print(f"   Original: {processed[i]['original'][:80]}...")
            print(f"   Nettoyé:  {processed[i]['cleaned'][:80]}...")
            print(f"   Features: {processed[i]['features']}")
        
        return 0
        
    except TypeError as e:
        print(f"❌ Erreur: process_batch n'est pas correctement implémenté")
        print(f"   {e}")
        print("\n💡 Complétez TODO-PERF1 dans preprocessing.py")
        return 1
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test de performance du preprocessing')
    parser.add_argument(
        '--size',
        choices=['small', 'medium', 'large'],
        default='small',
        help='Taille du dataset à utiliser'
    )
    
    args = parser.parse_args()
    sys.exit(test_performance(args.size))
