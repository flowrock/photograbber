import urllib
from json_finder import _parse_json
import requests
import urlparse

class safe_urlopen(object):
    def __init__(self, *args, **kwargs):
        self.file_resp = urllib.urlopen(*args, **kwargs)

    def __enter__(self):
        return self.file_resp 
    
    def __exit__(self, type, value, traceback):
        self.file_resp.close()

def http_request(base_url, path, post_args, log_request=False, **kwargs):
    post_data = None if post_args is None else urllib.urlencode(post_args)
    encoded_kwargs = smart_urlencode(kwargs)
    full_url = base_url + path + "?" + encoded_kwargs
    if log_request:
        from time import time
        print time()
        print full_url
    with safe_urlopen(full_url, post_data) as file_resp:
        file_contents = file_resp.read()
        if log_request:
            from time import time
            print time()
            print file_contents[:40]
        response = None
        try:
            response = _parse_json(file_contents)
        except:
            print file_contents
            print full_url
    return response

def smart_urlencode(kwargs):
    for key in kwargs:
        array = type(kwargs[key]) in (list, tuple)
        if array:
            new_key = key + '[]'
            kwargs[new_key] = kwargs[key]
            del(kwargs[key])
    return urllib.urlencode(kwargs, True)

def paginate(skip, rpp, request_function, title, total_pages=5):
    page = 1
    if skip:
        page = skip / rpp
        skip -= page * rpp
        page += 1
        assert(skip >= 0) 
    while True:
        data = request_function(page=page, rpp=rpp)
        for thing in data[title]:
            if skip:
                skip -= 1
                continue
            yield thing
        if page == total_pages:
            break
        page += 1
