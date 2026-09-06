class VM:
    def __init__(self, data: bytes):
        total = 0
        multiplier = 1
        i = 0
        while i < len(data):
            chr_byte_size = [1, 1, 1, 1, 1, 1, 1, 1, None, None, None, None, 2, 2, 3, 4](data[i] >> 4)
            
        print(self.bits

