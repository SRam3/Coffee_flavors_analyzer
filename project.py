import os.path
import fitz
import glob
import json

from fitz import Document, Page, Rect


def main():
    return information_extraction_from_pdf()


def pdf_files_path():
    input_path = os.path.join("coffee_flavor_profiles", "*.pdf")
    # input_path = "test.pdf"
    return glob.glob(input_path)


def information_extraction_from_pdf():
    data_pandas_format = []
    for pdf in pdf_files_path():
        with fitz.open(pdf) as pdf_file:
            for i in range(len(pdf_file)):
                page: Page = pdf_file[i]

                # See visualize_region_of_extraction() for details
                rectangle_red = Rect(30, 67, 250, 123)
                text_red = page.get_textbox(rectangle_red).split("\n")

                rectangle_blue = Rect(30, 190, 161, 370)
                text_blue = page.get_textbox(rectangle_blue).split("\n")

                rectangle_yellow = Rect(163, 188, 462, 303)
                text_yellow = page.get_textbox(rectangle_yellow).split("\n")

                rectangle_black = Rect(163, 290, 462, 380)
                text_black = page.get_textbox(rectangle_black).split("\n")

                data = {
                    'Fecha': f'{text_red[2]}', 
                    'ID': f'{text_red[0]}',
                    'Fragancia/Aroma': f'{text_blue[1]}',
                    'Sabor': f'{text_blue[3]}',
                    'Sabor Residual': f'{text_blue[5]}',
                    'Acidez': f'{text_blue[7]}',
                    'Cuerpo': f'{text_blue[9]}',
                    'Uniformidad': f'{text_blue[11]}',
                    'Balance': f'{text_blue[13]}',
                    'Taza Limpia': f'{text_blue[15]}',
                    'Dulzura': f'{text_blue[17]}',
                    'Puntaje Catador': f'{text_blue[19]}',
                    'Puntaje Total': f'{text_blue[21]}',
                    'Descripcion': f'{text_yellow}',
                    'Humedad': f'{text_black[1]}',
                    'Almendra sana': f'{text_black[3]}',
                    'Broca': f'{text_black[5]}',
                    'Pasilla': f'{text_black[7]}'
                }

                data_pandas_format.append(data)
                # print(text_yellow)
                
    # print(text_yellow[0])
    # Write
    with open("data.json", "a") as f:
        json.dump(data_pandas_format, f, ensure_ascii=False, sort_keys=True, indent=2)


def visualize_region_of_extraction():
    """Function to create a set of rectangles that encircles the data to extract.
    It uses a specific pdf file to test the coordinates of the rectangles to
    extract the data. This coordinates are used in the information_extraction_from_pdf()
    function.
    To be scaled to the coffee_flavor_profiles files, it is considered to use the specific
    pdf format from the test pdf.
    """

    # Flag to create a pdf with the rectangles area extraction
    VISUALIZE = True

    input_path = "test.pdf"
    doc: Document = fitz.open(input_path)

    for i in range(len(doc)):
        page: Page = doc[i]

        # Coordinates (x0, y0, x1, y1)
        rectangle_red = Rect(30, 67, 250, 123)
        rectangle_blue = Rect(30, 190, 161, 370)
        rectangle_yellow = Rect(163, 188, 462, 290)
        rectangle_black = Rect(163, 290, 462, 390)

        if VISUALIZE:
            # Draw a rectangle with specific color to visualize the data extraction area
            page.draw_rect(rectangle_red, width=1.5, color=(1, 0, 0))
            page.draw_rect(rectangle_blue, width=1.5, color=(0, 0, 1))
            page.draw_rect(rectangle_yellow, width=1.5, color=(1, 1, 0))
            page.draw_rect(rectangle_black, width=1.5, color=(0, 0, 0))

            def text_extraction_validation():
                """Print the information which has been extrated from the rectangle"""
                rectangle_red_text = page.get_textbox(rectangle_red)
                rectangle_blue_text = page.get_textbox(rectangle_blue)
                rectangle_yellow_text = page.get_textbox(rectangle_yellow)
                rectangle_black_text = page.get_textbox(rectangle_black)
                print(
                    "{0},\n,{1},\n,{2},\n,{3}".format(
                        rectangle_red_text,
                        rectangle_blue_text,
                        rectangle_yellow_text,
                        rectangle_black_text,
                    )
                )

    if VISUALIZE:
        head, tail = os.path.split(input_path)
        area_name = os.path.join(head, "area_" + tail)
        return doc.save(area_name), text_extraction_validation()


if __name__ == "__main__":
    main()
