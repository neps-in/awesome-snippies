# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Snippet:
#   Invert Color
# About:
#   For a given color in hex format as '#ce12fa' gives a inverted color in the same
# format as "#31ed5"
#   * Support for black & white / grayscale
# 
# Inspiration :
#   To write python version for this https://github.com/onury/invert-color
#
#
# Funda / Steps :
# 1. Seperate the R, G, B Components
# 2. Subtract from 255 to get inverted color the separated component
# 3. Convert back the individual component to hexa decimal and concat all the separate R, G, B components
#
# Author:
#   Napoleon Arouldas
#
# Link:
#   https://neps.in
#
# Created on:
#   2021-10-24 10:35:05
#
# Changelog:
#   2021-10-24 10:35:21 - created first raw version
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def invertColor(hexa,  bw=False):
    """
    For a given color code in hex value as "#ge127e" returns a inverted color code
    in the same hex format "#"
    """
    # Extract the color code only leaving the #
    if hexa.index('#') == 0:
        hexa = hexa[1:]

    # convert 3-digit hexa to 6-digits.
    if len(hexa) == 3:
        hexa = hexa[0] + hexa[0] + hexa[1] + hexa[1] + hexa[2] + hexa[2]

    # Check for validity of the color code
    if len(hexa) != 6:
        print('Invalid color code')

    # Get R, G, B component
    r = int(hexa[slice(0, 2)], 16)
    g = int(hexa[slice(2, 4)], 16)
    b = int(hexa[slice(4, 6)], 16)

    # If black & White
    if bw:
        inverted_color = '#000000' if (
            r * 0.299 + g * 0.587 + b * 0.114) > 186 else '#FFFFFF'
        return inverted_color

    #print(str(r) + str(g) + str(b))

    # invert color components
    inverted_r = hex(255 - int(hexa[slice(0, 2)], 16))
    inverted_g = hex(255 - int(hexa[slice(2, 4)], 16))
    inverted_b = hex(255 - int(hexa[slice(4, 6)], 16))

    # print('Inverted val r, g, b', inverted_r, inverted_g, inverted_b)

    # Prefix with '#' and return the value
    return '#' + removePrefix(inverted_r) + removePrefix(inverted_g) + removePrefix(inverted_b)


def removePrefix(s):
    """
    Python have a habit of adding 0x for hexa decimal numbers.
    Removes the prefix 0x of oXFe ( Hexa decimal number )
    :param s:
    :return after removal of 0x:
    """

    # 0x - length is 2
    prefix_removed_str = s[2:]

    # print(' st: %s, prefix removed str: %s ', s, prefix_removed_str)
    return prefix_removed_str


# @todo : This code is broken, needs fix and improvement
# def generateAllColors():
#     for i in range(0, 10):
#         for j in range(0, 10):
#             for k in range(0, 10):
#                 hex_i = str(hex(i))
#                 hex_j = str(hex(j))
#                 hex_k = str(hex(k))
#                 hex_number = hex_i[2:] + hex_j[2:] + hex_k[2:]
#                 hex_number = '#' + hex_number
#                 # print('A Random Hex Color Code is :',hex_number)
#                 inverted_color = invertColor(hex_number)
#                 print("Color code:   Inverted Color:    ",
#                       hex_number, inverted_color)


if __name__ == "__main__":
    inverted_color = invertColor('#ce12fa')
    print('Inverted color', inverted_color)

    inverted_color_as_bw = invertColor('#ce12fa', bw=True)
    print('Inverted color as Black and White ', inverted_color_as_bw)
