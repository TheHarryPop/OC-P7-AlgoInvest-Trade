# AlgoInvest-Trade

Cette application Python permet d'afficher les meilleurs investissements parmi une liste donnée d'actions

## Installation et lancement de l'application

### Installation

Étape à effectuer une seule fois :

```bash
$ git clone https://github.com/TheHarryPop/OC-P7-AlgoInvest-Trade.git
$ cd OC-P7-AlgoInvest-Trade
$ python3 -m venv env (Sous Windows => python -m venv env)
$ source env/bin/activate (Sous Windows => env\Scripts\activate)
$ pip install -r requirements.txt
```

### Lancement

Activez l'environnement avant de lancer les commandes suivantes.

Pour lancer le fichier bruteforce.py :

```bash
$ python bruteforce.py
```

Pour lancer le fichier optimized.py :

```bash
$ python optimized.py
```

## Usage

Le fichier bruteforce.py traite un .csv contenant 20 actions et nous retourne une liste d'actions ne 
dépassant pas un coût de 500€ pour un maximum de rentabilité

Le fichier optimized.py traite d'une part le .csv contenant 20 actions en un temps réduit, et d'autre part deux autres 
.csv contenant 1000 actions. Le résultat sera également une liste d'actions ne dépassant pas un coût de 500€ pour 
un maximum de rentabilité