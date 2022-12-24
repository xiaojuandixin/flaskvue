import pandas as pd
url='./data.html'
df=pd.read_html(url)[3]
print(df)
