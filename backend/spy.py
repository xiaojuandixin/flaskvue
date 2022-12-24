import pandas as pd
url='./fox.html'
df=pd.read_html(url)[3]
print(df)
