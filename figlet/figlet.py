from pyfiglet import Figlet
import sys
import random


def main():
    """Test figlet"""
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 2:
        sys.exit('Invalid usage')
    if len(sys.argv) == 3:
        if not (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
            sys.exit('Invalidd usage')
        font = sys.argv[2]
        if not font in fonts:
            sys.exit('Invalid font')

    if len(sys.argv) < 2:
        font = random.choice(fonts)
    figlet.setFont(font=font)
    print(figlet.renderText(input('Input: ').strip()))


if __name__ == '__main__':
    main()
