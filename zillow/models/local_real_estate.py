from py_zillow.zillow.helpers.api_helpers import APIHelpers as helpers

class LocalRealEstate(object):

    def __init__(self):
        self.region = None

    def __repr__(self):
        return str(self.__dict__)
    
    def set_local_real_estate_data(self, data, api_method):
        if api_method == 'searchresults' or api_method == 'zestimate' or api_method == 'comps' or api_method == 'deepcomps':
            result = data['localRealEstate']
            self.region = helpers.assign_if_present(result, 'region')