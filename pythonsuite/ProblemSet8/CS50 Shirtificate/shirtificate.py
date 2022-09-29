from fpdf import FPDF

def print_pdf(name: str) ->None:
    pdf = FPDF()
    pdf.page_mode = "FULL_SCREEN"
    pdf.output("shirtificate.pdf")


def main() ->None:
    name = "Ivan Gorshenin"#input("Name: ").strip()
    print_pdf(name)

if __name__ == "__main__":
    main()
