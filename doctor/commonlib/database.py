#!/usr/bin/env python
# -*-coding: utf-8 -*-
import sys

import MySQLdb

from commonlib.log_utils import log


def connect_db(_config):
    """ 连接数据库
    :param _config:
    :return:
    """
    return Database(_config)


class STATUS(object):
    DB_EXEC_OK = 0  # database execute
    DB_EXCEPTION = -1  # database all excetion code.
    DB_CONNECTION_ERROR = -12  # database connection error.
    DB_OPERATION_ERROR = -13  # database operation error.


class Database(object):
    """
    @summary: database operation class.
    """

    def __init__(self, _db_config):
        """
        @note: _db_config MUST be a dict, which MUST contains keys: "host", "user", "port", "passwd", "db".
        -Meanwhile must ensure the type of the key-map-value:
        -    _db_config["host"]   MUST be a string.
        -    _db_config["user"]   MUST be a string.
        -    _db_config["port"]   MUST be a integer.
        -    _db_config["passwd"] MUST be a string.
        -    _db_config["db"]     MUST be a string.
        -Here do not verify the exceptional type no longer.
        """
        # self.log = log

        if not isinstance(_db_config, dict):
            log().warning("database configuration must be a dict.")
            return

        if "host" not in _db_config or \
                "user" not in _db_config or \
                "port" not in _db_config or \
                "passwd" not in _db_config or \
                "db" not in _db_config:
            log().warning("database configuration has problems, please check!")

        self.db_config = _db_config
        self.db_conn = None

    def __del__(self):
        """
        @note: cleanup all db conn
        """
        if self.db_conn is not None:
            self.__close_conn()

    def __close_conn(self):
        """
        @note: close db connection
        """
        try:
            self.db_conn.ping()
        except Exception as e:
            return None

        log().debug("close db connection ...")
        self.db_conn.close()
        return None

    def __get_conn(self):
        """
        @note
        """
        try:
            self.db_conn.ping()
        except Exception as e:
            self.db_conn = self.__connect()
        return self.db_conn

    def __connect(self):
        """
        @summary: connect to database, a private member function.
        @return: connection to database, or None. Judgement is needed.
        """
        retry = 5
        while retry > 0:
            retry -= 1
            try:
                db_conn = MySQLdb.connect(**self.db_config)
                db_conn.autocommit(True)
                log().debug("Connect to database:%s success." % self.db_config["db"])
                return db_conn
            except MySQLdb.Error() as error:
                if retry == 0:
                    raise Exception("Connect to DB failed after 5 retrys")
                else:
                    msg = "Connect to mysql error : %s, trying again......" % (error)
                    log().warning(msg)

    def __execute(self, sql):
        """
        @summary: execute a sql sentence, a private member function.
        @param sql: sql to execute.
        @return:the status of database operation(insert, update).
        -status definition in module conf.statuscode.
        """
        cursor = None
        db_conn = self.__get_conn()

        try:
            cursor = db_conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
        except MySQLdb.Error as e:
            log().warning("FAILED SQL[%s], \n err_msg is %s" % (sql, e))
            return STATUS.DB_EXCEPTION
        log().debug("SUCC SQL[%s]" % sql)
        return STATUS.DB_EXEC_OK

    def execute(self, sql):
        """
        @note:
        """
        return self.__execute(sql)

    def query(self, sql):
        """
        @note: query sql select
        """
        return self.fetchall(sql)

    def update(self, sql):
        """
        @note:
        """
        db_conn = self.__get_conn()
        try:
            db_conn.query(sql)
        except MySQLdb.Error as e:
            log().warning("FAILED SQL[%s], \n err_msg is %s" % (sql, e))
            return STATUS.DB_EXCEPTION

        if db_conn.affected_rows() == 0:
            log().debug("Update error SQL:%s" % sql)
            return STATUS.DB_OPERATION_ERROR

        log().debug("update succ SQL:%s" % sql)
        return STATUS.DB_EXEC_OK

    def insert(self, sql):
        """
        @note
        """
        ret = self.__execute(sql)

        if ret != STATUS.DB_EXEC_OK:
            log().warning("failed insert SQL:%s" % sql)
            return None

        insert_id = self.db_conn.insert_id()

        log().debug("succ insert [id:%s]:%s" % (insert_id, sql))
        return insert_id

    def fetchone(self, sql):
        """
        @summary: execute select sql and just return the first selected result.
        @param sql: selct sql sentence
        @return: return the first selected result, if not None, or return None.
        """
        row = None
        db_conn = self.__get_conn()
        try:
            cursor = db_conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
            row = cursor.fetchone()
            cursor.close()
        except MySQLdb.Error as e:
            log().warning("FAILED SQL[%s], \n err_msg is %s" % (sql, e))
            # return STATUS.DB_EXCEPTION
            return None

        if row is None:
            log().warning("failed query SQL:%s" % sql)
            return None

        log().debug("succ query SQL:%s" % sql)
        return row

    def fetchall(self, sql):
        """
        @summary: execute select sql and return all selected result.
        @param sql: select sql sentence.
        @return: return all selected result, if not None, or return None.
        """
        rows = None
        db_conn = self.__get_conn()
        try:
            cursor = db_conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            cursor.execute(sql)
            rows = cursor.fetchall()
            cursor.close()
        except MySQLdb.Error as e:
            log().warning("FAILED SQL[%s], \n err_msg is %s" % (sql, e))
            # return STATUS.DB_EXCEPTION
            return None

        if type(rows) == tuple and len(rows) == 0:
            # self.warning("failed query SQL:%s" % sql)
            return None

        log().debug("succ query SQL:%s" % sql)
        return rows

    def escape_string(self, unit):
        """
        @note:
        """
        return MySQLdb.escape_string(unit)


if '__main__' == __name__:
    _db_config = {
        "host": "10.0.0.1",
        "user": "root",
        "port": 8306,
        "passwd": "123456",
        "db": "dbname"
    }
    db = Database(_db_config)
