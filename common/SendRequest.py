import logging

import requests


class SendRequest:
    sess = requests.session()

    def __init__(self, args):
        self.url = args['request']['url']
        self.method = args['request']['method']

    def send_all_request(self, **kwargs):
        response = SendRequest.sess.request(method=self.method, url=self.url, **kwargs)
        logging.info(self.method)
        return response
