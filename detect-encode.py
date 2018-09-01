import sys
from collections import Counter
import string


def check(trg, charset, name):
    if trg.issubset(charset):
        print('****' + name + "****")
    else:
        print("Not {}".format(name))
        print(trg.difference(charset))

    return


chars = ''
# read from stdin
with open(sys.argv[1]) as f:
    chars = f.read().replace('\n', '')

char_set = set(Counter(chars).keys())

# binhex
bin_hex = set("!\"#$%&'()*+,-012345689@ABCDEFGHIJKLMNPQRSTUVXYZ[`abcdefhijklmpqr")

# ascii85
ascii85_z85 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii85_z85 += '0123456789'
ascii85_z85 += '.-:+=^!/*?&<>()[]{}@%$#'
ascii85_z85 = set(ascii85_z85)

# also base85
ascii85_rfc1924 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii85_rfc1924 += '0123456789'
ascii85_rfc1924 += '!#$%&()*+-;<=>?@^_`{|}~'
ascii85_rfc1924 = set(ascii85_rfc1924)

# base16 hex
base16 = set('0123456789ABCDEFabcdef')

# base32
base32_rfc4648 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
base32_rfc4648 += '234567'
base32_rfc4648 += '='
base32_rfc4648 = set(base32_rfc4648)

base32_z = 'abcdefghijkmnopqrstuwxyz'
base32_z += '13456789'
base32_z = set(base32_z)

base32_crockford = set('abcdefghijklmnopqrstvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ0123456789')

# base36
base36 = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890')

# base58
base58 = set('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')

# base64
"too hard"

# base91
base91 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
base91 += '0123456789'
base91 += '!#$%&()*+,./:;<=>?@[]^_`{|}~"'
base91 = set(base91)

# base122
"too complicated"

# uuencode
uuencode = set([chr(i) for i in range(32, 96)])

# xxencode
xxencode = set(string.ascii_letters + string.digits + '-+')

check(char_set, bin_hex, "BinHex")
check(char_set, ascii85_z85, "Ascii85, ZeroMQ Version, Z85")
check(char_set, ascii85_rfc1924, "Ascii85, RFC-1924 Version")
check(char_set, base16, "Base16, Hexadecimal")
check(char_set, base32_rfc4648, "Base32, RFC-4648 Version")
check(char_set, base32_z, "Base32, z-base-32 Version")
check(char_set, base32_crockford, "Base32, Crockford Version")
check(char_set, base36, "Base36")
check(char_set, base58, "Base58")
check(char_set, base91, "Base91")
check(char_set, uuencode, "uuencode")
check(char_set, xxencode, "xxencode")
