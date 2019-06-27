from py_zillow.zillow.models.zestimate         import Zestimate
from py_zillow.zillow.models.links             import Links
from py_zillow.zillow.models.local_real_estate import LocalRealEstate
from py_zillow.zillow.models.address           import Address
from py_zillow.zillow.models.details           import Details

class Place(object):

    def __init__(self):
        self.zpid              = None
        self.links             = Links()
        self.address           = Address()
        self.zestimate         = Zestimate()
        self.local_real_estate = LocalRealEstate()
        self.details           = Details()
        # self.similarity_score = None

    def __repr__(self):
        return str(self.__dict__)

    def set_zpid(self, zpid):
        self.zpid = zpid