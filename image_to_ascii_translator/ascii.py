from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

def get_char(r, g, b, alpha = 256):
	if alpha == 0:
		return " "
	length = len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	normalized_gray = gray / 256.0
	return ascii_char[int(normalized_gray*length)]

parser = argparse.ArgumentParser()

parser.add_argument("file", help="The input image of the program")
parser.add_argument("-o", "--output", help="The output .txt file of the program")
parser.add_argument("--width", type=int, default=80, help="Output width")
parser.add_argument("--height", type=int, default=80, help="Output height")

args = parser.parse_args()
image = args.file
width = args.width
height = args.height
output_filename = args.output

if __name__ == "__main__":
	im = Image.open(image)
	im = im.resize((width, height), Image.NEAREST)

	text_content = ""

	for h in range(height):
		for w in range(width):
			text_content += get_char(*im.getpixel((w, h)))
		text_content += "\n"

	if output_filename:
		with open(output_filename+".txt", "w") as f:
			f.write(text_content)
	else:
		with open("output.txt", "w") as f:
			f.write(text_content)