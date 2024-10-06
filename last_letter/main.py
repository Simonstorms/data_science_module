import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### Load the data from text files into dataframes
dataframes = [pd.read_csv(f'yob/yob{year}.txt', names=["Name", "Gender", "Count"]).assign(Year=year) for year in range(1880, 2015)]

### Combine all dataframes into a single dataframe
all_data = pd.concat(dataframes, ignore_index=True)

### Create a new column with the last letter of each name
all_data['LastLetter'] = all_data['Name'].str[-1]



### Plot the bar chart of last letters of names
# last_letter = all_data.groupby('LastLetter')['Count'].sum()
# last_letter.plot.bar()
# plt.title('Total Count of Names by Last Letter')
# plt.xlabel('Last Letter of Names')
# plt.ylabel('Total Count')
# plt.show()



### count for specific letter "s" in the years
# filtered_data = all_data[all_data['LastLetter'] == "s"]
# timeline_data = filtered_data.groupby('Year')['Count'].sum().reset_index()
# timeline_data.columns = ['Year', 'Count']
# print(timeline_data)
#
# timeline_data.plot(x='Year', y='Count')
# plt.show()



### multiple timelines for letters
# grouped_data = all_data.groupby(['LastLetter', 'Year'])['Count'].sum()
# crosstable = grouped_data.unstack(0)
#
# letters_to_plot = ['s', 'r', 'p']
# for letter in letters_to_plot:
#     if letter in crosstable.columns:
#         plt.plot(crosstable.index, crosstable[letter])
#
# plt.show()



### Heatmap of first and last letters
all_data['Name'] = all_data['Name'].str.upper()
all_data['FirstLetter'] = all_data['Name'].str[0]
all_data['LastLetter'] = all_data['Name'].str[-1]
crosstab = pd.crosstab(all_data['FirstLetter'], all_data['LastLetter'], values=all_data['Count'], aggfunc='sum')
crosstab = crosstab.sort_index(axis=0)

print(crosstab)
sns.heatmap(crosstab)
plt.show()