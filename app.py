import argparse

from imagery import Imagery

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tool to perform sending images to Facebook API')
    parser.add_argument('--input', action='store', type=str,
                        help='Sets the path of the folder containing the images that will be sent')
    parser.add_argument('--output', action='store', type=str,
                        help='Location where json with ids will be generated')
    parser.add_argument('--token', action='store', type=str,
                        help='Set the token that will be used')    

    args = parser.parse_args()

    if not (args.token and args.input):
        print('As opções\n --token\n --input\nDevem estar preenchidas')
    else:
        if args.output != None:
            img = Imagery(args.token, args.input, args.output)
        else:
            img = Imagery(args.token, args.input)
        img.send_image()