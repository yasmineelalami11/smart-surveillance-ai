
# Plateforme Smart Surveillance AI

Cette interface est une démonstration pour le projet :
**Système de Surveillance Intelligent basé sur YOLO, CNN et LSTM**

Elle permet de montrer au professeur une plateforme complète avec :
- Dashboard général
- Analyse vidéo simulée
- Gestion des alertes
- Liste des caméras
- Rapports et statistiques
- Paramètres IA

---

## 1. Installation sur PC

### Étape 1 : installer Python
Télécharger Python depuis le site officiel puis l’installer.

### Étape 2 : ouvrir le terminal dans le dossier du projet

### Étape 3 : installer les bibliothèques
```bash
pip install -r requirements.txt
```

### Étape 4 : lancer la plateforme
```bash
streamlit run app.py
```

Après l’exécution, une page web s’ouvre automatiquement dans le navigateur.

---

## 2. Exécution sur Google Colab

Dans une cellule Colab, écrire :

```python
!pip install streamlit pyngrok
```

Puis uploader les fichiers :
- app.py
- dataset_surveillance_sequences.csv

Ensuite lancer :

```python
!streamlit run app.py & npx localtunnel --port 8501
```

Colab va générer un lien public. Cliquer sur le lien pour ouvrir l’interface.

---

## 3. Explication à dire au professeur

Cette interface représente la partie plateforme de notre projet.  
Elle permet à un agent de sécurité de visualiser les caméras, lancer une analyse vidéo, consulter les alertes détectées et suivre les statistiques du système.

Même si le modèle YOLO, CNN et LSTM est développé dans Google Colab, cette interface montre comment notre solution peut être utilisée dans un vrai environnement professionnel.

La page Analyse vidéo simule le fonctionnement du modèle :
1. YOLO détecte les personnes.
2. CNN extrait les caractéristiques visuelles.
3. LSTM analyse le comportement dans le temps.
4. Le système affiche une décision finale : Normal ou Suspect.

---

## 4. Remarque importante

Cette version est une maquette fonctionnelle.  
Elle peut être connectée plus tard directement au modèle entraîné dans Google Colab.
