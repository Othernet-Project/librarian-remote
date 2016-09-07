"""
Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

from bottle_utils import form
from bottle_utils.i18n import lazy_gettext as _


class RemoteForm(form.Form):
    # Translators, used as label for a form field
    key = form.StringField(_("Key"))
    # Translators, used as label for a form field
    hostname = form.StringField(_("Hostname"))
    # Translators, used as label for a form field
    host = form.StringField(_("Host"))
    # Translators, used as label for a form field
    port = form.IntegerField(_("Port"))
    # Translators, used as label for a form field
    enabled = form.BooleanField(_("Enabled"), value='yes')

    def preprocess_port(self, value):
        return value if value else None
