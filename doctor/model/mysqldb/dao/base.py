#!/usr/bin/env python
# -*-coding: utf-8 -*-
from commonlib.sql import SQL


class BaseDao(SQL):
    """
    @note: base model
    """

    def __init__(self, db, table_name):
        """
        @note: init func
        """
        self.db = db
        self.table_name = table_name
        super(BaseDao, self).__init__()

    def c_add_new_record(self, info):
        """ 增加一条
        @note: add new record
        """
        return self.data(info).add()

    def c_delete_by_id(self, _id, id_field=None):
        """ 删除一条
        :param _id:
        :param id_field:
        :return:
        """
        if not id_field:
            id_field = "id"
        where = "%s = '%s'" % (id_field, _id)
        return self.where(where).delete()

    def c_update_by_id(self, _id, info, id_field=None):
        """ 修改一条
        :param id_field:
        :param _id:
        :param info:
        :return:
        """
        if not id_field:
            id_field = "id"
        where = "%s = '%s'" % (id_field, _id)
        return self.where(where).data(info).save()

    def c_get_all(self):
        """ 查询所有
        :return:
        """
        return self.select()

    def c_get_by_id(self, _id, id_field=None):
        """ 查询一条
        :param _id:
        :param id_field:
        :return:
        """
        if not id_field:
            id_field = "id"
        where = "%s = '%s'" % (id_field, _id)
        if id_field:
            return self.where(where).select()
        else:
            return self.where(where).find()