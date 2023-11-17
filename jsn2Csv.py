import pandas as pd

df = pd.read_json(r'output2.json')

df.to_csv(r'testps3.csv')