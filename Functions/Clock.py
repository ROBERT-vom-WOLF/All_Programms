def convert(hours, minutes, seconds=0, output_int=True, show=True):
    if seconds >= 60:
        seconds = 0
        minutes += 1
    if minutes >= 60:
        minutes = 0
        hours += 1

    text = ""
    if hours < 10:
        text += f"0{str(hours)}:"
    else:
        text += f"{str(hours)}:"

    if minutes < 10:
        text += f"0{str(minutes)}:"
    else:
        text += f"{str(minutes)}:"

    if seconds < 10:
        text += f"0{str(seconds)}"
    else:
        text += f"{str(seconds)}"

    if show:
        print(text)

    if output_int:
        return hours, minutes, seconds

    else:
        return text


convert(2, 8, 30, show=False, output_int=True)

