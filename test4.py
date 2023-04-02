import tabula
di = tabula.read_pdf('Jaquar.pdf', pages='all',
                     encoding='iso-8859-1', stream=True)
# encoding='iso-8859-1'
count = 0
for i in di:
    i.to_csv('Practise'+str(count)+'.csv', index=False)
    count += 1
