from bs4 import BeautifulSoup
import pandas as pd

class Dictionary:
    '''Get values from LDOCE Dictionary'''

    def __init__(self, string):
        super(Dictionary, self).__init__()
        self.string = string
        self.bsObj = BeautifulSoup(self.string, 'html.parser')

    def get_pos(self):
        try:
            namelist = self.bsObj.find('span', {'class':'pos'}).get_text()
        except AttributeError:
            namelist = None
        return namelist

    def get_gram(self):
        try:
            namelist = self.bsObj.find('span', {'class':'GRAM'}).get_text()
        except AttributeError:
            namelist = None
        return namelist

    def get_inflections(self):
        try:
            namelist = self.bsObj.findall('span', {'class':'Inflections'})
            for name in namelist:
                return name
        except AttributeError:
            namelist = None
            return namelist

    def get_vf(self):
        try:
            namelist = self.bsObj.findall('span', {'class':'vf'})
            for name in namelist:
                return name
        except AttributeError:
            namelist = None
            return namelist