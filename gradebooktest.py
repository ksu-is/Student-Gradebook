import pandas as pd
import numpy as np
from xlsxwriter.utility import xl_rowcol_to_cell

df = pd.read_excel('GradebookDatabase.xlsx')
df.head(100)

print(df.head(100))


