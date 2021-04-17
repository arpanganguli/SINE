# import packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from matplotlib.pylab import rcParams

# import files into a data frame

df = pd.read_csv("/Users/arpanganguli/Documents/Professional/Projects/SINE/Database/Time_Series/Macroeconomic_Aggregates.csv", thousands=",")
df.set_index('Year', inplace=True)
df.sort_index(ascending=True, inplace=True)
print(df.head())

# plot figures

fig, ax = plt.subplots(3, 2)
fig.suptitle("Macroeconomic Indicators at constant prices (Base year: 2011-12)", verticalalignment="top", fontsize=28, fontweight="bold")

sns.barplot(x= df.index, y=df['Gross Domestic Product'], color="darkblue", ax=ax[0,0])
ax[0,0].set_title('Gross Domestic Product (at constant prices) \nBase year: 2011-12', fontsize=20, fontweight='bold')
ax[0,0].set_xlabel("Years", fontsize=8, fontweight='bold')
ax[0,0].set_ylabel("Amount (Rupees Crore)", fontsize=8, fontweight='bold')
ax[0,0].xaxis.set_major_locator(ticker.MultipleLocator(5))

sns.barplot(x= df.index, y=df['Net Domestic Product'], color="darkblue", ax=ax[0,1])
ax[0,1].set_title('Net Domestic Product (at constant prices) \nBase year: 2011-12', fontsize=20, fontweight='bold')
ax[0,1].set_xlabel("Years", fontsize=8, fontweight='bold')
ax[0,1].set_ylabel("Amount (Rupees Crore)", fontsize=8, fontweight='bold')
ax[0,1].xaxis.set_major_locator(ticker.MultipleLocator(5))

sns.barplot(x= df.index, y=df['Gross National Income'], color="darkblue", ax=ax[1,0])
ax[1,0].set_title('Gross National Income (at constant prices) \nBase year: 2011-12', fontsize=20, fontweight='bold')
ax[1,0].set_xlabel("Years", fontsize=8, fontweight='bold')
ax[1,0].set_ylabel("Amount (Rupees Crore)", fontsize=8, fontweight='bold')
ax[1,0].xaxis.set_major_locator(ticker.MultipleLocator(5))

sns.barplot(x= df.index, y=df['Net National Income'], color="darkblue", ax=ax[1,1])
ax[1,1].set_title('Net National Income (at constant prices) \nBase year: 2011-12', fontsize=20, fontweight='bold')
ax[1,1].set_xlabel("Years", fontsize=8, fontweight='bold')
ax[1,1].set_ylabel("Amount (Rupees Crore)", fontsize=8, fontweight='bold')
ax[1,1].xaxis.set_major_locator(ticker.MultipleLocator(5))

sns.barplot(x= df.index, y=df['Per Capita GDP'], color="darkblue", ax=ax[2,0])
ax[2,0].set_title('Per Capita GDP (at constant prices) \nBase year: 2011-12', fontsize=20, fontweight='bold')
ax[2,0].set_xlabel("Years", fontsize=8, fontweight='bold')
ax[2,0].set_ylabel("Amount (Rupees Crore)", fontsize=8, fontweight='bold')
ax[2,0].xaxis.set_major_locator(ticker.MultipleLocator(5))

sns.barplot(x= df.index, y=df['Per Capita GNI'], color="darkblue", ax=ax[2,1])
ax[2,1].set_title('Per Capita GNI (at constant prices) \nBase year: 2011-12', fontsize=20, fontweight='bold')
ax[2,1].set_xlabel("Years", fontsize=8, fontweight='bold')
ax[2,1].set_ylabel("Amount (Rupees Crore)", fontsize=8, fontweight='bold')
ax[2,1].xaxis.set_major_locator(ticker.MultipleLocator(5))

fig.tight_layout()
fig.subplots_adjust(top=0.75, bottom=-0.2)
plt.show()

# export figures

plt.savefig("/Users/arpanganguli/Documents/Professional/Projects/SINE/Plots/Macroeconomic Indicators at constant prices 2011-12.png"