from PyPDF2 import PdfFileWriter, PdfFileReader

reader = PdfFileReader("Perfilación German Ramirez 2.pdf", "r")
output = PdfFileWriter()
page = reader.getPage(0)

# (X0, Y0)
page.cropBox.setLowerLeft((0, 0))
# (X1, Y0)
page.cropBox.setLowerRight((750, 0))
# (X0, Y1)
page.cropBox.setUpperLeft((0, 600))
# (X1, Y1)
page.cropBox.setUpperRight((750, 600))

output.addPage(page)

with open("out.pdf", "wb") as out_f:
    output.write(out_f)


# Original PDF document's dimensions to crop
# (0, 0)
# (0, 595.32)
# (841.92, 595.32)
# (841.92, 0)
