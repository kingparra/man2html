#!/usr/bin/env python3
# Add <link> within <head>...</head> element to include a stylesheet.
# This is computationally expensive, try to use a diff instead.
from bs4 import BeautifulSoup as S
import sys


def main():
    path = sys.argv[1]
    with open(path, "r") as file:
        content = S(file.read(), "html")
        content.head.append(
            S("""<link rel="stylesheet" type="text/css" href="style.css">""",
                "html").head.link
            )
    with open(path + ".new.html", "w") as file:
        file.write(str(content.prettify()))


if __name__ == "__main__":
    main()
