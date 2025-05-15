# Script de conversion WhatsApp TXT vers CSV et Excel

Ce script Python permet de convertir automatiquement un fichier texte exporté depuis WhatsApp (`chat.txt`) en deux formats :
- CSV (`chat.csv`)
- Excel (`chat.xlsx`)

## Fonctionnalités
- Extraction automatique de la date, l'heure, l'auteur (si présent) et le message.
- Gestion des messages sur plusieurs lignes.
- Export CSV et Excel prêts à l'emploi.

## Prérequis
- Python 3.x
- Bibliothèques : `pandas`, `openpyxl` (pour l'export Excel)

## Installation des dépendances

```bash
pip install pandas openpyxl
```

## Utilisation
1. Placez votre fichier `chat.txt` (export WhatsApp) dans le même dossier que le script `main.py`.
2. Exécutez le script :
   ```bash
   python main.py
   ```
3. Les fichiers `chat.csv` et `chat.xlsx` seront générés dans le même dossier.

## Structure du CSV/Excel
Chaque ligne contient :
- **date** : Date du message (ex : 17/12/20)
- **time** : Heure du message (ex : 9:27 am)
- **author** : Auteur du message (vide pour les messages système)
- **message** : Contenu du message (texte, liens, notifications, etc.)

## Exemple de sortie
| date      | time    | author                  | message                       |
|-----------|---------|-------------------------|-------------------------------|
| 17/12/20  | 9:27 am |                         | You were added                |
| 10/11/21  | 1:42 pm | Mme AMIA THIERYY        | <Media omitted>               |
| 16/11/21  | 8:33 am | Mme AMIA THIERYY        | Bonjour à tous ...            |

## Remarques
- Le script gère les messages sur plusieurs lignes.
- Les fichiers médias ou pièces jointes sont signalés dans le texte (ex : `<Media omitted>`).

## Auteur
R4GAMIA