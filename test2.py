from collections import namedtuple
import re
import pdfplumber
import pandas as pd
Line = namedtuple(
    'Line', 'SKU MRP Retailer_landing_with')
line_re = re.compile(r'\d \d{2,}')


def numbify(num):
    return float(num.replace('$', '').replace(',', ''))


with pdfplumber.open("01.pdf")as pdf:
    page = pdf.pages[0]
    text = page.extract_text(x_tolerance=2, y_tolerance=0)
    print(text)
data = []
with pdfplumber.open("01.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text(x_tolerance=2, y_tolerance=0)

    for line in text.split('\n'):
        if line_re.search(line):
            in_lines = True
            retailer_landing_with = line.split()
        # elif line.startswith('Grand'):
        #     break
        elif re.match(r'T\S{1}', line):
            mrp = line
        elif re.match(r'\d{0}', line):
            sku = line
        elif re.match(r'T\S{2}', line):
            retailer_landing_with = line
            line_info = Line(sku, mrp)
            data.append(line_info)
df = pd.DataFrame(data)
df
# df['Retailer_landing_with'] = df['Retailer_landing_with'].map(numbify)
# sum(df['Retailer_landing_with'])
df['MRP'] = df['MRP'].map(numbify)
# sum(df['MRP'])
df.to_csv('file01.csv', index=False)
