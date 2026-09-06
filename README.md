# unnamed bit based esolang

the concept is that even on golfing languages like vyxal and golfscript, using entire characters to represent really common information is bad. instead of byte-based tokenization, we can use a huffman tree.

## unicode decodable program encoding

56% full utf8 bound written about [here](https://qntm.org/unicodings) (144.56775126843763/256 = 0.5647177783923345).

## todo

- compression support first bit 1 or 0 to distinguish?
- standard prepackaged huffman trees for shorter golfing
- make the huffman tree nodes shufflable.

