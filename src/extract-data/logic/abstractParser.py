from abc import ABC, abstractmethod
import glob
import os

class AbstractParser(ABC):

    @property
    @abstractmethod
    def cFileExtension(self):
        pass

    Files = []

    
    def GetFiles(self):
        return glob.glob(os.path.dirname(os.path.dirname(__file__)) + "\\asset\\input\\*." + self.cFileExtension) # hate it

    def __init__(self):
        super().__init__()
        self.Files = self.GetFiles()

    @abstractmethod
    def ParseFiles(self):
        pass