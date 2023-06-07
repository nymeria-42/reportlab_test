from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.units import cm
from reportlab.platypus import NextPageTemplate, PageBreak
from reportlab.lib.pagesizes import A4

def FirstPage(canvas, doc):
    try:
        canvas.saveState()
        lista = {"Linha teste 1": "Valor 1", "Linha teste 2": "Valor 2"}

        nome_pdf = "teste"
        x = 720
        for key,value in lista.items():
            x -= 20
            canvas.drawString(100,x, '{} : {}'.format(key,value))
        canvas.setTitle(nome_pdf)
        canvas.setFont("Helvetica-Oblique", 14)
        canvas.line(110,700,580,700)
        canvas.drawString(245,750, 'Cabeçalho')
        canvas.setFont("Helvetica-Bold", 12)
        canvas.drawString(245,724, 'Teste')
        canvas.restoreState()
    except Exception as e:
        print(e)

doc = SimpleDocTemplate("test_doc.pdf", pagesize=A4,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
Story=[]
path_to_png = ""
plot = f"{path_to_png}"

im = Image(plot, 10*cm, 10*cm)
Story.append(PageBreak())
Story.append(im)
doc.build(Story, onFirstPage=FirstPage)

# Referências:
# https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/
# https://www.reportlab.com/docs/reportlab-userguide.pdf
# https://github.com/dschuermann/printable-digital-signature/blob/master/generate_pdf.py
