import pdfplumber
import csv 
import tqdm

# Replace '\n' with an empty string and add the subscript
def convert_subscript(formula):
    if formula is None: 
        return None
    if "\n" in formula:
        cleaned_formula = formula.replace("\n", "")
        return cleaned_formula
    return formula  # Return unchanged if no \n

with open('data/standard_state.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    with pdfplumber.open("data/NIST.TN.2126.pdf") as pdf:
        # Pages where heat of combustion data is present
        for pages in tqdm.tqdm(range(361, 380), desc="Processing pages"):
            page = pdf.pages[pages]
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if row[1] != '' and row[4] != None:
                        # row[4] is the molecule name
                        # row[10] is the phase
                        # row[16] is the heat of combustion
                        row = [row[4], row[10], row[16]]
                        writer.writerow(row)
