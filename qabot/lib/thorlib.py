# thorlib.py
import time
import requests
import os
import logging

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)


class ThorLib:
    def __init__(self):
        # self.thor_instance = thor_instance
        self.base_url = "placeholder.com"
        # Eventually this will be qa.planx-pla.net/thor,
        # while being developed it will be colinyao.planx-pla.net,
        # but we don't have this yet

    def send_get_request(self, url):
        """
        Send a GET request to the given url
        """
        log.debug("sending GET request to {}".format(url))
        r = requests.get(url)
        return "GET request to {} sent".format(url)

    def send_post_request(self, endpoint, body=None):
        """
        Send a POST request to the specified endpoint with the given body
        """
        send_url = self.base_url + endpoint
        log.debug(f"sending POST request to {send_url} with body {body}")
        r = requests.post(send_url, data=body)

        return {"status_code": r.status_code, "body": r.json()}

    def send_put_request(self, url, data):
        """
        Send a PUT request to the given url with the given data
        """
        log.debug("sending PUT request to {}".format(url))
        r = requests.put(url, data=data)
        return "PUT request to {} sent".format(url)
