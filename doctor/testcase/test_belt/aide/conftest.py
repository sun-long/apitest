#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import sys

import pytest

from commonlib import sign_utils
from commonlib.log_utils import log
from commonlib.sign_utils import encode_jwt_token
from defines.belt.face_service_business import FaceSwaggerBusiness




@pytest.fixture(scope='function')
def adapter_CreateAlterDb(config_obj, AdapterApi, cache_obj):
    """ before test create db, after test del db"""
    key = '%s_%s' % (sys._getframe().f_code.co_name, 'CreateAlertDb')
    i=1

    def cache_func():
        #name = "autotest" + sign_utils.getUuid(5)
        resp=AdapterApi.create_NewDb()
        i=1
        #resp = AdapterApi.FaceService_CreatePersonDBPostApi(name=name, description="automation test db")
        db_id = resp.json["db_id"]
        log().info("class db_id:%s" % db_id)


        def clear_func():
            resp = AdapterApi.DeleteDB(db_id=db_id)
            assert resp.status_code == 200

        return db_id, clear_func

    yield cache_obj.get_value(key, func=cache_func)
