import os
from PIL import Image


class PhotoPuter:

    def __init__(self):
        self.fileExtension = (".png", ".jpg", ".jpeg")
        self.inDirectory = f"{os.path.dirname(os.path.abspath(__file__))}/images"
        self.outDirectory = f"{os.path.dirname(os.path.abspath(__file__))}/results"
        self.watermark = Image.open("logo.png")
        self.width = self.watermark.width
        self.height = self.watermark.height

    def start(self):
        pictures = self.getPhotosFromDirectory()
        self.process_images(pictures)

    def getPhotosFromDirectory(self):
        photos = [f for f in os.listdir(
            self.inDirectory) if f.endswith(self.fileExtension)]
        return photos

    def process_images(self, images):
        for image in images:
            image_name, ext = str(image).split(".")
            image = Image.open(f"{self.inDirectory}/{image}")
            image_width = image.width
            image_height = image.height
            image.paste(self.watermark,
                        (int((image_width - self.width) / 2),
                         int((image_height - self.height) / 2)))
            image.save(f'{self.outDirectory}/marked_{image_name}.{ext}')


def main():
    process1 = PhotoPuter()
    process1.start()


if __name__ == "__main__":
    main()
