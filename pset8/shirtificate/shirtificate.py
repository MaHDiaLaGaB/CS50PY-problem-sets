from fpdf import FPDF

class Shirt():
    def __init__(self, name):
        self.tpdf = FPDF()
        self.tpdf.add_page()
        self.tpdf.set_font("helvetica", "B", 50)
        self.tpdf.multi_cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align = 'C')
        self.tpdf.image("shirtificate.png", w=self.tpdf.epw)

        self.tpdf.set_font_size(30)
        self.tpdf.set_text_color(255,255,255)
        self.tpdf.text(x =47.5, y= 140, txt = f"{name} took CS50")

    def save(self, name):
        self.tpdf.output(name)

name = input('Name: ')
pdf = Shirt(name)
pdf.save("shirtificate.pdf")