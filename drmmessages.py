def rotation(str):
    cont = 0
    for char in str:
        cont += ord(char) - 65
    return cont


def forward(str, positions):
    str_new = []
    for char in str:
        # char_new = ord(char) - 65 + positions
        char_new = ord(char) - 65 + positions % 26
        if char_new <= 25:
            str_new.append(chr(char_new + 65))
        else:

            while char_new > 25:
                char_new -= 26
            str_new.append(chr(char_new + 65))

    return ''.join(str_new)


def merge(first, second):
    out = []
    i = 0
    while i < len(first):
        out.append(forward(first[i], ord(second[i]) - 65))
        i += 1

    return ''.join(out)


drm = input()
size = len(drm)

first = drm[:size//2]
second = drm[size//2:]

rotation_01 = rotation(first)
rotation_02 = rotation(second)

first_new = forward(first, rotation_01)
second_new = forward(second, rotation_02)

out = merge(first_new, second_new)
print(out)
