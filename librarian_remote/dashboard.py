"""
Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

from bottle_utils.i18n import lazy_gettext as _

from librarian.core.exts import ext_container as exts
from librarian.presentation.dashboard.dashboard import DashboardPlugin

from .forms import RemoteForm


class RemoteDashboardPlugin(DashboardPlugin):
    # Translators, used as dashboard section title
    heading = _('Remote Access Setup')
    name = 'remote'

    def get_template(self):
        return self.name + '/dashboard.tpl'

    def get_context(self):
        data = exts.config.get('remote', {})
        form = RemoteForm(data)
        return dict(form=form)
