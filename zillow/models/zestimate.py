from py_zillow.zillow.helpers.api_helpers import APIHelpers as helpers

class Zestimate(object):

    def __init__(self):
        self.amount = None
        self.last_updated = None
        self.low_value = None
        self.high_value = None

    def __repr__(self):
        return str(self.__dict__)

    def set_zestimate_data(self, data, api_method):
        if api_method == 'searchresults' or api_method == "zestimate" or api_method == 'deepsearchresults' or api_method == 'comps' or api_method == 'deepcomps':
            data = data['zestimate']
            self.amount       = data['amount']['#text']
            self.last_updated = helpers.assign_if_present(data, 'last-updated')
            self.low_value    = data['valuationRange']['low']['#text']
            self.high_value   = data['valuationRange']['high']['#text']
        elif api_method == 'regionchildren':
            self.amount       = data['zindex']['#text'] if 'zindex' in data else None