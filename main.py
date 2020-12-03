from service.Encoder import Encoder
import argparse

def OsChecker(path):
    if "/" in path:
        return True
    else:
        return False
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="The path of the file", type=str)
    parser.add_argument("mode", help="E : Encoding mode | D : Decoding mode", choices=['E', 'D'])
    args = parser.parse_args()
    if OsChecker(args.path):
        path, filename = args.path.rsplit("/", 1)
        path += "/"
        filename = filename.split('.')[0]
    else:
        path, filename = args.path.rsplit("\\", 1)
        path += "\\"
        filename = filename.split('.')[0]
    if args.mode == 'E':
        encode = Encoder(filename,path)
        print("Encoding...")
        encode.encode()
        print ("Encoding was successful!")
    else:
        print(f'{path}/{filename}')
        encode = Encoder(filename, path)
        print("Decoding...")
        encode.decode()
        print("Decoding was successful!")


Main()
