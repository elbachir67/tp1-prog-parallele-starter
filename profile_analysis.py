"""
Script de profiling pour identifier les goulots d'étranglement
TP1 - Programmation Parallèle
"""

import cProfile
import pstats
import pandas as pd
import os
from preprocessing import TweetPreprocessor

def profile_preprocessing():
    """
    Fonction principale pour profiler le preprocessing
    """
    
    # Vérifier que les données existent
    if not os.path.exists('data/tweets_medium.csv'):
        print("❌ Erreur: Fichier data/tweets_medium.csv non trouvé!")
        print("   Exécutez d'abord: python download_data.py")
        return
    
    # Charger les données
    print("📊 Chargement des données...")
    df = pd.read_csv('data/tweets_medium.csv')
    tweets = df['text'].tolist()
    print(f"   ✅ {len(tweets)} tweets chargés")
    
    # Créer le preprocessor
    processor = TweetPreprocessor()
    
    print("\n🔍 Lancement du profiling...")
    print("-" * 60)
    
    # ========================================================================
    # TODO-PROF1: Ajoutez le code de profiling avec cProfile
    # ========================================================================
    # Instructions :
    # 1. Créer un profiler avec : profiler = cProfile.Profile()
    # 2. Activer le profiling avec : profiler.enable()
    # 3. Exécuter le traitement : processor.process_batch(tweets)
    # 4. Désactiver le profiling : profiler.disable()
    # 5. Créer les statistiques : stats = pstats.Stats(profiler)
    # 6. Trier par temps cumulé : stats.sort_stats('cumulative')
    # 7. Afficher un titre : print("\n🔝 Top 10 fonctions les plus lentes:")
    # 8. Afficher les stats : stats.print_stats(10)
    # 9. Si possible, calculer et afficher :
    #    - Le temps total d'exécution
    #    - Le temps moyen par tweet
    # ========================================================================
    
    # À IMPLÉMENTER
    
    print("\n⚠️  TODO-PROF1 non implémenté")
    print("   Complétez le code de profiling dans profile_analysis.py")


if __name__ == "__main__":
    profile_preprocessing()
