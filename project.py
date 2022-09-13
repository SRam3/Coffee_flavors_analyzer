import os.path
import fitz
import glob
import json
import sys

from fitz import Page, Rect


def main():
    return information_extraction_from_pdf()


def input_test_file_checker():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    return sys.argv[1]


def pdf_files_path():
    input_path = os.path.join(input_test_file_checker(), "*.pdf")
    path = glob.glob(input_path)
    if len(path) == 0:
        raise FileNotFoundError("Incorrect file path")
    return path


def information_extraction_from_pdf():
    data_pandas_format = []
    for pdf in pdf_files_path():
        with fitz.open(pdf) as pdf_file:
            for i in range(len(pdf_file)):
                page: Page = pdf_file[i]

                # See extraction_coordinates function for details
                rectangle_red = Rect(30, 67, 250, 123)
                text_red = page.get_textbox(rectangle_red).split("\n")

                rectangle_blue = Rect(30, 190, 161, 370)
                text_blue = page.get_textbox(rectangle_blue).split("\n")

                rectangle_yellow = Rect(163, 188, 462, 303)
                text_yellow = page.get_textbox(rectangle_yellow).split("\n")

                rectangle_black = Rect(163, 290, 462, 380)
                text_black = page.get_textbox(rectangle_black).split("\n")

                data = {
                    "Fecha": f"{text_red[2]}",
                    "ID": f"{text_red[0]}",
                    "Fragancia/Aroma": f"{text_blue[1]}",
                    "Sabor": f"{text_blue[3]}",
                    "Sabor Residual": f"{text_blue[5]}",
                    "Acidez": f"{text_blue[7]}",
                    "Cuerpo": f"{text_blue[9]}",
                    "Uniformidad": f"{text_blue[11]}",
                    "Balance": f"{text_blue[13]}",
                    "Taza Limpia": f"{text_blue[15]}",
                    "Dulzura": f"{text_blue[17]}",
                    "Puntaje Catador": f"{text_blue[19]}",
                    "Puntaje Total": f"{text_blue[21]}",
                    "Descripcion": f"{text_yellow}",
                    "Humedad": f"{text_black[1]}",
                    "Almendra sana": f"{text_black[3]}",
                    "Broca": f"{text_black[5]}",
                    "Pasilla": f"{text_black[7]}",
                }

                data_pandas_format.append(data)

    # Write data in suitable json format to read as pandas dataframe
    with open("data.json", "a") as f:
        json.dump(data_pandas_format, f, ensure_ascii=False, sort_keys=True, indent=2)


if __name__ == "__main__":
    main()
