# import itertools

# for c in range(0x110000):
#     if 0xdfff >= c >= 0xd800:
#         continue
#     bytes_enc = chr(c).encode('u8')
#     #if c >= 0xe000:
#     #    c -= 0x800
#     assert [1, 1, 1, 1, 1, 1, 1, 1, None, None, None, None, 2, 2, 3, 4][bytes_enc[0] >> 4] == len(bytes_enc), bytes_enc

# generate number of distinct unicode decodable bytestrings of length N, O(N * 256^N) time complexity
# all_bytes = [*range(256)]
# N = 3
# count = 0
# for res in itertools.product(*[all_bytes]*N):
#     try:
#         bytes(res).decode()
#         count += 1
#     except Exception as e:
#         pass
# print(f"{N = }\t{count = }")


charsets: dict[int, list[tuple[str, bytes]]] = {}


def build_charsets():
    if len(charsets) != 0:
        return
    print('building charsets')
    for ci in range(0x110000):
        if ci == 0 or 0xd800 <= ci < 0xe000:  # not using surrogates or null byte
            continue
        c = chr(ci)
        cb = c.encode()
        if len(cb) not in charsets:
            charsets[len(cb)] = []
        charsets[len(cb)].append((c, cb))
    print('done building charsets')


# generate number of distinct unicode decodable bytestrings of length N, O(N^2) time complexity
# 0x01 to 0x7f: 1 byte (0x7f)
# 0x80 to 0x7ff: 2 byte (0x780)
# 0x800 to 0xffff: 3 byte (0xf000 b/c surrogate space of 0xd800 to 0xdfff removed)
# 0x10000 to 0x110000: 4 byte (0x100000)
def get_bytestrings_of_length(N: int):
    build_charsets()
    charset_lengths = [len(charsets[i]) for i in range(1, 5)]
    a = []
    for n in range(N):
        total = charset_lengths[n] if n < 4 else 0
        for i in range(0, min(n, 4)):
            total += a[-1-i] * [127, 1920, 61440, 1048576][i]
        a.append(total)
        #print(a[-1], a[-1]/a[-2] if len(a) > 1 else None)
    #print(len(a), a[-1]/a[-2])
    return a[-1] if len(a) else 1


# find the nth ordered string, O(log^2(N)) time complexity
def n_to_str(n: int) -> str:
    build_charsets()
    print()
    print(n, 'start')
    if n == 0:
        return ''
    i = 0
    a = []
    so_far = 1
    while True:
        total = [127, 1920, 61440, 1048576, 0][min(i, 4)]
        for j in range(0, min(i, 4)):
            total += a[-1-j] * [127, 1920, 61440, 1048576][j]
        a.append(total)
        if so_far+total > n:
            break
        so_far += total
        i += 1
    if len(a) == 0:
        c, _ = charsets[1][n-1]
        return c
    print(a, f'| {n-so_far = }, {so_far = }, things: {[a[-2-i]*len(charsets[i+1]) for i in range(min(len(a)-1, 4))]}')
    print(n, 'end')
    return 'no proper return'


build_charsets()
print(hex(len(charsets[1])))
print(hex(len(charsets[2])))
print(hex(len(charsets[3])))
print(hex(len(charsets[4])))

print(get_bytestrings_of_length(3))

print(ascii(n_to_str(0).encode()), ascii(b''))
print(ascii(n_to_str(1).encode()), ascii(b'\x01'))
print(ascii(n_to_str(1 + 127 - 1).encode()), ascii(b'\x7f'))
print(ascii(n_to_str(1 + 127).encode()), ascii(b'\x01\x01'))
print(ascii(n_to_str(1 + 127 + 127*127 - 1).encode()), ascii('\x7f\x7f'))
print(ascii(n_to_str(1 + 127 + 127*127).encode()), ascii('\xc2\x80'))
print(ascii(n_to_str(1 + 127 + 127*127+1920 - 1).encode()), ascii('idk lol'))
print(ascii(n_to_str(1 + 127 + 127*127+1920).encode()), ascii(b'\x01\x01\x01'))
print(ascii(n_to_str(1 + 127 + 127*(127)+1920 + 127*(127*127+1920) - 1).encode()), ascii(b'\x7f\xdf\xbf'))
print(ascii(n_to_str(1 + 127 + 127*(127)+1920 + 127*(127*127+1920)).encode()), ascii(b'\x7f\xdf\xbf'))

