#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# :author Sythelux Rikd

import logging
import logging.handlers
import os

BASE_LOG_DIR = "log"

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def create_stream_handler(logger: logging.Logger) -> logging.StreamHandler:
    # create console handler and set level to debug
    sh = logging.StreamHandler()
    sh.setLevel(logger.level)

    # add formatter to sh
    sh.setFormatter(formatter)
    return sh


def create_file_handler(logger: logging.Logger, name: str) -> logging.handlers.RotatingFileHandler:
    if not os.path.exists(BASE_LOG_DIR):
        os.makedirs(BASE_LOG_DIR)
    fh = logging.handlers.RotatingFileHandler(BASE_LOG_DIR + "/" + name + ".log", "a",
                                              100 * 1024 * 1024,
                                              5, "UTF-8", True)
    fh.setLevel(logger.level)
    fh.setFormatter(formatter)
    return fh


def create_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(create_stream_handler(logger))
    logger.addHandler(create_file_handler(logger, name))
    return logger
