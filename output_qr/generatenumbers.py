#just used to create some image numbers to test the square numbers

from PIL import Image, ImageDraw, ImageFont

for i in range(1,33):
    # Create a new image
    img = Image.new('RGB', (270, 270), color = (73, 109, 137))

    # Get a drawing context
    d = ImageDraw.Draw(img)

    # Define the font
    font = ImageFont.truetype("arial.ttf", 100)

    # Write the index number as text on the image
    d.text((10,10), str(i), fill=(255,255,0), font=font)

    # Save the image
    img.save(f'{i}.png')