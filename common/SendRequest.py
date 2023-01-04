import logging

import requests


class SendRequest:
    sess = requests.session()

    @staticmethod
    def send_all_request(method, url, **kwargs):
        response = SendRequest.sess.request(method, url, **kwargs)
        logging.info(method)
        return response
