from py_zillow.zillow.models.place import Place
from py_zillow.zillow.api.error import handle_errors

class ZestimateRequest(object):

    def __init__(self):
        self.place = Place()

    def __repr__(self):
        return str(self.__dict__)

    def set_zestimate_data(self, data):
        handle_errors(data["Zestimate:zestimate"]['message']['code'])
        
        result = data['Zestimate:zestimate']['response']
        place = self.place
        place.set_zpid(result['zpid'])
        place.links.set_links_data(result, 'zestimate')
        place.address.set_address_data(result, 'zestimate')
        place.zestimate.set_zestimate_data(result, 'zestimate')
        place.local_real_estate.set_local_real_estate_data(result, 'zestimate')
