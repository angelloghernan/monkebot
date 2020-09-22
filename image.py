import giphy_client
from giphy_client.rest import ApiException
from google_images_search import GoogleImagesSearch
import random
from pathlib import Path

# create API objects & variables
data_folder = Path("files/")
api_instance = giphy_client.DefaultApi()
api_key = open(data_folder / "giphytoken.txt", "r").readline()

images_key = open(data_folder / "imagestoken.txt", "r").readline()
images_cx = "9afb025346948a6ad"

gis = GoogleImagesSearch(images_key, images_cx)


def get_gif(q: str, rating: str):
    try:
        api_response = api_instance.gifs_random_get(api_key=api_key, tag=q, rating=rating)
        return api_response.data.url
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_random_get: %s\n" % e)


def get_image(q: list, num: int):
    _search_params = {
        'q' : random.choice(q),
        'num': num,
        'safe': 'medium',
        'filetype': 'jpg|png',
        'imgType': 'photo'
    }

    gis.search(search_params=_search_params)
    return random.choice(gis.results()).url

