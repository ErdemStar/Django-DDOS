from fpdf import FPDF
import datetime
class PDF(FPDF):
    def header(self):
        # Logo
        #self.image('logo_pb.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'DDOS Attack Result')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class

def CreatePDF(data):
    time = datetime.datetime.now()
    tmp = "Result "+str(time.year) + "." + str(time.month) + "." + str(time.day)+".pdf"
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for i in range(1):
        pdf.cell(0, 10, str(data) + str(i), 0, 1)
    pdf.output(tmp, 'F')