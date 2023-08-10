# Detectar números de teléfono en una cadena y sustituyéndolos por (número oculto):

import re


string = "Tel +34 666 61 21 45 | +34 651 23 48 91."

string_mod = re.sub(r"\+\d{1,3}\s\d{3}(\s\d{2}){3}","(número oculto)", string)

print(string, string_mod)