def print_box_wrapper(text):
    width = len(text[0]) + 4
    print('')
    g_line = "+{0}+".format("-" * (width - 2))
    print(g_line)
    for line in text:
        print("| {0:<{1}} |".format(line, width - 4))
    print(g_line)
