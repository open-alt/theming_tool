from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Elements & Fonts"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Element",
                    "label": _("Elements"),
                    "description": _("Create an Element."),
                },
                {
                    "type": "doctype",
                    "name": "System Font",
                    "label": _("System Fonts"),
                    "description": _("Create a font."),
                }
            ]
        },
        {
            "label": _("Theme Settings"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Theme Settings",
                    "label": _("Theme Settings"),
                    "description": _("Edit Theme settings"),
                }
            ]
        },
    ]
