from service.Encoder import Encoder

felix = "C:\\Users\\Bepix\\Desktop\\realboi\\src\\dataset\\"
eddy = "/home/eddy/Documents/Coding/PycharmProjects/PyHuffman/dataset/"
encode = Encoder("beenus", felix)
encode.encode()
print(encode.decode())