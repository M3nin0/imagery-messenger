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
    parser.add_argument('--config', action='store', type=str,
                        help='')

    args = parser.parse_args()

    if not (args.token and args.input and args.output):
        print('As opções\n --token\n --input\n --output\nDevem estar preenchidas')
    else: 
        pass
