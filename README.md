# TP1 - Programmation Parallèle : Préprocessing de données textuelles 🚀

## 📋 Description

Ce TP vous introduit aux concepts fondamentaux de la programmation parallèle à travers l'optimisation d'un module de préprocessing de tweets. Vous apprendrez à mesurer, profiler et optimiser du code séquentiel - étapes essentielles avant toute parallélisation.

## 🎯 Objectifs

- ✅ Mesurer les performances d'un programme Python
- ✅ Identifier les goulots d'étranglement avec le profiling
- ✅ Optimiser le code séquentiel (regex, calculs)
- ✅ Comprendre l'importance de l'optimisation avant parallélisation

## 📁 Structure du projet

```
tp1-prog-parallele/
├── preprocessing.py              # Module principal (TODO-PERF1)
├── profile_analysis.py           # Script de profiling (TODO-PROF1)
├── preprocessing_optimized.py    # Version optimisée (TODO-OPT1, TODO-OPT2)
├── test_performance.py          # Tests de performance
├── benchmark.py                 # Comparaison des versions
├── validate_tp.py               # Validation automatique
├── download_data.py             # Téléchargement des données
├── data/                        # Datasets
│   ├── tweets_small.csv        # 100 tweets
│   ├── tweets_medium.csv       # 1,000 tweets
│   └── tweets_large.csv        # 10,000 tweets
└── README.md                    # Ce fichier

```

## 🚀 Installation

```bash
# 1. Installation des dépendances
pip install pandas

# 2. Si les données n'existent pas
python download_data.py
```

## 📝 TODOs à compléter

### TODO-PERF1 : Mesure de performance
**Fichier** : `preprocessing.py` (ligne ~130)  
**Objectif** : Implémenter `process_batch()` pour traiter les tweets et mesurer le temps

### TODO-PROF1 : Profiling  
**Fichier** : `profile_analysis.py` (ligne ~30)  
**Objectif** : Ajouter le code de profiling avec cProfile

### TODO-OPT1 : Optimisation du nettoyage
**Fichier** : `preprocessing_optimized.py` (ligne ~50)  
**Objectif** : Utiliser les regex pré-compilés

### TODO-OPT2 : Optimisation des features
**Fichier** : `preprocessing_optimized.py` (ligne ~80)  
**Objectif** : Optimiser les calculs de features

## 🧪 Tests et validation

```bash
# Tester les performances
python test_performance.py --size small

# Profiler le code
python profile_analysis.py

# Comparer les versions
python benchmark.py

# Valider le TP
python validate_tp.py
```

## 📊 Résultats attendus

| Version | Temps (1000 tweets) | Amélioration |
|---------|-------------------|--------------|
| Base | ~2-3 secondes | - |
| Optimisée | ~0.6-0.8 secondes | **3-4x plus rapide** |

## 💡 Conseils

1. **Commencez par TODO-PERF1** - Sans mesure, pas d'optimisation
2. **Utilisez le profiling** - Les goulots ne sont pas toujours évidents
3. **Pré-compilez les regex** - Gain de performance majeur
4. **Testez régulièrement** - `python validate_tp.py`

## 🎓 Contexte académique

**Cours** : Programmation Parallèle  
**Établissement** : UCAD - FST/DMI  
**Enseignant** : Dr. El Hadji Bassirou TOURE  
**Année** : 2024-2025

---

💪 **Bon courage et bon TP !**
