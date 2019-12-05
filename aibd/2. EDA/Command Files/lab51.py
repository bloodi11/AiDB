import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("../Analysis Data/earthquake_data.csv")

new_data = pd.DataFrame()

age = data['Age']
gender = data['What is your gender?']
answer = data['Do you think the \"Big One\" will occur in your lifetime?']

new_data.insert(0, "Age", age, True)
new_data.insert(1, "Gender", gender, True)
new_data.insert(2, "OneBigHappen", answer, True)


new_data.groupby(['Age', 'OneBigHappen'])\
    .OneBigHappen.count().unstack().plot.bar(legend=True)
    
plt.show()

new_data.groupby(['Gender', 'OneBigHappen'])\
    .OneBigHappen.count().unstack().plot.bar(legend=True)
    
plt.show()
 





