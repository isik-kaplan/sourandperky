import os
from glob import glob
from importlib import import_module


def glob_init(name, ignore=None, recursive=True):
    path = '**'
    ignore = ignore or []
    name = name.replace('.', os.sep)
    path = os.sep + path
    modules = []
    for module in glob(name + path, recursive=recursive):
        importable = os.path.splitext(module)[0].replace(os.sep, '.').rstrip('.')
        if any(ignored in importable for ignored in ignore + ['__init__', '__pycache__']):
            continue
        imported = import_module(importable)
        modules.append(imported)
    return modules


class AttrDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    @classmethod
    def from_data(cls, data: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = cls.from_data(value)
        return cls(**data)
