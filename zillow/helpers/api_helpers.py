class APIHelpers(object):

    def assign_if_present(dict_obj, key):
        return dict_obj[key] if key in dict_obj else None