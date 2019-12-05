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


#new_data.insert(0, "Count", count, True)

# final_data = pd.DataFrame()

# final_data.insert(0, "Age", age, False)
# final_data.insert(1, "Gender", gender, False)
# final_data.insert(2, "One Big happen?", answer, False)

print(new_data)

# age = data.set_index("Age", drop = False)
# gender = data.set_index("What is your gender?", drop = False)
# answer = data.set_index("Do you think the \"Big One\" will occur in your lifetime?", drop = False)

