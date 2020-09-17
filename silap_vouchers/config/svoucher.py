from __future__ import unicode_literals
from frappe import _

def get_data():

    return [
        {
            "label": _("SILAP Voucher"),
            "icon": "octicon octicon-file-directory",
            "items": [
                {
                    "type": "doctype",
                    "name": "Request Voucher",
                    "label": _("Document"),
                }
            ]
        }
    ]
