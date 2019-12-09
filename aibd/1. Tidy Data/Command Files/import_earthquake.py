import pandas as pd

data = pd.read_csv("../Analysis Data/earthquake_data.csv")

new_data = pd.DataFrame()

age = data[['Age']]
gender = data[['What is your gender?']]
answer = data[['Do you think the \"Big One\" will occur in your lifetime?']]

new_data.insert(0, "Age", age, True)
new_data.insert(1, "Gender", gender, True)
new_data.insert(2, "One Big happen?", answer, True)

rank = new_data.groupby(['Age', 'Gender', 'One Big happen?'])

print(new_data)

new_data.to_csv(r'../Analysis Data/results.csv', index = False, header = True)
