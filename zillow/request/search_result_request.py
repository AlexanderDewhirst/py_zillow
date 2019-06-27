from py_zillow.zillow.models.place import Place
from py_zillow.zillow.api.error import handle_errors

class SearchResultRequest(object):

    def __init__(self):
        self.place = Place()

    def __repr__(self):
        return str(self.__dict__)

    def set_search_result_data(self, data):
        handle_errors(data['SearchResults:searchresults']['message']['code'])

        result = data['SearchResults:searchresults']['response']['results']['result']
        place = self.place
        place.set_zpid(result['zpid'])
        place.links.set_links_data(result, 'searchresults')
        place.address.set_address_data(result, 'searchresults')
        place.zestimate.set_zestimate_data(result, 'searchresults')
        place.local_real_estate.set_local_real_estate_data(result, 'searchresults')