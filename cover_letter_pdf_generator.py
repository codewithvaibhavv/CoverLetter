from fpdf import FPDF
import os

date = input("Enter Date (e.g., 28 Feb 2026): ")
company_name = input("Enter Company Name: ")
company_address = input("Enter Company Address (comma-separated): ")
appliedVia = input("Where did you see the job posting? (e.g., Naukri.com, LinkedIn): ")

# ----------------------------
# Format address: two parts per line
# ----------------------------
address_parts = [part.strip() for part in company_address.split(",")]
formatted_address = "\n".join([", ".join(address_parts[i:i+2]) for i in range(0, len(address_parts), 2)])

cover_letter = f"""
Vaibhav Sharma
Sec - 6, E - 62
Moradabad (244001)
vaibhavsharma11061998@gmail.com
9760653801
{date}

{company_name}
{formatted_address}

Dear Hiring Manager,
                        I am writing to express my interest in the Dot Net Developer position at {company_name}, as advertised on {appliedVia}. With my experience in Dot Net development and a strong passion for C#, I am confident that I would be a valuable addition to your team.

In my previous role as Dot Net Developer at Teerthankar Mahaveer University, I developed solid skills in this field. I am eager to contribute my expertise to {company_name} and would welcome the opportunity to discuss how my qualifications align with your needs.

Thank you for considering my application. I look forward to the possibility of speaking with you.

Sincerely,

Vaibhav Sharma
"""

pdf = FPDF()
pdf.add_page()

font_path = "dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf"
if not os.path.exists(font_path):
    print(f"Error: {font_path} not found. Please check the font path.")
    exit()

pdf.add_font("DejaVu", "", font_path, uni=True)
pdf.set_font("DejaVu", "", 12)
pdf.multi_cell(0, 8, cover_letter)

file_name = f"Cover_Letter_{company_name.replace(' ', '_')}.pdf"
pdf.output(file_name)

print(f"\n✅ Cover letter PDF generated successfully: {file_name}")