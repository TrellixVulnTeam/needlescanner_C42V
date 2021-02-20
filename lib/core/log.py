# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: Liang Ma
# CreatedDate: 2021/1/5 15:37
# Description:

import sys
import logging

from lib.core.enums import CUSTOM_LOGGING

logging.addLevelName(CUSTOM_LOGGING.SYSINFO, '*')
logging.addLevelName(CUSTOM_LOGGING.SUCCESS, '+')
logging.addLevelName(CUSTOM_LOGGING.WARNING, '!')
logging.addLevelName(CUSTOM_LOGGING.ERROR, '-')

LOGGER = logging.getLogger('needle')

LOGGER_HANDLER = None

LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

# try:
#     from pocsuite3.thirdparty.ansistrm.ansistrm import ColorizingStreamHandler
#
#     disableColor = False
#
#     for argument in sys.argv:
#         if "disable-col" in argument:
#             disableColor = True
#             break
#
#     if disableColor:
#         LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
#     else:
#         LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
#         LOGGER_HANDLER.level_map[logging.getLevelName("*")] = (None, "cyan", False)
#         LOGGER_HANDLER.level_map[logging.getLevelName("+")] = (None, "green", False)
#         LOGGER_HANDLER.level_map[logging.getLevelName("-")] = (None, "red", False)
#         LOGGER_HANDLER.level_map[logging.getLevelName("!")] = (None, "yellow", False)
# except ImportError:
#     LOGGER_HANDLER = logging.StreamHandler(sys.stdout)


FORMATTER = logging.Formatter('\r[%(asctime)s] [%(levelname)s] %(message)s', '%H:%M:%S')

LOGGER_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(logging.INFO)

