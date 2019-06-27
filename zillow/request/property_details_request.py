from py_zillow.zillow.models.place import Place
from py_zillow.zillow.api.error import handle_errors


class PropertyDetailsRequest(object):

    def __init__(self):
        self.place = Place()

    def __repr__(self):
        return str(self.__dict__)

    def set_property_details_data(self, data):
        handle_errors(data['UpdatedPropertyDetails:updatedPropertyDetails']['message']['code'])

        result = data['UpdatedPropertyDetails:updatedPropertyDetails']['response']
        place = self.place
        place.set_zpid(result['zpid'])
        place.links.set_links_data(result, 'propertydetails')
        place.address.set_address_data(result, 'propertydetails')
        place.details.set_details_data(result, 'propertydetails')