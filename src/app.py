import random
import os
import requests
from flask import Flask, render_template, abort, request


from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes_ = []
    for f in quote_files:
        quotes_.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    # images within the images images_path directory
    for root, dirs, files in os.walk(images_path):
        imgs_ = [os.path.join(root, name) for name in files]

    return quotes_, imgs_


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    if not request.form.get('image_url'):
        abort(404)
    url = request.form.get('image_url')
    image = requests.get(url)

    temp_image = 'temp_image.jpg'
    with open(temp_image, 'wb') as img:
        img.write(image.content)

    quote = request.form.get('body')
    author = request.form.get('author')

    path = meme.make_meme(temp_image, quote, author)
    os.remove(temp_image)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
