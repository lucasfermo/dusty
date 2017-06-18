import math,random,operator
from collections import Container
import abc

class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls,C):
        if cls is MediaLoader:
            attrs=set(dir(c))
            if set(cls.__abstractmethods__)<=attrs:
                return True

        return True

class Wav(MediaLoader):
    pass

class Ogg(MediaLoader):
    ext= '.ogg'
    """def play(self):
        pass"""

x=Ogg()
