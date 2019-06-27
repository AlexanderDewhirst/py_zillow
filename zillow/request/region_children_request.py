from py_zillow.zillow.models.place import Place
from py_zillow.zillow.api.error import handle_errors

class RegionChildrenRequest(object):

    def __init__(self):
        self.region = None
        self.places = []

    def __repr__(self):
        return str(self.__dict__)

    def set_region_children_data(self, data):
        handle_errors(data["RegionChildren:regionchildren"]['message']['code'])

        result = data['RegionChildren:regionchildren']
        self.region = result['response']
        self._map_data_to_places(result['response']['list']['region'], result['request'], result['response']['subregiontype'])

    def _map_data_to_places(self, response_data, request_data, subregion_type):
        for response_place_data in response_data:
            response_place_data[subregion_type] = response_place_data['name']

            place = Place()
            place_data = dict(response_place_data, **request_data)
            self._set_place_data(place, place_data)
            self.places.append(place)
    
    # set place data from request at most recent index
    def _set_place_data(self, place, place_data):
        place.set_zpid(place_data['id'])
        place.address.set_address_data(place_data, 'regionchildren')
        place.zestimate.set_zestimate_data(place_data, 'regionchildren')