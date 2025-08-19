#!/usr/bin/env python3
"""
Script de benchmark pour comparer les versions
TP1 - Programmation Parallèle
"""

import pandas as pd
import os
import sys
import time

# Import de la version de base
from preprocessing import TweetPreprocessor

# Import conditionnel de la version optimisée
try:
    from preprocessing_optimized import TweetPreprocessorOptimized
    optimized_available = True
except:
    optimized_available = False

def benchmark():
    """Compare les performances des deux versions"""
    
    print("=" * 70)
    print(" " * 20 + "BENCHMARK - Comparaison des versions")
    print("=" * 70)
    
    # Vérifier les données
    if not os.path.exists('data/tweets_medium.csv'):
        print("❌ Données non trouvées. Exécutez: python download_data.py")
        return 1
    
    # Charger les données
    df = pd.read_csv('data/tweets_medium.csv')
    tweets = df['text'].tolist()
    print(f"\n📊 Dataset: {len(tweets)} tweets")
    print("-" * 70)
    
    results = {}
    
    # Test version de base
    print("\n🐌 Version de base (non optimisée):")
    processor_base = TweetPreprocessor()
    
    try:
        processed_base, exec_time_base = processor_base.process_batch(tweets)
        if processed_base and exec_time_base:
            results['base'] = exec_time_base
            print(f"   • Temps total: {exec_time_base:.3f} secondes")
            print(f"   • Temps par tweet: {exec_time_base/len(tweets)*1000:.2f} ms")
            print(f"   • Tweets/seconde: {len(tweets)/exec_time_base:.0f}")
        else:
            print("   ❌ process_batch non implémenté (TODO-PERF1)")
    except:
        print("   ❌ Erreur dans process_batch")
    
    # Test version optimisée
    if optimized_available:
        print("\n⚡ Version optimisée:")
        processor_opt = TweetPreprocessorOptimized()
        
        try:
            # Vérifier que les méthodes sont implémentées
            test_tweet = "Test tweet with @mention and #hashtag 😊"
            cleaned = processor_opt.clean_tweet_optimized(test_tweet)
            
            if cleaned is None:
                print("   ❌ clean_tweet_optimized non implémenté (TODO-OPT1)")
            else:
                features = processor_opt.extract_features_optimized(cleaned)
                if features is None:
                    print("   ❌ extract_features_optimized non implémenté (TODO-OPT2)")
                else:
                    # Tester sur le dataset complet
                    processed_opt, exec_time_opt = processor_opt.process_batch_optimized(tweets)
                    results['optimized'] = exec_time_opt
                    
                    print(f"   • Temps total: {exec_time_opt:.3f} secondes")
                    print(f"   • Temps par tweet: {exec_time_opt/len(tweets)*1000:.2f} ms")
                    print(f"   • Tweets/seconde: {len(tweets)/exec_time_opt:.0f}")
        except Exception as e:
            print(f"   ❌ Erreur: {e}")
    else:
        print("\n⚡ Version optimisée: Non disponible")
    
    # Calcul du gain si les deux versions sont disponibles
    if 'base' in results and 'optimized' in results:
        speedup = results['base'] / results['optimized']
        improvement = (1 - results['optimized']/results['base']) * 100
        
        print("\n" + "=" * 70)
        print(" " * 25 + "📊 RÉSUMÉ")
        print("=" * 70)
        print(f"   🚀 Gain de performance: {speedup:.2f}x plus rapide")
        print(f"   📉 Réduction du temps: {improvement:.1f}%")
        print(f"   ⏱️  Temps économisé: {results['base']-results['optimized']:.2f} secondes")
        
        if speedup >= 2.5:
            print("\n   🏆 Excellent travail! Optimisation très efficace!")
        elif speedup >= 1.5:
            print("\n   ✅ Bon travail! Optimisation notable.")
        else:
            print("\n   💡 L'optimisation peut être améliorée.")
    
    print("\n" + "=" * 70)
    return 0

if __name__ == "__main__":
    sys.exit(benchmark())
