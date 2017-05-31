#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import logging
import aiomysql


def log(sql, arg=()):
    logging.info('SQL: %s' % sql)

@asyncio.coroutine
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool()