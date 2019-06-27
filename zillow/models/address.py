from py_zillow.zillow.helpers.api_helpers import APIHelpers as helpers

class Address(object):

    def __init__(self):
        self.street    = None
        self.city      = None
        self.state     = None
        self.zipcode   = None
        self.latitude  = None
        self.longitude = None

    def __repr__(self):
        return str(self.__dict__)
    
    def set_street(self, value):
        self.street = value

    def set_zipcode(self, value):
        self.zipcode = value

    def set_city(self, value):
        self.city = value

    def set_state(self, value):
        self.state = value

    def set_address_data(self, data, api_method):
        if api_method == 'searchresults' or api_method == 'propertydetails' or api_method == 'zestimate' or api_method == 'deepsearchresults' or api_method == 'comps' or api_method == 'deepcomps':
            data = data['address']
            self.street    = helpers.assign_if_present(data, 'street')
            self.city      = helpers.assign_if_present(data, 'city')
            self.state     = helpers.assign_if_present(data, 'state')
            self.zipcode   = helpers.assign_if_present(data, 'zipcode')
            self.latitude  = helpers.assign_if_present(data, 'latitude')
            self.longitude = helpers.assign_if_present(data, 'longitude')
        elif api_method == 'regionchildren':
            self.street    = helpers.assign_if_present(data, 'address')
            self.city      = helpers.assign_if_present(data, 'city')
            self.state     = helpers.assign_if_present(data, 'state')
            self.zipcode   = helpers.assign_if_present(data, 'zipcode')
            self.latitude  = helpers.assign_if_present(data, 'latitude')
            self.longitude = helpers.assign_if_present(data, 'longitude')