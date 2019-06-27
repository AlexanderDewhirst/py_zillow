from py_zillow.zillow.helpers.api_helpers import APIHelpers as helpers

class Links(object):

    def __init__(self):
        self.home_details = None
        self.graphs_and_data = None
        self.map_this_home = None
        self.comparables = None

    def __repr__(self):
        return str(self.__dict__)

    def set_links_data(self, data, api_method):
        if api_method == "searchresults" or api_method == 'zestimate' or api_method == 'deepsearchresults' or api_method == 'comps' or api_method == 'deepcomps':
            result = data['links']

            self.home_details    = helpers.assign_if_present(result, 'homedetails')
            self.graphs_and_data = helpers.assign_if_present(result, 'graphsanddata')
            self.map_this_home   = helpers.assign_if_present(result, 'mapthishome')
            self.comparables     = helpers.assign_if_present(result, 'comparables')
        elif api_method == "propertydetails":
            result = data['links']
            self.home_details    = helpers.assign_if_present(result, 'homeDetails')
            self.graphs_and_data = helpers.assign_if_present(result, 'photoGallery')