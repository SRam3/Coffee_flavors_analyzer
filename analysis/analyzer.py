import sys

from util import Coffee

def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python analizer.py <directory>")
    directory = sys.argv[1] if len(sys.argv) == 2 else "data.json"
    try:
        coffee = Coffee(directory)
    except FileNotFoundError:
        sys.exit("File not found")

    coffee.get_correlation()

if __name__ == "__main__":
    main()
