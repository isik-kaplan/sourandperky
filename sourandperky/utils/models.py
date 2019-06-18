from urllib.request import urlopen

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


def field_image_from_link(instance, field_name, image_name, image_url):
    img_temp = NamedTemporaryFile()
    img_temp.write(urlopen(image_url).read())
    img_temp.flush()

    getattr(instance, field_name).save(image_name+'.jpg', File(img_temp))
