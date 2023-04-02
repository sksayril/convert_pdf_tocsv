# import tabula
# di = tabula.read_pdf('Atomberg Retail price list 01.07.2021.pdf',
#                      encoding='utf-8', pages='1')

# for i in range(len(di)):
#     di[i].to_csv(f"all_pages_table{i}.csv")

# pdf_path = ('Atomberg Retail price list 01.07.2021.pdf',enco)
# dfs = tabula.read_pdf(pdf_path, pages='1')
import tabula

di = tabula.read_pdf('RAJESHBHAI GAJERA.pdf',
                     encoding='iso-8859-1', pages='all')

for i in range(len(di)):
    di[i].to_csv(f"all_pages1{i}.csv")

# import tabula
# import pandas as pd

# pdf_file_path = 'Jaquar.pdf'

# # Read all PDF pages into a list of pandas DataFrames
# df_list = tabula.read_pdf(pdf_file_path, encoding='iso-8859-1', pages='all')

# # Concatenate all DataFrames into a single DataFrame
# df = pd.concat(df_list)

# # Write the concatenated DataFrame to a CSV file
# df.to_csv('all_pages.csv', index=False)
