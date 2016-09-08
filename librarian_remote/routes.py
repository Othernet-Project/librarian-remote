"""
Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

import logging
import os

from bottle_utils.i18n import lazy_gettext as _
from streamline import XHRPartialFormRoute

from librarian.core.contrib.templates.renderer import template
from librarian.core.exts import ext_container as exts

from .forms import RemoteForm
from .helpers import save_remote_setup


def restart_services(commands):
    """
    Execute the given sequence of commands that will restart the necessary
    services to enable / disable remote access.
    """
    logging.info('Restarting remote services')
    for cmd in commands:
        logging.debug('Executing command: "%s"', cmd)
        ret = os.system(cmd)
        if ret:
            logging.debug('"%s" returned %s', cmd, ret)


class Remote(XHRPartialFormRoute):
    name = 'remote:setup'
    path = '/remote/'
    template_func = template
    template_name = 'remote/remote'
    partial_template_name = 'remote/_remote_form'
    form_factory = RemoteForm

    def get_unbound_form(self):
        form_factory = self.get_form_factory()
        data = exts.config.get('remote', {})
        return form_factory(data)

    def form_valid(self):
        params = self.form.processed_data
        dest = exts.config['remote.file']
        # store configuration in both setup and REMOTE file
        save_remote_setup(params, dest)
        exts.setup.append({'remote': params})
        # restart remote services
        commands = self.config['remote.restart_commands']
        exts.tasks.schedule(restart_services, args=(commands,), delay=5)
        return dict(message=_("Remote access settings have been saved."))
