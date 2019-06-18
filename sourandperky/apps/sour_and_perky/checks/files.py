import contextlib
import pathlib

from django.conf import settings
from django.core.checks import register, Tags, Debug
import os.path


class FileSystemTags(Tags):
    paths_exist = 'paths_exist'


@register(FileSystemTags.paths_exist)
def check_paths_exist(app_configs=None, **kwargs):
    """
    Check if the required file and folders exist, and try to create the possible ones.
    """

    REQUIRED_PATHS = [
        settings.MEDIA_ROOT,
        settings.STATIC_ROOT,
        os.path.join(settings.MEDIA_ROOT, 'avatars')
    ]
    errors = []

    def created_the_absent(file, error_id):
        errors.append(
            Debug(
                msg='"{}" could not be found but successfully created'.format(file),
                id='apps.sour_and_perky.D{}'.format(str(error_id).zfill(3)),
            )
        )

    for index, path in enumerate(REQUIRED_PATHS):
        path = pathlib.Path(path)
        if not path.exists():
            with contextlib.suppress(FileExistsError):
                path.mkdir(parents=True)
                created_the_absent(path, index)

    return errors
