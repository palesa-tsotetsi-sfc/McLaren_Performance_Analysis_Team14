#Winning Factor 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# ML
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

print('Improt Done')

results = pd.read_csv("RESULTS.csv")
races = pd.read_csv("RACES.csv")
drivers = pd.read_csv("DRIVERS.csv")
constructors = pd.read_csv("CONSTRUCTORS.csv")
qualifying = pd.read_csv("QUALIFYING.csv")
status = pd.read_csv("STATUS.csv")
pit_stops = pd.read_csv("PIT_STOPS.csv")
lap_times = pd.read_csv("LAP_TIMES.csv")

print('Load Done')


# dataframe =[]
# Binary classification: Did Mercedes win the race?
# df['mercedes_win'] = ((df['constructor'] == 'Mercedes') & (df['positionOrder'] == 1)).astype(int)
