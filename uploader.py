import base64
import json
import os

import requests

import settings

class EDIDUploader(object):
    """
    Uploads a list of EDID files to EDID Catalog.
    """

    post_url = 'http://127.0.0.1:8000/api/upload/'

    def __init__(self):
        self.failed = 0
        self.succeeded = 0
        self.post_url = os.path.join(
            settings.EDID_WEBSITE_ROOT_URL, settings.EDID_WEBSITE_UPLOAD_URL
        )

    def upload(self, edid_list):
        """
        Post EDIDs and parse output.
        """

        req = requests.post(self.post_url, data=self._make_body(edid_list))

        if req.status_code == 200:
            response = req.json()
            self.failed = response['failed']
            self.succeeded = response['succeeded']
        else:
            raise RuntimeError(
                'Uploading failed: %s' % req.text
            )

    def _make_body(self, edid_list):
        """
        Makes post body and returns it encoded in JSON.
        """

        body = {}

        # Add EDIDs
        encoded_edid_list = []
        for edid in edid_list:
            # Encode EDID binary in base64 and add it to the list.
            encoded_edid_list.append(base64.b64encode(edid))

        body['edid_list'] = encoded_edid_list

        return json.dumps(body)
