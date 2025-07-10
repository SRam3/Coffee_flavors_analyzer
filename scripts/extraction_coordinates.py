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
    """Create rectangles to visualize the areas of interest used for extraction.

    A sample PDF file is used to test and demonstrate the coordinates of the
    rectangles from which the data will be extracted. These same coordinates are
    later consumed by the :func:`information_extraction_from_pdf` function in
    ``scripts/data_extraction.py``.  This helper function therefore
    demonstrates the coordinates that are ultimately used during the extraction
    process. To be scaled to the coffee_flavor_profiles files, it is considered
    to use the specific PDF format from the test PDF.
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

        head, tail = os.path.split(input_path)
        area_name = os.path.join(head, "area_" + tail)
        return doc.save(area_name), text_extraction_validation()


if __name__ == "__main__":
    main()
