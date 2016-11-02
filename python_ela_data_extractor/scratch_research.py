import os
import exifread
import json
import re
import arrow
import math
#import wand
import base64
from PIL import Image, ImageStat, ImageChops, ImageEnhance
from PIL.ExifTags import TAGS, GPSTAGS
from io import BytesIO
import subprocess
import platform


class ImageElaDataExtractor():

    def __init__(self, _file_path):
        self._file_path = _file_path
        self._json_data = dict()
        self._image = None

    @property
    def json(self):
        return json.dumps(self._json_data)

    def execute(self):
        source_buffer = BytesIO()
        compare_buffer = BytesIO()
        self._image = Image.open(self._file_path)
        self._image.save(source_buffer, format='JPEG', quality=100)
        # self._image.save(compare_buffer, format='JPEG', quality=50)
        self._image.save(compare_buffer, format='JPEG', quality=50)

        source = Image.open(BytesIO(source_buffer.getvalue()))
        compare = Image.open(BytesIO(compare_buffer.getvalue()))

        diff_image = ImageChops.difference(source, compare)
        # diff_image = ImageEnhance.Brightness(diff_image).enhance(20.0)
        diff_image = ImageEnhance.Brightness(diff_image).enhance(10.0)
        diff_image.save('../output/out.jpg', format='JPEG', quality=100)

if __name__ == "__main__":
    extractor = ImageElaDataExtractor('../Resources/ela5.jpg')
    extractor.execute()
    print(extractor.json)


