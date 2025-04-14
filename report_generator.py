from fpdf import FPDF

def generate_pdf_report(filename, scores, details):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="AIthics Score Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Final Score: {scores['total']}/100", ln=True)
    pdf.ln(5)

    for category, value in scores.items():
        if category != 'total':
            pdf.cell(200, 10, txt=f"{category.capitalize()} Score: {value}", ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", 'I', 10)
    for title, info in details.items():
        pdf.multi_cell(0, 10, f"{title}: {info}")

    pdf.output(filename)
