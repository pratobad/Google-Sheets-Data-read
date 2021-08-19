import pandas as pd
sheetname="enrollment" # Enter Sheet name without using extention
sh = gc.open(sheetname)
worksheet = sh.sheet1
values_list = worksheet.get_all_values()
df = pd.DataFrame(values_list)
df.head()
