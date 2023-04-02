from collections import namedtuple
import re
import pdfplumber
import pandas as pd
Line = namedtuple(
    'Line', 'No Article Desc Quant UOM MRP BaseCost IGST_perc IGST_INR Total_Base HSN_SAC_Code Site')
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
            no, article, *desc, quant, uom, mrp, basecost, igstp, igst_inr, total_base = line.split()
            desc = ' '.join(desc)
        elif line.startswith('Grand'):
            break
        elif re.match(r'\d{4}', line):
            hsn_code = line
        elif re.match(r'T\S{3}', line):
            site = line
            line_info = Line(no, article, desc, quant, uom, mrp,
                             basecost, igstp, igst_inr, total_base, hsn_code, site)
            data.append(line_info)
df = pd.DataFrame(data)
df
df['Total_Base'] = df['Total_Base'].map(numbify)
sum(df['Total_Base'])
df['IGST_INR'] = df["IGST_INR"].map(numbify)
sum(df['IGST_INR'])
df.to_csv('file.csv', index=False)
