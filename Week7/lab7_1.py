# NOTE: Throughout, if there is an error that you need to deal with
# like the input string was not valid URL, then your function should
# return None.


import requests

def url_verification(url):
    urlx = url[-4:]
    valid_url = [".com",".net",".gov",".edu"]

    if urlx in valid_url:
        return url
    else:
        return None


def basic_request(url):
    a = url_verification(url)

    if a is None:
        return None
    sc = requests.get(url).status_code
    return sc 


def request_user_agent(url, user_agent):
    a = url_verification(url)

    if a is None:
        return None

    if type(user_agent) is not str:
        return None

    return requests.get(url, headers={'User-Agent': user_agent}).text


def request_post(url, dictionary):
    a = url_verification(url)

    if a is None:
        return None

    if dictionary is None or not bool(dictionary) or type(dictionary) is not dict:
        return None

    return requests.post(url, data=dictionary).text