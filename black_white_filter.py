from PIL import Image
import time
import argparse
parser = argparse.ArgumentParser(description='Great Description To Be Here')
parser.add_argument('-location', action='store', help='Location of original image')
args = parser.parse_args()
im = Image.open(args.location)
filtered_im = im.convert('L')
time.sleep(8)
filtered_im.save('result.jpg')
