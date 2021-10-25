


def custom_json_datatype_handler(x):
""" 
	Custom type handler for json 
	Usage: in json.dumps( default='custom_json_datatype_handler')
"""
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")
