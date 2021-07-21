import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

fish = pd.read_csv('https://bit.ly/fish_csv_data')
fish.head()

# print(pd.unique(fish['Species']))

fish_input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
# print(fish_input[:5])

fish_target = fish['Species'].to_numpy()
# print(fish_target[:5])

train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)