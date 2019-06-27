from py_zillow.zillow.helpers.api_helpers import APIHelpers as helpers

class Details(object):

    def __init__(self):
        self.bedrooms = None
        self.bathrooms = None
        self.finished_sqft = None
        self.lot_size_sqft = None
        self.year_built = None
        self.num_rooms = None
        self.last_sold_date = None
        self.last_sold_price = None

    def __repr__(self):
        return str(self.__dict__)

    def set_details_data(self, data, api_method):
        if api_method == "propertydetails":
            data = data['editedFacts']
            self.bedrooms        = helpers.assign_if_present(data, 'bedrooms')
            self.bathrooms       = helpers.assign_if_present(data, 'bathrooms')
            self.finished_sqft   = helpers.assign_if_present(data, 'finishedSqFt')
            self.lot_size_sqft   = helpers.assign_if_present(data, 'lotSizeSqFt')
            self.year_built      = helpers.assign_if_present(data, 'yearBuilt')
            self.num_rooms       = helpers.assign_if_present(data, 'numRooms')
            self.last_sold_date  = helpers.assign_if_present(data, 'lastSoldDate')
            # self.last_sold_price = data['lastSoldPrice']
        elif api_method == 'deepsearchresults' or api_method == 'deepcomps':
            self.bedrooms        = helpers.assign_if_present(data, 'bedrooms')
            self.bathrooms       = helpers.assign_if_present(data, 'bathrooms')
            self.finished_sqft   = helpers.assign_if_present(data, 'finishedSqFt')
            self.lot_size_sqft   = helpers.assign_if_present(data, 'lotSizeSqFt')
            self.year_built      = helpers.assign_if_present(data, 'yearBuilt')
            self.num_rooms       = helpers.assign_if_present(data, 'numRooms')
            self.last_sold_date  = helpers.assign_if_present(data, 'lastSoldDate')
            self.last_sold_price = data['lastSoldPrice']['#text']