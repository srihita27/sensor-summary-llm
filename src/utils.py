import os


def create_directories():

    folders = [

        "data",

        "data/raw",

        "data/processed",

        "outputs"

    ]

    for folder in folders:

        os.makedirs(folder, exist_ok=True)