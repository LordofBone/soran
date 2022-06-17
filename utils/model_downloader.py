import gdown
from config.tensorflowasr import *


def download_models():
    url = "https://drive.google.com/file/d/1d3OukHeysMKMfaGZUJ2JPO06yVzqVhWy/view?usp=sharing"
    gdown.download(url, model, quiet=False, fuzzy=True)

    url = "https://drive.google.com/file/d/1NNo-IRvBlZJsRB51eNr5yGYRzSyqfCk1/view?usp=sharing"
    gdown.download(url, subwords_file, quiet=False, fuzzy=True)


if __name__ == "__main__":
    download_models()
