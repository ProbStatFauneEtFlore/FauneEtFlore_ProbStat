# 📘 Cahier des charges – Projet de Probabilités et Statistiques

**Superviseurs :** Cédric Travelletti et Florian Desmons  
**Année académique :** 2025–2026  

---

## 🧭 Titre du sujet
### *Analyse de la faune et de la flore en Suisse*

**Groupe :**
- Axel Hall  
- Jonathan Müller  
- Fatima Anougmar  
- Sebastian Morsch  

---

## 🎯 Définition de la problématique

> **Question centrale :**  
> *La modélisation de la dynamique d’une espèce permet-elle de prédire son évolution au sein de son écosystème ?*

L’objectif est d’analyser les interactions entre espèces animales et végétales présentes sur le territoire suisse.

---

## 🧩 Explication des données obtenues ou à collecter

**Source principale :** [iNaturalist.org](https://www.inaturalist.org/pages/api+reference)  
**Jeu de données :** `observations_swiss.csv` et API publique.

### Données disponibles
- Identifiant de l’observation  
- Identifiant de l’observateur  
- Latitude / Longitude  
- Précision positionnelle  
- Identifiant de l’espèce (taxon)  
- Niveau de l’observation (amateur, recherche)  
- Date de l’observation  

### Pré-traitement
- Nettoyage des observations incomplètes  
- Normalisation temporelle  
- Ajout d’informations supplémentaires via l’API  

---

## 🎓 Objectifs du projet

### 🌳 Visualisation en arbre des espèces
**But :** Mettre en évidence des paires d’espèces fréquemment co-observées.  
**Concepts :** Co-occurrence  
**Sources :** Longitude, latitude, taxon, date  
**Exemple de visualisation :** [Voir un exemple](https://app.vosviewer.com/?json=https%3A%2F%2Fapp.vosviewer.com%2Fdata%2FScientometrics_term_co-occurrence_network.json)

---

### 🗺️ Cartographie des écosystèmes en Suisse
**But :** Identifier des groupements spatiaux d’espèces et esquisser des écosystèmes types.  
**Concepts :** Clustering, typage d’écosystèmes, interpolation spatiale  
**Sources :** Longitude, latitude, taxon, date  
**Sortie :** Groupes représentant des écosystèmes

---

### 🔄 Tendances d’évolution d’une espèce
**But :** Estimer la probabilité d’occurrence d’une espèce cible selon la composition locale.  
**Concepts :** Tendances, facteurs de corrélation, graphes  
**Sources :** Groupes d’écosystèmes  
**Sortie :** Tendances, graphe pondéré des corrélations

---

### 📅 Évolution annuelle des espèces
**But :** Quantifier les tendances annuelles des populations.  
**Concepts :** Régression, interpolation  
**Sources :** Taxon, date  
**Sortie :** Courbe d’évolution annuelle des populations

---

### 🌦️ Évolution saisonnière des espèces
**But :** Quantifier les tendances saisonnières des populations.  
**Concepts :** Régression, interpolation  
**Sources :** Taxon, date  
**Sortie :** Courbe d’évolution saisonnière des populations

---

## 👥 Répartition du travail

| Membre | Rôle principal | Responsabilités |
|:--|:--|:--|
| **Sebastian Morsch** | Visualisation de la DATA | Représentation claire, création d’outils de visualisation (graphes, heatmaps, PyQT) |
| **Axel Hall** | Cartographie des écosystèmes | Distinction des espèces par zones, clustering spatial, production des cartes (hotspots, clusters) |
| **Jonathan Müller** | Évolution temporelle | Analyse des séries temporelles, détection de tendances, visualisations temporelles |
| **Fatima Anougmar** | Pré-traitement et modélisation | Nettoyage et normalisation des données, interprétation des résultats |

---

## 💡 Réflexion sur les résultats attendus

Nous anticipons :  
- Une variation saisonnière importante, en particulier pour les espèces migratrices et florales.  
- Des associations récurrentes entre certaines espèces animales et végétales.  
- Une diversité plus élevée dans les zones naturelles, mise en évidence par le clustering des écosystèmes.

---
