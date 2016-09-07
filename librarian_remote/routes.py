"""
Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

from streamline import XHRPartialFormRoute

from librarian.core.contrib.templates.renderer import template
from librarian.core.exts import ext_container as exts

from .forms import RemoteForm
from .helpers import save_remote_setup


class Remote(XHRPartialFormRoute):
    name = 'remote:setup'
    path = '/remote/'
    template_func = template
    template_name = 'remote/remote'
    partial_template_name = 'remote/_remote'
    form_factory = RemoteForm

    def get_unbound_form(self):
        form_factory = self.get_form_factory()
        data = exts.config.get('remote', {})
        return form_factory(data)

    def form_valid(self):
        params = self.form.processed_data
        dest = exts.config['remote.file']
        save_remote_setup(params, dest)
        exts.setup.append({'remote': dict(self.request.forms)})
