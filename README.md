# 🧠 Analyse de la faune et de la flore en Suisse

**Projet de Probabilités et Statistiques – 2025–2026**  
Auteurs : *Sebastian Morsch*, *Axel Hall*, *Jonathan Müller*, *Fatima Anougmar*

---

## 🌍 Description du projet

Ce projet vise à **analyser les interactions entre les espèces animales et végétales présentes en Suisse**, à partir de données d’observation issues de la plateforme [iNaturalist.org](https://www.inaturalist.org/pages/api+reference).

> **Problématique :**  
> *La modélisation de la dynamique d’une espèce permet-elle de prédire son évolution au sein de son écosystème ?*

Le travail consiste à :
- Nettoyer et structurer les données d’observations.
- Identifier des **groupements écologiques** cohérents à travers la Suisse.
- Mettre en évidence des **co-occurrences** entre espèces.
- Étudier les **tendances d’évolution** temporelles et saisonnières des populations.

---

## 📊 Données utilisées

Les données proviennent de la plateforme **iNaturalist**, via :
- Le jeu de données `observations_swiss.csv`
- Des appels complémentaires à leur **API publique**

### Champs principaux :
- `observation_id`  
- `observer_id`  
- `latitude`, `longitude`  
- `precision`  
- `taxon_id` (identifiant de l’espèce)  
- `grade` (niveau de validation : amateur ou recherche)  
- `observed_on` (date de l’observation)

### Prétraitement :
1. Nettoyage des entrées incomplètes  
2. Normalisation temporelle  
3. Enrichissement des observations via l’API  

---

## ⚙️ Script d’analyse : `data_infos.py`

Le fichier [`data_infos.py`](./data_infos.py) permet d’extraire des statistiques essentielles à partir du fichier CSV.

### 🎯 Objectif du script
Calculer, pour chaque année :
- Le **nombre total d’observations**
- Le **nombre d’espèces distinctes observées**
- Le **nombre d’observateurs uniques**

### 📦 Dépendances
Aucune dépendance externe (utilise uniquement la bibliothèque standard Python 3).

### 🚀 Utilisation

```bash
python data_infos.py --csv observations_swiss.csv --out results.csv
```

## Project structure

```
.
├── data_infos.py
├── observations_swiss.csv
├── Project_goal.txt
├── README.md
└── julia_files/
	└── blank.jl
```
