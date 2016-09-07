"""
Copyright 2014-2015, Outernet Inc.
Some rights reserved.

This software is free software licensed under the terms of GPLv3. See COPYING
file that comes with the source code, or http://www.gnu.org/licenses/gpl.txt.
"""

import os


KEYS = ('key', 'hostname', 'host', 'port')


def save_remote_setup(params, dest):
    """
    Write the passed in dict of key-value pairs into the remote file with the
    keys converted to uppercase form.
    """
    contents = '\n'.join('{key}="{value}"'.format(key=k.upper(), value=v)
                         for (k, v) in params.items() if v and k in KEYS)
    if not contents or not params['enabled']:
        # remove config file when it's empty or should be disabled
        if os.path.exists(dest):
            os.remove(dest)
        return
    # there is configuration to be stored
    with open(dest, 'w') as remote_file:
        remote_file.write(contents)
