# Credits to https://pythonhosted.org/PyPDF2/PdfFileMerger.html

from PyPDF2 import PdfFileMerger
from os import walk

files = next(walk("./org"), (None, None, []))[2]
pdffm = PdfFileMerger()

for p in files:
    pdffm.append('./org/'+p)

pdffm.write("./dst/result.pdf")
pdffm.close()