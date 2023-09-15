#################################################################################################
# FONCTIONS SPECIFIQUES
#------------------------------------------------------------------------------------------------
# Les fonctions à coder selon l'échancier donné dans le document SAE15-Présentation.ipynb
#################################################################################################

#------------------------------------------------------------------------------------------------
# importations des modules utiles
#
# attention : geopandas et contextily doivent être installés avant l'importation
# utiliser pour cela !pip install ... dans le Notebook principal
#
import pandas as pd             # pour la mise en forme, l'analyse et la publication
import datetime as dt           # pour la détermination de la date
import geopandas as gpd         # pour la spatialisation des données
import matplotlib.pyplot as plt # pour les graphes
import contextily as ctx        # pour l'utilisation de cartes géographiques

#------------------------------------------------------------------------------------------------
# fonction qui retourne le taux de disponibilité des stands (en %)
def availableDocksRate(stations_df) :

  # votre code...

  return rate

#------------------------------------------------------------------------------------------------
# fonction qui retourne le taux de disponibilité des vélos (en %)
def availableBikesRate(stations_df) :

  # votre code...

  return rate

#------------------------------------------------------------------------------------------------
# fonction qui retourne la date la plus récente de la mise à jour des données dynamiques
def getLatestDate(stations_df) :

  # votre code...

  return date

#------------------------------------------------------------------------------------------------
# fonction qui retourne les mesures statistiques  d'une clé du DataFrame de stations
def stationStatistics(stations_df_key) :

  # calcul des mesures statistiques
  # votre code...

  # créaton d'un DataFrame des mesures statistiques avec le nom de la clé passée à la fonction
  # votre code...

  return stats

#------------------------------------------------------------------------------------------------
# fonction qui exporte au format HTML le DataFrame des mesures statistiques
def exportStatistics(stats_df, filename) :

  # votre code...

  return

#------------------------------------------------------------------------------------------------
# fonction qui affiche et exporte la carte des stations Vélibs géolocalisées
def exportCityMap(geo_stations, marker_size, marker_color, title, date=None, filename=None) :
  # figure et axes
  # votre code...

  # conversion des coordonnées dans le système approprié
  # votre code...
  
  # affichage en fonction des variables passées en argument
  # votre code...

  # effacement des axes gradués
  # votre code...

  # ajout du fond de carte correspondant aux coordonnées géographiques des stations
  # votre code...

  # affichage du titre avec la date de mise à jour
  # votre code...

  # sauvegarde de la carte sur le Drive
  # votre code...
  
  # affichage forçé
  # votre code...

  return 

