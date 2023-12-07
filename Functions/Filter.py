def filter_str(key_filters, text, key_idex, show=True, ignore_capitals=True):
    text = str(text)
    chars_filtert = 0
    keys = []
    final_text = ""
    key_idex = str(key_idex)
    if ignore_capitals:
        text = text.lower()
        key_filters = key_filters.lower()
    if len(key_idex) > 0:
        keys = key_filters.split(key_idex)
    else:
        for char in key_filters:
            keys.append(char)

    for char in text[:]:
        if char in keys:
            text.replace(char, "")
            chars_filtert += 1
        else:
            final_text += str(char)
    if show:
        print(f"\n\t\t\t\t\t\t\t\t\t\t\t\tFilter_function:\t\t~~Removed ({chars_filtert}) from ({len(text)}) Characters~~\n")    # nopep8
    return final_text


filters = ""
text2 = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam"    # nopep8

print(filter_str(filters, text2, ""))
