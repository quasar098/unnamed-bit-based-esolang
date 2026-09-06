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

# generate number of distinct unicode decodable bytestrings of length N, O(N^2) time complexity
# 0x00 to 0x7f: 1 byte (0x80)
# 0x80 to 0x7ff: 2 byte (0x780)
# 0x800 to 0xffff: 3 byte (0xf000 b/c surrogate space of 0xd800 to 0xdfff removed)
# 0x10000 to 0x110000: 4 byte (0x100000)
N = 10000
a = []
for n in range(N):
    total = [128, 1920, 61440, 1048576, 0][min(len(a), 4)]
    for i in range(0, min(n, 4)):
        total += a[-1-i] * [128, 1920, 61440, 1048576][i]
    a.append(total)
    #print(a[-1], a[-1]/a[-2] if len(a) > 1 else None)
print(len(a), a[-1]/a[-2])

# get nth lexicographically smallest unicode decodable bytestring of length N


