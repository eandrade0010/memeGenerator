"""Module manipulates and draws text onto images."""

from PIL import Image, ImageDraw, ImageFont
import textwrap
import random

import os


class MemeEngine:
    """Class will input an image and a random QuoteModel object and return a meme. """

    def __init__(self, path):
        """Initialize and add path of original image file to state."""
        self.image = path

    @staticmethod
    def draw_text(img: Image, body, author, font_size=32):
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

        # Positioning and formatting of body text
        pos_y = img.height/16
        lines = textwrap.wrap(body, width=35)
        for line in lines:
            left, top, right, bottom = font.getbbox(line.upper())
            width, height = (right - left, bottom - top)
            draw.text(((img.width - width) / 2, pos_y), line.upper(), font=font, fill=text_color)
            pos_y += height

        # Positioning and formatting of author text
        pos_y = 14*(img.height / 16)
        lines = textwrap.wrap(author, width=35)
        for line in lines:
            left, top, right, bottom = font.getbbox(line.upper())
            width, height = (right - left, bottom - top)
            draw.text(((img.width - width) / 2, pos_y), line.upper(), font=font, fill=text_color)
            pos_y += height

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
        rel_path = os.path.join(self.image, file_path)
        img.save(rel_path)

        return rel_path
