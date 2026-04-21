from fpdf import FPDF

class SessionPDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, 'Project Documentation', border=0, align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(10)

    def section(self, title, content):
        self.set_font('Helvetica', 'B', 14)
        self.set_fill_color(230, 230, 230)
        self.cell(0, 10, f" {title}", border=1, align='L', fill=True, new_x='LMARGIN', new_y='NEXT')
        self.ln(4)
        self.set_font('Helvetica', '', 11)
        self.multi_cell(0, 7, content)
        self.ln(5)

def generate_report():
    pdf = SessionPDF()
    pdf.add_page()
    
    pdf.section("Phase 1: Extraction", "Extracted test.zip and verified CSV integrity.")
    pdf.section("Phase 2: Cleaning", "Filled 22 null overviews and standardized datetime formats.")
    pdf.section("Phase 3: Visualization", "Generated a 4-panel Seaborn dashboard with KPIs.")
    
    pdf.output('Project_Report.pdf')
    print("Report generated: Project_Report.pdf")

if __name__ == "__main__":
    generate_report()
