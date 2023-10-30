#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   conftest.py    
@Contact :   wangan@sensetime.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/11/10 下午2:58   wangan      1.0         None
'''
import pytest


@pytest.fixture(scope='function')
def appletConfigStr():
    config_str = "{\"type_url\":\"com.sensetime.algo.face.liveness\",\"value\":\"{\\\"$schema\\\":\\\"http://json-schema.org/draft-07/schema#\\\",\\\"type\\\":\\\"object\\\",\\\"additionalProperties\\\":false,\\\"definitions\\\":{\\\"VERTEX\\\":{\\\"type\\\":\\\"object\\\",\\\"properties\\\":{\\\"x\\\":{\\\"description\\\":\\\"horizontal position ratio\\\",\\\"type\\\":\\\"number\\\",\\\"minimum\\\":0,\\\"maximum\\\":1},\\\"y\\\":{\\\"description\\\":\\\"vertical position ratio\\\",\\\"type\\\":\\\"number\\\",\\\"minimum\\\":0,\\\"maximum\\\":1}},\\\"required\\\":[\\\"x\\\",\\\"y\\\"]},\\\"VERTEX_ARRAY\\\":{\\\"type\\\":\\\"array\\\",\\\"items\\\":{\\\"description\\\":\\\"vertex use ratio position\\\",\\\"$ref\\\":\\\"#/definitions/VERTEX\\\"},\\\"minItems\\\":3,\\\"maxItems\\\":100},\\\"POLYGON\\\":{\\\"type\\\":\\\"object\\\",\\\"properties\\\":{\\\"vertices\\\":{\\\"description\\\":\\\"series of vertex form one polygon\\\",\\\"$ref\\\":\\\"#/definitions/VERTEX_ARRAY\\\"}}},\\\"POLYGON_ARRAY\\\":{\\\"type\\\":\\\"array\\\",\\\"items\\\":{\\\"description\\\":\\\"polygon as one area\\\",\\\"$ref\\\":\\\"#/definitions/POLYGON\\\"},\\\"minItems\\\":0,\\\"maxItems\\\":10},\\\"ROI\\\":{\\\"type\\\":\\\"object\\\",\\\"properties\\\":{\\\"vertices\\\":{\\\"description\\\":\\\"Polygon vertices compatibility implement, a single include polygon\\\",\\\"$ref\\\":\\\"#/definitions/VERTEX_ARRAY\\\"},\\\"include\\\":{\\\"description\\\":\\\"multiple union polygons as one area\\\",\\\"$ref\\\":\\\"#/definitions/POLYGON_ARRAY\\\"},\\\"exclude\\\":{\\\"description\\\":\\\"multiple union polygons as one area\\\",\\\"$ref\\\":\\\"#/definitions/POLYGON_ARRAY\\\"}}}},\\\"properties\\\":{\\\"filters\\\":{\\\"type\\\":\\\"object\\\",\\\"properties\\\":{\\\"detect_topk\\\":{\\\"type\\\":\\\"number\\\",\\\"minimum\\\":1,\\\"maximum\\\":5},\\\"reserve\\\":{\\\"type\\\":\\\"boolean\\\"},\\\"detect_roi\\\":{\\\"$ref\\\":\\\"#/definitions/ROI\\\"},\\\"quality_threshold\\\":{\\\"type\\\":\\\"number\\\",\\\"minimum\\\":0,\\\"maximum\\\":1},\\\"min_width\\\":{\\\"type\\\":\\\"number\\\",\\\"minimum\\\":0,\\\"maximum\\\":4000},\\\"min_height\\\":{\\\"type\\\":\\\"number\\\",\\\"minimum\\\":0,\\\"maximum\\\":4000},\\\"min_width_ratio\\\":{\\\"type\\\":\\\"number\\\",\\\"minimum\\\":0,\\\"maximum\\\":1},\\\"min_height_ratio\\\":{\\\"type\\\":\\\"number\\\",\\\"minimum\\\":0,\\\"maximum\\\":1}}},\\\"stages\\\":{\\\"type\\\":\\\"array\\\",\\\"items\\\":{\\\"description\\\":\\\"optional stages\\\",\\\"type\\\":\\\"string\\\",\\\"enum\\\":[\\\"headpose\\\",\\\"eyestate\\\",\\\"feature\\\",\\\"liveness\\\",\\\"defake\\\"]},\\\"minItems\\\":1,\\\"maxItems\\\":100}}}\"}"
    return config_str

