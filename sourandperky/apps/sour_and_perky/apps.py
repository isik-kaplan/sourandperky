from django.apps import AppConfig

from utils.utils import glob_init


class SourAndPerkyConfig(AppConfig):
    name = 'apps.sour_and_perky'

    def ready(self):
        glob_init('apps.sour_and_perky.signals',)
        glob_init('apps.sour_and_perky.checks',)
        glob_init('apps.sour_and_perky.admin',)

