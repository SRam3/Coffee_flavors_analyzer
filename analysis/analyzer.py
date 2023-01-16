import sys

from util import Exploration, Coffee

def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python analizer.py <directory>")
    directory = sys.argv[1] if len(sys.argv) == 2 else "data.json"
    try:
        data_exploration = Exploration(directory)
        coffee = Coffee(directory)
    except FileNotFoundError:
        sys.exit("File not found")

    data_exploration.get_histogram()
    # data_exploration.get_description()
    # coffee.qualitative_sensorial_attributes()


if __name__ == "__main__":
    main()
