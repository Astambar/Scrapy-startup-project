# Démarrage projet Srapy basique scrapy-startup-project
Ce projet peut être utilisé pour commencer un projet Scrapy de zéro. Il est à visée éducative où l'on apprend à extraire des informations de ce site : http://quotes.toscrape.com/

# Installation et prérequis
1. Cloner ce projet
2. Créer un en environnement virtuel Python : `python -m venv ven`
3. Activer l'environnement virtuel Python : `source venv/bin/activate` sous Linux ; `.\venv\Scripts\activate` sous Windows
4. Installer Scrapy avec pip : `pip install scrapy`
5. Entrer dans le dossier du projet : `cd scrapy-startup-project`
6. Lister les 'spiders' du projet Scrapy : `scrapy list`
6. Vous pouvez désormais exécuter le programme scrapy  : `scrapy crawl quotes`