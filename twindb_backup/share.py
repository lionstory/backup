# -*- coding: utf-8 -*-
"""
Module that works with sharing backups
"""
from __future__ import print_function

from twindb_backup import TwinDBBackupError
from twindb_backup.configuration import get_destination


def share(config, s3_url):
    """
    Function for generate make public file and get public url

    :param config: Config file
    :param s3_url: S3 url to file
    :type s3_url: str
    :raise: TwinDBBackupError
    """
    dst = get_destination(config)
    try:
        print(dst.share(s3_url))
    except NotImplementedError as err:
        raise TwinDBBackupError(err)
