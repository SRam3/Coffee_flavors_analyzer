import os.path
import fitz
import glob
import json
import argparse

from fitz import Page, Rect


def main():
    user_path = input_test_file_checker()
    return information_extraction_from_pdf(user_path)


def information_extraction_from_pdf(path):
    """
    Data from pdf documents written in a json file compatible to be
    readed as pandas dataframe

    :param path: User input folder name containing the information to be extrated
    :type path: str
    :raise FileNotFoundError: If path is not correct.
    :rtype: json file
    """
    input_path = pdf_files_path(path)
    data_pandas_format = []
    for pdf in input_path:
        with fitz.open(pdf) as pdf_file:
            for i in range(len(pdf_file)):
                page: Page = pdf_file[i]

                # See extraction_coordinates module for details
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


def input_test_file_checker() -> object:
    """
    object holding path name of the folder containing the pdf documents.

    :param argparse object: command line argument from user input
    :type argparse
    :rtype: argument values of parser object in readable string representation
    """

    parser = argparse.ArgumentParser(description="folder path")
    parser.add_argument("-p", "--path", help="name path of the folder containing the pdf documents", type=str, required=True)
    args = parser.parse_args()
    return args


def pdf_files_path(user_path: str):
    """
    List of documents in folder path

    :param user_path: User input folder name containing the information to be extrated
    :type user_path: str
    :raise FileNotFoundError: If the user input is invalid
    :rtype: List containing the pdf documents name
    """

    input_path = os.path.join(user_path, "*.pdf")
    path = glob.glob(input_path)
    if len(path) == 0:
        raise FileNotFoundError("Incorrect file path")
    return path


if __name__ == "__main__":
    main()
