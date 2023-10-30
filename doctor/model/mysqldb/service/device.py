#!/usr/bin/env python
# -*-coding: utf-8 -*-

from model.mysqldb.dao.device import DeviceDao
from model.mysqldb.service.base import BaseData


class DeviceData(BaseData):
    """
    @note: device
    """

    def __init__(self, db):
        """
        @note: init func
        """
        self.dao = DeviceDao(db)
        super(DeviceData, self).__init__(self.dao)


if __name__ == "__main__":
    pass