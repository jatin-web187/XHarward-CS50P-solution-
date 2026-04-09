# to do
# import modules; pyfiglet,random , sys


# access class and mehods
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

# VALID ARGUMENT CASES ONLY
if len(sys.argv) == 1:
    font = random.choice(fonts)

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    if sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        sys.exit("Invalid font")

else:
    sys.exit("Invalid usage")

# Ask for input ONLY after validation
text = input("Input: ")

figlet.setFont(font=font)
print(figlet.renderText(text))


# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
