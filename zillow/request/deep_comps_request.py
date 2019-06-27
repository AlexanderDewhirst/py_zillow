from py_zillow.zillow.models.place import Place
from py_zillow.zillow.api.error import handle_errors


class DeepCompsRequest(object):
    
    def __init__(self):
        self.principal = Place()
        self.places = []

    def __repr__(self):
        return str(self.__dict__)

    def set_deep_comps_data(self, data):
        handle_errors(data['Comps:comps']['message']['code'])

        result = data['Comps:comps']['response']['properties']
        principal = self.principal
        principal.set_zpid(result['principal']['zpid'])
        principal.links.set_links_data(result['principal'], 'deepcomps')
        principal.address.set_address_data(result['principal'], 'deepcomps')
        principal.zestimate.set_zestimate_data(result['principal'], 'deepcomps')
        principal.local_real_estate.set_local_real_estate_data(result['principal'], 'deepcomps')
        principal.details.set_details_data(result['principal'], 'deepcomps')

        self._map_data_to_places(result['comparables']['comp'])

    def _map_data_to_places(self, response_data):
        for place_data in response_data:
            place = Place()
            self._set_place_data(place, place_data)
            self.places.append(place)

    def _set_place_data(self, place, place_data):
        place.set_zpid(place_data['zpid'])
        place.links.set_links_data(place_data, 'deepcomps')
        place.address.set_address_data(place_data, 'deepcomps')
        place.zestimate.set_zestimate_data(place_data, 'deepcomps')
        place.local_real_estate.set_local_real_estate_data(place_data, 'deepcomps')
        place.details.set_details_data(place_data, 'deepcomps')