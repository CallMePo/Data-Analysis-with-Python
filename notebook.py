import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
games=pd.read_csv('D:\Data Visualization\games.csv')
sns.regplot(games[games['playingtime']<500], x='playingtime',y='average_rating')
plt.show()