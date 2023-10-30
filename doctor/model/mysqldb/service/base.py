#!/usr/bin/env python
# -*-coding: utf-8 -*-

class BaseData(object):
    """
    @note: machine
    """

    def __init__(self, dao):
        """
        @note: init func
        """
        self.dao = dao

    def d_add_new_record(self, info):
        """
        :param info:
        :return:
        """
        return self.dao.c_add_new_record(info)

    def d_delete_by_id(self, _id, id_field=None):
        """ 删除一条
        :param _id:
        :param id_field:
        :return:
        """
        return self.dao.c_delete_by_id(_id, id_field=id_field)

    def d_update_by_id(self, _id, info, id_field=None):
        """ 修改一条
        :param id_field:
        :param _id:
        :param info:
        :return:
        """
        return self.dao.c_update_by_id(_id, info, id_field=id_field)

    def d_get_all(self):
        """ 查询所有
        :return:
        """
        return self.dao.c_get_all()

    def d_get_by_id(self, _id, id_field=None):
        """ 查询一条
        :param _id:
        :param id_field:
        :return:
        """
        return self.dao.c_get_by_id(_id, id_field=id_field)


if __name__ == "__main__":
    pass
