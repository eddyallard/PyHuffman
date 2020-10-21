from service.Encoder import Encoder
import argparse


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="The path of the file", type=str)
    parser.add_argument("mode", help="E : Encoding mode | D : Decoding mode", choices=['E', 'D'])
    args = parser.parse_args()
    path, filename = args.path.rsplit('/', 1)
    path += "/"
    filename = filename.split('.')[0]
    if args.mode == 'E':
        encode = Encoder(filename,path)
        print("Encoding...")
        encode.encode()
        print ("Encoding was successful!")
    else:
        print(filename)
        print(path)
        encode = Encoder(filename, path)
        print("Decoding...")
        print(encode.decode())
        print("Decoding was successful!")


Main()
