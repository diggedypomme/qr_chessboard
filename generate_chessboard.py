import segno            # QR generator
from PIL import Image   # for generating the chessboard


# Creating the QR codes
#######################

with open('chess_links.txt', 'r') as f:
    lines = f.readlines()
    
countup=1
while countup<33:


    qrcode = segno.make('{}'.format(lines[countup-1]))
    qrcode.save('output_qr/{}.png'.format(countup),  scale=10,border=1)
    countup=countup+1
    
    
# Create a blank image with the specified size
#######################
img = Image.new('RGB', (270, 270), color = (255, 255, 255))

# Save the image
img.save('output_qr/blank.png')    
    
    
    
# Adding them to the chessboard
###############################

# Load the images for the black squares
black_images = []
for i in range(1, 33):
    black_images.append(Image.open(f"output_qr/{i}.png"))

# Load the image for the white squares
white_image = Image.open("output_qr/blank.png")

# Get the size of a square from the first black image
square_size = black_images[0].size

# Create an empty image with a white background
width = square_size[0] * 8
height = square_size[1] * 8
chessboard = Image.new("RGB", (width, height), (255, 255, 255))

# Add the squares to the chessboard image
k = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            chessboard.paste(black_images[k], (i * square_size[0], j * square_size[1]))
            k += 1
        else:
            chessboard.paste(white_image, (i * square_size[0], j * square_size[1]))

#rotate the chessboard as the bottom left is white and should be black. The qrs 
#will be rotated but it's not an issue
chessboard = chessboard.rotate(90)

# Save the chessboard image
chessboard.save("chessboard.png")
