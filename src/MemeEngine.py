"""Module manipulates and draws text onto images."""

from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine:
    """Class will input an image and a random QuoteModel object and return a meme. """

    def __init__(self, path):
        """Initialize and add path of original image file to state."""
        self.image = path

    @staticmethod
    def draw_text(img: Image, body, author, font_size=36):
        """Helper method formats and adds text to image.

        :param Image img: The meme image to add text to
        :param str body: The quote body
        :param str author: The quote author
        :param int font_size: size of text font
        :return Image image: Image with text formatted and added
        """
        # Create a drawing context
        draw = ImageDraw.Draw(img)

        # Text formatting
        font = ImageFont.truetype("./assets/impact.ttf", font_size)
        text_color = (255, 255, 255)

        # Positioning of body text
        text_length = draw.textlength(body, font)
        pos_x = (img.width - text_length) / 2
        pos_y = img.height / 16

        draw.text((pos_x, pos_y), body, fill=text_color, font=font)

        # Positioning of author text
        text_length = draw.textlength(author, font)
        pos_x = (img.width - text_length) / 2
        pos_y = 14*(img.height / 16)

        draw.text((pos_x, pos_y), author, fill=text_color, font=font)

        return img

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Handler for generating the meme from an image file and quote.

        :param str img_path: Location of the image file
        :param str text: Text to add to the image
        :param str author: Name of the author text is attributed to
        :param int width: Width of the output of the image
        :return: The path of the newly generated meme image file
        """
        img = Image.open(img_path)

        # Resizing image
        aspect_ratio = img.size[1] / img.size[0]
        img = img.resize((width, int(aspect_ratio * width)))

        # Adding text
        self.draw_text(img, text, author)

        # Saving image file
        file_path = f'meme{random.randint(1111, 9999)}.jpeg'
        img.save(file_path)

        return file_path
