#!/usr/bin/python
r"""cowsay.py -
 __________________________________
| Pick an animal and feed it text. |
 ----------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

 ________________________________________
| e.g. ./cowsay.py 'All animals are      |
| equal, but some animals are more equal |
| than others.'                          |
 ----------------------------------------
        \     .-.'  `; `-._  __  _
         \   (_,         .-:'  `; `-._
           ,'o"(        (_,           )
          (__,-'      ,'o"(            )>
             (       (__,-'            )
              `-'._.--._(             )
                 |||  |||`-'._.--._.-'
                            |||  |||
"""
import sys
import textwrap

ANIMALS = {
    'cow': r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """,
    'sheep': r"""
        \     .-.'  `; `-._  __  _
         \   (_,         .-:'  `; `-._
           ,'o"(        (_,           )
          (__,-'      ,'o"(            )>
             (       (__,-'            )
              `-'._.--._(             )
                 |||  |||`-'._.--._.-'
                            |||  |||
    """
}

def main():
    """Read content from stdin or sys.argv."""
    if len(sys.argv) > 1:
        content = sys.argv[1]
    else:
        content = sys.stdin.read()
    animal = ANIMALS['cow']
    blob = print_animal(animal, content)
    print blob

def print_animal(animal, content, line_width=39, border='|'):
    """Creates printable `animal` saying `content`."""
    # First put together text balloon.
    wrapped = textwrap.wrap(content, width=line_width)
    max_width = max(map(len, wrapped))
    lines = ['{border} {line} {border}'.format(
        border=border, line=line.ljust(max_width))
             for line in wrapped]
    border = lambda char:\
        [' {border} '.format(border=char * (2 + max_width))]
    balloon = '\n'.join(border('_') + lines + border('-'))
    animal = animal.lstrip('\n')  # for the `r"""...` line
    return '\n'.join([balloon, animal])


if __name__ == '__main__':
    main()
