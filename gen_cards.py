from PIL import Image, ImageDraw, ImageFont

# Define the path for the uploaded suit images
suit_images = {
    'clubs': 'symbols/clubs.png',
    'diamonds': 'symbols/diamonds.png',
    'hearts': 'symbols/hearts.png',
    'spades': 'symbols/spades.png'
}

# Define suits and values
suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

# Set image dimensions and background color
img_width, img_height = 200, 300
background_color = 'white'

# Create an example image for 'Ace of Clubs' to demonstrate the output with a bigger text and graphics
# Since the user has only uploaded clubs.png, we will use it as an example

for suit in suits:
  for value in values:
    # Load the club symbol image
    suit_image = Image.open(suit_images[suit])

    # Resize the suit image to fit the card
    suit_image = suit_image.resize((100, 100))

    # Create a blank image with white background
    img = Image.new('RGB', (img_width, img_height), color=background_color)
    draw = ImageDraw.Draw(img)

    # Load a font
    font_size = 40
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)

    # Add text for value and suit
    text = f"{value}"
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (img_width - text_width) / 2
    text_y = (img_height - text_height) / 2 - suit_image.height / 2
    draw.text((text_x, text_y), text, font=font, fill='black')

    # Paste the suit image onto the card
    img.paste(suit_image, (int((img_width - suit_image.width) / 2), int(text_y + text_height + 10)), suit_image)

    # Save the image
    output_path = f'cards/{value}_of_{suit}.png'
    img.save(output_path)

output_path

