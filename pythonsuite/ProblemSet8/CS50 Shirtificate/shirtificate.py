from fpdf import FPDF
from PIL import Image


def reduce_value_by_percent(value: int, percent: int) -> int:
    return value-int((value * percent) / 100)


def print_pdf(name: str) ->None:
    pdf = FPDF(orientation="Portrait", format="A4")
    pdf.set_left_margin(5)
    pdf.set_right_margin(5)
    pdf.set_auto_page_break(True)
    pdf.add_page(format=(210, 297))
    
    img = Image.open("shirtificate.png")
    img = img.resize((reduce_value_by_percent(img.width, 5), reduce_value_by_percent(img.height, 5)))
    pdf.image(img, y=pdf.epw/3)

    pdf.set_font('helvetica', size=48)
    pdf.cell(w=0, h=45, txt='CS50 Shirtificate', border=0, align='C');

    pdf.set_font('helvetica', size=24)
    pdf.set_xy(0,0)
    pdf.set_text_color(255)
    pdf.cell(w=0, h=img.height/2, txt='Ivan Gorshenin took CS50', border=0, align='C');

    pdf.output("shirtificate.pdf")


def main() ->None:
    name = input("Name: ").strip()
    print_pdf(name)

if __name__ == "__main__":
    main()
