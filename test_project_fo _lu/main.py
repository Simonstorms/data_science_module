import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('countries.csv')



sns.scatterplot(x='area (sq.km)', y='population', c=df['pop_density']/5, data=df)
plt.show()
