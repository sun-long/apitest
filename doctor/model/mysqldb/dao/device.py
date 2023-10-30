#!/usr/bin/env python
# -*-coding: utf-8 -*-

from model.mysqldb.dao.base import BaseDao


class DeviceDao(BaseDao):
    """
    @note: base model
    """

    def __init__(self, db):
        """
        @note: init func
        """
        table_name = "device"
        super(DeviceDao, self).__init__(db, table_name)