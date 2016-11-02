# -*- coding: utf-8 -*-
import ConfigParser
import glob
import logging
import os

__author__ = 'TwinDB Development Team'
__email__ = 'dev@twindb.com'
__version__ = '2.1.4'

log = logging.getLogger(__name__)


def setup_logging(logger, debug=False):

    fmt_str = "%(asctime)s: %(levelname)s:" \
              " %(module)s.%(funcName)s():%(lineno)d: %(message)s"

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(logging.Formatter(fmt_str))
    logger.handlers = []
    logger.addHandler(console_handler)
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)


def get_directories_to_backup(config):
    backup_dirs = []
    try:
        backup_dirs_value = config.get('source', 'backup_dirs')
        backup_dirs = backup_dirs_value.strip('"\'').split()
        log.debug('Directories to backup %r', backup_dirs)

    except ConfigParser.NoOptionError:
        log.debug('Not backing up files')

    return backup_dirs


def get_files_to_delete(all_files, keep_copies):
    log.debug('Retain %d files', keep_copies)
    if keep_copies == 0:
        return all_files
    else:
        return all_files[:-keep_copies]


def delete_local_files(dir_backups, keep_copies):
    local_files = sorted(glob.glob(dir_backups))
    log.debug('Local copies: %r', local_files)

    for fl in get_files_to_delete(local_files, keep_copies):
        log.debug('Deleting: %s', fl)
        os.unlink(fl)