#!/usr/bin/env python3
"""
Script de validation automatique du TP
Vérifie que tous les TODOs sont correctement implémentés
"""

import sys
import os
import importlib
import pandas as pd

# Couleurs pour l'affichage
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_test(name, passed, message=""):
    """Affiche le résultat d'un test"""
    if passed:
        print(f"{GREEN}✅ {name}{RESET}")
        if message:
            print(f"   {message}")
    else:
        print(f"{RED}❌ {name}{RESET}")
        if message:
            print(f"   {message}")

def validate_todo_perf1():
    """Valide TODO-PERF1: process_batch"""
    print(f"\n{BLUE}Validation TODO-PERF1: Méthode process_batch{RESET}")
    
    try:
        from preprocessing import TweetPreprocessor
        processor = TweetPreprocessor()
        
        # Test avec quelques tweets
        test_tweets = [
            "This is a test tweet @user #test",
            "Another tweet with URL https://test.com 😊"
        ]
        
        result = processor.process_batch(test_tweets)
        
        # Vérifications
        if result is None:
            print_test("TODO-PERF1", False, "La méthode retourne None")
            return False
        
        if not isinstance(result, tuple):
            print_test("TODO-PERF1", False, "Doit retourner un tuple")
            return False
        
        if len(result) != 2:
            print_test("TODO-PERF1", False, "Le tuple doit contenir 2 éléments")
            return False
        
        processed, exec_time = result
        
        if not isinstance(processed, list):
            print_test("TODO-PERF1", False, "Le premier élément doit être une liste")
            return False
        
        if not isinstance(exec_time, (int, float)):
            print_test("TODO-PERF1", False, "Le temps doit être un nombre")
            return False
        
        if len(processed) != len(test_tweets):
            print_test("TODO-PERF1", False, "Nombre de tweets traités incorrect")
            return False
        
        # Vérifier la structure des tweets traités
        for item in processed:
            if not isinstance(item, dict):
                print_test("TODO-PERF1", False, "Chaque tweet traité doit être un dict")
                return False
            
            required_keys = {'original', 'cleaned', 'features'}
            if not required_keys.issubset(item.keys()):
                print_test("TODO-PERF1", False, f"Clés manquantes: {required_keys - item.keys()}")
                return False
        
        print_test("TODO-PERF1", True, f"Correctement implémenté ({exec_time:.3f}s pour {len(test_tweets)} tweets)")
        return True
        
    except ImportError as e:
        print_test("TODO-PERF1", False, f"Erreur d'import: {e}")
        return False
    except Exception as e:
        print_test("TODO-PERF1", False, f"Erreur: {e}")
        return False

def validate_todo_prof1():
    """Valide TODO-PROF1: Profiling"""
    print(f"\n{BLUE}Validation TODO-PROF1: Code de profiling{RESET}")
    
    # Vérifier que le fichier contient les éléments de profiling
    try:
        with open('profile_analysis.py', 'r') as f:
            content = f.read()
        
        required_elements = [
            'cProfile.Profile()',
            'profiler.enable()',
            'profiler.disable()',
            'pstats.Stats',
            'sort_stats',
            'print_stats'
        ]
        
        missing = []
        for element in required_elements:
            if element not in content:
                missing.append(element)
        
        if missing:
            print_test("TODO-PROF1", False, f"Éléments manquants: {', '.join(missing)}")
            return False
        
        print_test("TODO-PROF1", True, "Code de profiling présent")
        return True
        
    except Exception as e:
        print_test("TODO-PROF1", False, f"Erreur: {e}")
        return False

def validate_todo_opt1():
    """Valide TODO-OPT1: clean_tweet_optimized"""
    print(f"\n{BLUE}Validation TODO-OPT1: Méthode clean_tweet_optimized{RESET}")
    
    try:
        from preprocessing_optimized import TweetPreprocessorOptimized
        processor = TweetPreprocessorOptimized()
        
        # Test de nettoyage
        test_tweet = "Check this out! 😍 @user https://test.com #amazing"
        result = processor.clean_tweet_optimized(test_tweet)
        
        if result is None:
            print_test("TODO-OPT1", False, "La méthode retourne None")
            return False
        
        # Vérifier que les éléments sont bien supprimés
        checks = [
            ('😍' not in result, "Emojis non supprimés"),
            ('@user' not in result.lower(), "Mentions non supprimées"),
            ('https' not in result.lower(), "URLs non supprimées"),
            (result.islower() or not result, "Texte non converti en minuscules")
        ]
        
        for check, message in checks:
            if not check:
                print_test("TODO-OPT1", False, message)
                return False
        
        print_test("TODO-OPT1", True, f"Nettoyage correct: '{result}'")
        return True
        
    except AttributeError:
        print_test("TODO-OPT1", False, "Méthode clean_tweet_optimized non trouvée")
        return False
    except Exception as e:
        print_test("TODO-OPT1", False, f"Erreur: {e}")
        return False

def validate_todo_opt2():
    """Valide TODO-OPT2: extract_features_optimized"""
    print(f"\n{BLUE}Validation TODO-OPT2: Méthode extract_features_optimized{RESET}")
    
    try:
        from preprocessing_optimized import TweetPreprocessorOptimized
        processor = TweetPreprocessorOptimized()
        
        # Test d'extraction de features
        test_text = "this is a test text with some words"
        result = processor.extract_features_optimized(test_text)
        
        if result is None:
            print_test("TODO-OPT2", False, "La méthode retourne None")
            return False
        
        if not isinstance(result, dict):
            print_test("TODO-OPT2", False, "Doit retourner un dictionnaire")
            return False
        
        # Vérifier les clés requises
        required_keys = {'word_count', 'char_count', 'avg_word_length', 'stop_word_ratio'}
        missing_keys = required_keys - set(result.keys())
        
        if missing_keys:
            print_test("TODO-OPT2", False, f"Clés manquantes: {missing_keys}")
            return False
        
        # Vérifier la cohérence des valeurs
        words = test_text.split()
        expected_word_count = len(words)
        
        if result['word_count'] != expected_word_count:
            print_test("TODO-OPT2", False, f"word_count incorrect: {result['word_count']} != {expected_word_count}")
            return False
        
        print_test("TODO-OPT2", True, "Extraction de features correcte")
        return True
        
    except AttributeError:
        print_test("TODO-OPT2", False, "Méthode extract_features_optimized non trouvée")
        return False
    except Exception as e:
        print_test("TODO-OPT2", False, f"Erreur: {e}")
        return False

def main():
    """Fonction principale de validation"""
    print("=" * 60)
    print(" " * 15 + "VALIDATION AUTOMATIQUE DU TP1")
    print("=" * 60)
    
    # Vérifier que les données existent
    if not os.path.exists('data/tweets_small.csv'):
        print(f"\n{RED}⚠️  Données non trouvées!{RESET}")
        print("   Exécutez d'abord: python download_data.py")
        return 1
    
    # Valider chaque TODO
    results = {
        'TODO-PERF1': validate_todo_perf1(),
        'TODO-PROF1': validate_todo_prof1(),
        'TODO-OPT1': validate_todo_opt1(),
        'TODO-OPT2': validate_todo_opt2()
    }
    
    # Résumé
    print("\n" + "=" * 60)
    print(" " * 25 + "RÉSUMÉ")
    print("=" * 60)
    
    completed = sum(results.values())
    total = len(results)
    percentage = (completed / total) * 100
    
    for todo, passed in results.items():
        status = f"{GREEN}✅{RESET}" if passed else f"{RED}❌{RESET}"
        print(f"   {status} {todo}")
    
    print(f"\n   Score: {completed}/{total} ({percentage:.0f}%)")
    
    if completed == total:
        print(f"\n   {GREEN}🎉 Félicitations! TP complété avec succès!{RESET}")
        print(f"   Lancez 'python benchmark.py' pour voir les gains de performance")
        return 0
    else:
        remaining = total - completed
        print(f"\n   {YELLOW}📝 Il reste {remaining} TODO(s) à compléter{RESET}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
