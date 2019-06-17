class Choices:
    def __init__(self, choices):
        self.__choices = {
            key: (
                val if not isinstance(val, type(Ellipsis)) else key
            ) for key, val in choices.items()}

        for human_readable, database_value in self.__choices.items():
            setattr(self, human_readable, database_value)

    def __contains__(self, item):
        return item in self.__choices.values() or item in self.__choices.keys()

    @property
    def choices(self):
        return tuple(self.__choices.items())

    def get(self, item, fallback=None):
        return self.__choices.get(item, fallback)

    def __getitem__(self, item):
        return self.__choices[item]
