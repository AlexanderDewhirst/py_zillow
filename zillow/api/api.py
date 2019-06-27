import requests
import xmltodict
from py_zillow.zillow.request.search_result_request         import SearchResultRequest
from py_zillow.zillow.request.deep_search_result_request    import DeepSearchResultRequest
from py_zillow.zillow.request.property_details_request      import PropertyDetailsRequest
from py_zillow.zillow.request.region_children_request       import RegionChildrenRequest
from py_zillow.zillow.request.zestimate_request             import ZestimateRequest
from py_zillow.zillow.request.comps_request                 import CompsRequest
from py_zillow.zillow.request.deep_comps_request            import DeepCompsRequest
from urllib.parse import urlparse, urlunparse, urlencode


class ValuationAPI(object):

    def __init__(self):
        self.base_url = "https://www.zillow.com/webservice"
        self._input_encoding  = None
        self._request_headers = None
        self.__auth           = None
        self._timeout         = None

    def get_updated_property_details(self, zws_id, zpid):
        url = '%s/GetUpdatedPropertyDetails.htm' % (self.base_url)
        parameters = { 'zws-id': zws_id, 'zpid': zpid }

        resp = self._request_url(url, 'GET', data = parameters)
        data = resp.content.decode('utf-8')
        xmltodict_data = xmltodict.parse(data)
        property_details = PropertyDetailsRequest()
        try:
            property_details.set_property_details_data(xmltodict_data)
        except:
            raise BaseException("UpdatePropertyDetails Instantiation Failed.")
        return property_details
        
    
    def get_region_children(self, zws_id, region_id = None, state = None, county = None, city = None, childtype = None):
        # TODO handling for region_id and county
        url = '%s/GetRegionChildren.htm' % (self.base_url)
        parameters = { 'zws-id': zws_id }
        if state:
            parameters['state'] = state
        if city:
            parameters['city'] = city
        if county:
            parameters['county'] = county
        
        resp = self._request_url(url, 'GET', data = parameters)
        data = resp.content.decode('utf-8')
        xmltodict_data = xmltodict.parse(data)
        region_children = RegionChildrenRequest()
        try:
            region_children.set_region_children_data(xmltodict_data)
        except:
            raise BaseException("RegionChildren Instantiation Failed.")
        return region_children

    def get_search_results(self, zws_id, address_city_state, zip_code, rentzestimate = False):
        url = '%s/GetSearchResults.htm' % (self.base_url)
        parameters = { 'zws-id': zws_id, 'rentzestimate': rentzestimate }
        if address_city_state and zip_code:
            parameters['address'] = address_city_state
            parameters['citystatezip'] = zip_code

        resp = self._request_url(url, 'GET', data = parameters)
        data = resp.content.decode('utf-8')
        xmltodict_data = xmltodict.parse(data)
        search_result = SearchResultRequest()
        try:
            search_result.set_search_result_data(xmltodict_data)
        except:
            raise BaseException("SearchResult Instantiation Failed.")
        return search_result

    def get_deep_search_results(self, zws_id, address_city_state, zip_code, rentzestimate = False):
        url = '%s/GetDeepSearchResults.htm' % (self.base_url)
        parameters = { 'zws-id': zws_id, 'rentzestimate': rentzestimate }
        if address_city_state and zip_code:
            parameters['address'] = address_city_state
            parameters['citystatezip'] = zip_code

        resp = self._request_url(url, 'GET', data = parameters)
        data = resp.content.decode('utf-8')
        xmltodict_data = xmltodict.parse(data)
        deep_search_result = DeepSearchResultRequest()
        try:
            deep_search_result.set_deep_search_results_data(xmltodict_data)
        except:
            raise BaseException("")
        return deep_search_result

    def get_zestimate(self, zws_id, zpid, rentzestimate = False):
        url = '%s/GetZestimate.htm' % (self.base_url)
        parameters = { 'zws-id': zws_id, 'zpid': zpid, 'rentzestimate': rentzestimate }

        resp = self._request_url(url, 'GET', data = parameters)
        data = resp.content.decode('utf-8')
        xmltodict_data = xmltodict.parse(data)
        zestimate = ZestimateRequest()
        try:
            zestimate.set_zestimate_data(xmltodict_data)
        except:
            raise BaseException("Zestimate Instantiation Failed.")
        return zestimate

    def get_comps(self, zws_id, zpid, count, rentzestimate = False):
        url = '%s/GetComps.htm' % (self.base_url)
        parameters = { 'zws-id': zws_id, 'zpid': zpid, 'count': count, 'rentzestimate': rentzestimate }

        resp = self._request_url(url, 'GET', data = parameters)
        data = resp.content.decode('utf-8')
        xmltodict_data = xmltodict.parse(data)

        comps = CompsRequest()
        try:
            comps.set_comps_data(xmltodict_data)
        except:
            raise BaseException('Comps Instantiation Failed')
        return comps

    def get_deep_comps(self, zws_id, zpid, count, rentzestimate = False):
        url = '%s/GetDeepComps.htm' % (self.base_url)
        parameters = { 'zws-id': zws_id, 'zpid': zpid, 'count': count, 'rentzestimate': rentzestimate }

        resp = self._request_url(url, 'GET', data = parameters)
        data = resp.content.decode('utf-8')
        xmltodict_data = xmltodict.parse(data)

        deep_comps = DeepCompsRequest()
        try:
            deep_comps.set_deep_comps_data(xmltodict_data)
        except:
            raise BaseException('DeepComps Instantiation Failed')
        return deep_comps

    def _request_url(self, url, verb, data = None):
        if verb == 'GET':
            url = self._build_url(url, extra_params = data)
            try:
                get_route = requests.get(
                    url,
                    auth = self.__auth,
                    timeout = self._timeout
                )
                return get_route
            except:
                raise BaseException("Request Failed.")
        return 0

    def _build_url(self, url, path_elements = None, extra_params = None):
        (scheme, netloc, path, params, query, fragment) = urlparse(url)

        if path_elements:
            p = [i for i in path_elements if i]
            if not path.endswith('/'):
                path += '/'
            path += "/".join(p)

        if extra_params and len(extra_params) > 0:
            extra_query = self._encode_parameters(extra_params)
            if query:
                query += '&' + extra_query
            else:
                query = extra_query

        return urlunparse((scheme, netloc, path, params, query, fragment))
    
    def _encode_parameters(self, parameters):
        if parameters is None:
            return None
        else:
            url_to_encode = dict([(k, self._encode(v)) for k, v in list(parameters.items()) if v is not None])
            return urlencode(url_to_encode)

    def _encode(self, s):
        if self._input_encoding:
            return str(s, self._input_encoding).encode('utf-8')
        else:
            return str(s).encode('utf-8')