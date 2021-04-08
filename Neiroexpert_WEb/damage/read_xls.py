import pandas as pd
init_file = 'dannye_old.xls'
line = pd.read_excel(open(init_file, 'rb'), sheet_name='line')
print (line)