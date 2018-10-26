#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import htwk_logging
from bot import Bot
import handles

####################################
LOG = htwk_logging.create_logger(__name__)

bot = Bot.get()
for handle in handles.HANDLES:
    bot.add_handle(handle)
LOG.info("starting")
bot.start()
LOG.info("stopped")
