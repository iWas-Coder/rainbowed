class rainbowed:

    # Input code in the ANSI escape sequence, the Select Graphic Rendition subset:
    def code(n: int):
        return '\033[{}m'.format(n)

    # Font effects:
    RESET = code(0)
    BOLD = code(1)
    UNDERLINE = code(4)
    CROSSED = code(9)

    # 4-bit colours:
    RED = code(91)
    GREEN = code(92)
    YELLOW = code(93)
    BLUE = code(94)
    MAGENTA = code(95)
    CYAN = code(96)
    WHITE = code(97)
