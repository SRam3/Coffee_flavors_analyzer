import fitz
import os.path
import sys


from fitz import Document, Page, Rect


def main():
    return visualize_region_of_extraction()


def input_test_file_checker():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    return sys.argv[1]


def visualize_region_of_extraction():
    """Function to create a set of rectangles that encircles the data to extract.
    It uses a specific pdf file to test the coordinates of the rectangles to
    extract the data. This coordinates are used in the information_extraction_from_pdf()
    function located in project.py file.
    To be scaled to the coffee_flavor_profiles files, it is considered to use the specific
    pdf format from the test pdf.
    """

    try:
        input_path = input_test_file_checker()
        doc: Document = fitz.open(input_path)
    except fitz.fitz.FileNotFoundError:
        print("Incorrect file name")
    else:
        for i in range(len(doc)):
            page: Page = doc[i]

            # Coordinates (x0, y0, x1, y1)
            rectangle_red = Rect(30, 67, 250, 123)
            rectangle_blue = Rect(30, 190, 161, 370)
            rectangle_yellow = Rect(163, 188, 462, 290)
            rectangle_black = Rect(163, 290, 462, 390)

            # Draw a rectangle with specific color to visualize the data extraction area
            page.draw_rect(rectangle_red, width=1.5, color=(1, 0, 0))
            page.draw_rect(rectangle_blue, width=1.5, color=(0, 0, 1))
            page.draw_rect(rectangle_yellow, width=1.5, color=(1, 1, 0))
            page.draw_rect(rectangle_black, width=1.5, color=(0, 0, 0))

            def text_extraction_validation():
                """Print the information which has been extracted from the rectangle"""
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

        head, tail = os.path.split(input_path)
        area_name = os.path.join(head, "area_" + tail)
        return doc.save(area_name), text_extraction_validation()


if __name__ == "__main__":
    main()
