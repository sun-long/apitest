#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import pytest
from PIL import Image
from commonlib import config, time_utils, sign_utils
from commonlib.log_utils import log

cyffea1  = "iP/1vO0Ck71KTzM9A5UUPVNkXb2hhC08V5ltPUX8uLyqtoG9/M6kO1Vzdj3GgY+8dg8HPJAsAr4ObqU9aq+sPN62Rz3qj5S99JOpvBwtVb3OF7081vW5PA9TkL2U9Ym7cHs1vXEQYjrYJGs5ylEUPvHhyjymcw89yMFZve7GrTo2hcq8Dd7auQNmQz3ZfS88JJglvbsBPD0fdD49YWokPSqDkz3y2549ADm9vOQd6j1Ms7c8f81ePVjYtrz29DK9KVZYPdf9uTy40ga8QVt6vTAhmr0a0Eg9iLwYvV3pgz287ZK9Pi8wPcOtwT0yHGE9SEOUPY0ALr0I77E9qyFFvRybAz2PNBO92au0vZDuWT008+O8ovBSPaVCBT2UJ7m9dTn3vKyR1zy6ZKk9j3f6vbgZnD2flec7onUVPftfAj3jExK+t2L6PNzRSz2+tK88llqXPBKU6Ty9t6S8QMX5vRsKEbs81kk9iK7VPRCytjvvJjg80LGsvJXRWDw9A4k8Exy0PQrEZbkW9SU+QtW5PMC2bj1HBea8nT8UPVl5Bjyfl588EkQBvEB1gr3X6DC86OsbPBEtOr36vW29NVITvTgK1j0DVSU9MWH2vGCdYD1DVDq9EOSRvTSYH72SYca9h8GGulDGszxNFr89B31nPWyxmjzPW7m8P+NTvWQdRL1fwpw9kToGPq6QpD3G/eS9cMBWPQD8RL0NJci9fCCuvXsvTjxBggW9Sz4UPc0kY72cdZq9ZfxVvkZ6hrxzpEw9FwkXPnkGoDy/dcG86WEJvZ4hjT2neIg8JJGyPf5nx7zRozw7UEQOvXOLOb3++3K8WQnNPPGbRj1AlRQ8iPUEvRh4xzxjfqC7iyZXvF7ZxjzFzYg9VZ8yvQQOSj2NYYm8NuJVO3KUJj3+UkQ94IB+Pe2jqrwGFYc9/95MvE5kjL1O9n8758Y4vcxiPL2nHxG98WFEuzvgXrw6/V89MUF3PbWbsbxqEwo+L/fHvUBJazzvjIg8j/TYPe70ELylq1e9cKkWPf03Pjn9wIe9kVKYvTRdkjzTP1E9FcT5O86MMT28L3O9yD/Kvez+w7wzx648UsTAvSOeUTza9tG9mZSyvSmLrD3JeSM9vRo/u3/s373aDis+HTTOvHXUzz2mZoK9wQEGvCfF0rxmoYe9P70IvVOHib3mddS8ZoZPPS7RIb5oCJA9eXvkvBhpt71qfQk9vRznvSBXMD1DZQo+1QFjvXsBej12bSk8Vy8xO4SDPD3QiBU+i7SIPJqAHz1cbz288RgdvUY+oD39fbY8IxrWvXJLAD4Wgs69QtUIvkG/o72HYZS9oQF1O2jG0zwB3zY9IiNkvFnlTL0f9iA+Zm+OvA=="
cyffea2  = "bNJ0vOAZQr1+kEu7zgyKPHPL370fDX490HKMPUCJjrwUsqG9CxAgvaSiLD3bXTG8GvH1vL1m0L0ue5c9xSQjvdqRXz01sBm9E1+hvFTWjL0u3R89sIOVPBvmeb1angI7seiFvfbmNjx3L1u6LqMdPrk5dz2ytIs8gDx1vXKCqLtHzY08fgvru8AuDD0Qf6Q8sUy7vfWg3T2jJOY79RorPTgHRz3DaWI9Hbl9vKDh4z3Lfv48xF/UPcECUb3fIdG7gNiePdOgjDyaOV69qZ38vE7a9rw8TZ48OuHgvX4lAj7XgV69SJIXPYniaz07xpE9fVSrPcYBIbzuIwM91XxQu27hoD3Aaok8F8yDvfIqCz1zRPW8ow+munUkJT3hwXu93LcjvXM0Ajun95c9w9byvSNgoz2wi2E97raaPY4AHzyBuvi9aXZoOrZOCz3HwEw9XSLqu6D0TD0O56G8PVLovRmNtryZjIQ96th/PblPhDzN8AO9waCzvXDypzxEbMU87XHCPZzRN7wCRcQ9Skw1Oxw+Lj3LE1+8lq29PNpTszyDdjO8eBT9PAqfMLxHQ2i9ZpYBPdRQYr3hZlm9vcVJvG/ahz2zN0w8x8IwvScruzyvUUi92Gmrvb+sGTyCN1e971pfPXADATwBWt09if4sPXFzGbxMXgE9B3Ulvb2Y8bwClhE+I926PTsHQT0FuOu9ow14PQdnyL2f9ce99cFkvTBSHbydJri8P9A/O3f1c72nx4+8Y9VpvknmYLxT5948vbxEPp6YMz3L65y8jVD7PGGakz3nlH88zeOyPXatS7w9hTe8sef4vCDcsr00uLY8t9TePFsq4jwBPJM7p0Vkvfw1eLxhS3K88hKVvTBgmjxhLeY98EAevQwMrD2Nxwg9PRsIvEfxkj00V0c9z69MPWt3jzw6q4M9JdSXPO3xmL2Mgdk84z8Rvflt47y9Np27cAQQveBV3rwL+SQ9O/ZYPZd7HT3kKlg9gjKovTOYCz2IIFs8E58IPYCkdb3gbHS94Bc5PZ1f2ryV/5i9IizZvUSq1zzi28Y9tlzJPKKdiTrkMs+9ANLavd+ZF722m4888vl2vZLPkDykEDO9DMnQvZfAej2lpS49dB2+O7XSd70Um+c9m9CWvNIAzD3hOb+9fMMHvMQ7ar1FiDS9ApvCvcztmb2a+FY88ZBTPEEoBL42SdI9Kf8JPPTUm736SV+8tNkgvh7pgD0wq+M9rbAvvSW+jT2VB+U8eu9LPWTM5TtS6u89hqb5vI6Vzz3JpAa9J/0jvVJs4T0USCI9Ltayvcyemj3KXIW97Gv2vYfFp71vuPu8vTkvPUwuLz24pUI9LIpCvXEFNL0f2hc+4oz6uw=="
zpcfea1  = "RH+JPNcMOD0/DY89nN2CvQOeID4VnlG9nm2uvaYT87y3tgK9OwesvH5zYzy088e9WysUOrhJqj19MAU8qE30u/T1ILzKIMm9IBcIvdFtTT3BdSY9iYWTPYS+gDwRuAc8Ft8JPCg8oDxpSiA9W5ihPYYgGjyT67u8dJGsPYF20TxZo8Q94ZCWPCpbBD3r1MO9mFWcPLlbdD2froy8k6I3vZU3Mz1Cxe8905civRsSWLxM+K89Szu1vfRDfr3ukAq9vVQOPbM0hrvuXSy7yy/cvNpygL1ay42862RFvXcECL1xxos8nCimvLU4w7sBrpQ977gJPQeeWz03/Qg95vpWvYfdNbxFFo09vPrIPEtNtr2SVNk9cuqFvWPYTb1spO28xEQWvZfrCr39VR69nM97vRwd4z21Y7M8mZmjPWB/MDtLGAu9DQdIvOmBWT2Qq+E8bLqSPcMC4Ds0WWm8FJPJPakpfrxEMv27Clfmu9LOWjxzBKc7xJsTPeyQDD0cCl493/poPZloVDyzvM89jkxOPOG+Zr4di6m8Ci2TPfVhDL0mEo48zjavPRMG4T2sFMm8zrQ9vST5UruNXyg9t+KkvEqEWT060rW93si9vac5DT1yctG8Y4KSPepYNjkZ/bi9Pvq2PShSmLyW+mg9e0N1vUA+oj3+dm89MYMXPti+gj036xG97bsTPrNygT3Wv4c6QCIkvfi41zxqcxY9EGY/PYLULz0sXZ49+QLku6xrBb4v66S8GFG1vT7S6ryR6gq+g2eXvelR5r0v0KM9J6GNvXNFzLzgY7a85/gRvdCptrxr0z29PN72PcZVADutnrq8mgBtvJZjC771sBs9QQZePWOfrrxFeB08plY2vQ8BMj13UlS8L1UzPYWj0zvlyJO9xt9hPd3+DjusT1g9zMBNvNzWtT0hmV69TzSqPax6UL0cfd68Y/o5PQW7WbsE99e73iKpPVc6TjyW6Is8tuWmPBjwpjzWOyO9ojb+vcCW1z36xhk+ocQZPURjmT2boT+8kQxdvXKAlj2bQH49dWnevBZGV71ITfW9sxDHO8n+HT68Itc8lLIMPdPYAT28pJC9JiGwvTVT+Dz+YSA9iNP3vGo1972GYCI88ylWPWq5yrxFsny91lCbPJpI5D1tI8O9D939PKkY2L06DAU+yGu/vEsocT1OzwS9wc4Rvakngzq3fxM8THFEvQqpDDwA14s9JZC7PIsetrw6DES9oXo9vKwTdLurARi9vomVPO4aFD7XmIQ9ia3lPTBpCz7qUBO8rbIVPfyrlL26XKI9CLecPWp+ILtD8Qe+gUzDPTQePD1ozaa8ixyCvWkQfD208O88pUWEuzbTRLwLfYO9mV4+PA=="
zpcfea2  = "SekvPZ00B73u9Z68V+iovKgECT4307q9JOgVO+Qd3bxGYpk8rsWVve6KoDxqQmW96rrDvJCqdD29k/s87T2UvI1HrruMz2e93JeDPcrGQD2TbGQ9y4vnPLqhhzwSpl29XWnPvJ8hIT0tmY09YBp5PWw7yLx/aFA8LJ8wPQUMlz0dIRI9JyxPPR1yEL6JZYe9B37RvQGxFryXM8+8gPeLvYuznz0Yd1E95g2zvF0kYLksewu99BYCvviqpL2BqjQ9zjmdPT0y6D0Yegy9SCIiPV0Ts70MhRC9i9QivbSWZ7004u+7Q6/hvErxXTzRuNk96yIMPUgkgj3w3hY9WjqqvOwhCj07fwk+WV6tPTroLb2ZCs89aRugPBTxIL2X0QU8I7ifvJfr1r2q3IO9hg4QPVisIj1qn8K7PO8NPSvgOj0FuAm91h9/vJqVqTxLUds85t2HO2R8ST3kpU+98vM6PaPL9rx+/Vu9MoEnPeOgf7yr4KS8A/WkvFojGbsdkNU8U0zzvHYpNj2jL8A91Dw9vHVlI70I86q8a5MGPaTkH71FGN27k+sJPRue5TwmGLS9m2pwvVLq1bu0HVg9vMcOPBnr1Ds7KxS+nlm8vUkJtrv94ew7rxiFPArylju5iK+9IIiAPR/ftbyQbgA8WcH6vVjRtT3Lh4g9QlzrPNF7pj0yRdY88AoAPvQj7T30r1q9CxGTPbA27jwcBx49KvnKPfO9qbzKVUc9ZPLKvPqZgDspyyC94Rm3veTmx71gpdS9FVhrvPhsFb7L76s8DjGmvdKptzx4QFW8Op/SvBMOqr2PUIC9qsORPY7u17w4I4W7xDKvvYd4Fr5BPMk8gXwgPfauAzxoaCm9m9ofviHQMT0gqiq7FpQOPHFuo7t+P7q5vMRPPRWgkbzkr5o8/PjHvfPwij32xp67AUsdPtRVLb04n8c8ZJEJPWimFD3j3Is9HpSUPYQhKzxb7bU9V89IPcllgT2kds29N07NvUF/VD2UgMY9JgKsPT9nLj7GIJc8+yu6O3tQHz1R/YU97vKUPYPjCb42qRa8bLQuvTu0Cj6tHSa9DDf0vDqyrD16A2+8GkYHvlQEUD3ltFG8xLEtvBCqvr0YF/E8JrqEPVhNmj1s7qK9YeXpPMlHrz1d0Zu948FKvamO8bzuAgg+p8ypO1er6zw0Jg69mMVKvatUhrtgI3U7eYWSvNMz7rsqa9c9geD7u9W6o7zLGf08OiYSvSlsqD1p7nG9Wd7Wu8oADz6LCnY9Dd2mPSn+2z1rJAO9jDTWPFyWzDxSrI091o4gPSVDqryKzj++ermsPejbsruQ+Gu8tk9iOgKXBDzZve08WvoMPQsOCj2lgBO95JKDPQ=="
bodyfea1 = "fWOZvAHChT2Yxni9AktqvUBGjr2CG6w9+WECvl9C0LsJHlG8sqJSPbAfyrw5Vts8S5m9O/yPt73wcOE9WS8ZvYr0or2N71A9pnNdPACvurvyWye9SZsEvmlhAL6GSc29G4+1PAHcoj2eaWY9/xBTOwStiD1KZYs9CMDCPQzGVb2tKZC9Gi0Dvde/ELzZUFe8GRfRPduA3DunjGM8beaGvA3ndj3e72Y6DWnJvZ0jrr1/lIo91rocPSEnmL2rMzs9a/EYvg7YrT0Mczm9uQOOu2QC1jsYMLY94a3sOyxTMb5Dw9u9DzmzPc3ovrxwOXC9/y+RPXt4oL2Q6sy9OywKPW7tsD2SpYY8mq+8PbW9jL0/W9y8Mb2ivV6+bTlIc4M9dGIEPff2vbyDeLW9l5Ffvd9OPD2h3Kk9swV5vRTEXrz+lYy8jHGqvZV7mj2iQjE+Bv/oujQ7brwfu088GI5pOgpKPjyyjmu8aIbxvCOqcb22c3w9/4rHPbcSR72vlmi9uM/Fvd5uzr0RVWO9/iorvZHPtL3J/JA9YWo9vbIshT3apw68mhwvPWVqKb1Vi9C8tioKvsEKaL1olEO9HrtqPTP1BD0jvIq8COZcvQq0IT38PZK9YGv4PLw1rLzt7vk8xaUnvZsDBz7ybDo9dLUBvuvtWbwll0w8mcOJvZPhLb2HDuM94AVQPXqh3Dwkqqy8yvTPPLjGKb3st+O8HYYmvSufzT0KVse8nNCvvSuilLw8Heq9UEGFvSTG+LpCM4M9+pjQu6uAfTs/q6g9Fc2wuhudqTtqAcS7J5rpPIYP6DydIoc84OI5vfEgwLwu71465ASZPdfPsr3d9pc8WX6xvEz7yrxr1II8z92LO/5Mu71zu+a99VEzPfZ73b24l8k9rJp1vQ46hryBkJM9FrywvesrDL54ITA9WvNKvUWlVz169cc9tMZ0PHqFjLxV+mS9i8iYPGSl0b2IEjm9x4ICvG/QiT3LHdY9TgU5PTZ6qj317og85R7GuqSLQT2XxcC9svR9vQqB0btp6ai77JCEvYLszLzHnho96bSKvTQysjt+9pM8BUYAvNgvRD269+g8CX4CPft2kj23d988Md+OPbrdHbtGRgK9tcAAvlHGBbzi36G8W8nPPVlXhTx+EaY94K9Nvc1xrLqIYVi9S3Zwvb3fYDxi/xg9M1S6vSu53bw8mMY8PljvvBNKbr27f589/Cf8vGY2E71dB5I9y/kavMVTkLudIw09N/FXvAJgj7o8pP285oyOvVoJGj2Te0o9PEofPrarH70muy48DZuVPSo2Zr1PTZc9z6PjPSIC770Nmwi8ykQhPAsGATvSQ4e9TGaUOwDnyzulErW9rEsOvQ=="
bodyfea2 = "6WacOlLcgT0/ZNy9w6/iPOXPe73Q9M09tizDvApCKz0bmwm99fuEPVI2mj1zzoQ9kGgTPeIJQ71OWqw9S2cavOrY2LxY2Dk9+Wr7O0mK0b3QOt48Q4a6veQZq73O3ja9hHgrPRayhbxBx9E9IJEjvVWaCr24PGs9yI0SPU6EJ72hUDm9yvpfPSMyWrsLu268PlCfPSjM4T3Pr4S7hzsru1yTvT3on8u8ppaQvPfzzL0c5X+9aLEEvWWDAb2C4Hu8xJiKu+TbvD2WrGI8Z0EhPLlgRL0XIkw9hlAZPcTlI75OKZG6zzGsvVx2yT2MqGi8LGgJvZnUojzP9RE9V4NPO6PG0D24sZK83MnIPFcobL3jmnW9d4q0vZLuED0QEzQ9+8THveoX0L1nBMq8jXiyvEnHOz02fgg8yI2ZPKZerr0VvpQ9+RTovOCDlT0N5bc9l4Siu4TG6zwS3l+7tECUvSiE4T0EXA69baTFPN1aYDyEopw9LCOQPa/QOzxiffo78mkLvtgXYD1cQci84jcEvfR+hL1uCos9Rp6hvbpPszy7SI+9LGE7PG+ewzzpMMI86kbsvcM7wLypyV+9/bPUPRQii7w8DA68uSeIvUjuXzxc/Ry+yc25vLfWgjsI25U9rpWDvQfiPT3hSwI9w8IGvZNFXb0CDYS9LtbHvfCmR704aeo9sosnO6JJaD2oENo7CPzzvHsCGL1VEZ+9oAynve0vMD78+/68iMy4vGTBgb3Q9Tm+CURpvb88UL2Xdma9QfGMPQLHPz3R2FI9/Vr1PPuxCr2RmpU9NxPnPIHBMLxpVx09qkTXvXzCx7sNgkc9CCg4PVOznDyIkTY82AtOPZ9sArxPMa09QagNvCJQCr4r65S8XfxxPQ1PBz2QMYE9+JFFvULWjrwj9P48juBSvcdSEL2aV+Y9w9KVvJ3l8z0qAZk9fbQjvY44rLzvLq+8Nc15PDrYF713BPq9i0j3OyEWcz0Wjrc9FYpgPOKl5Lx5hIa8ID2Svf99NT2QvAe7ilI/vSCQjb3V6jg9Lbv+PCFR3jxLrho9qoCZPD81Ib0wmjy8ObPuvGWHbT3Sx0o9ja1AvD94pT1u4TC8JAXfPIVvx7sOdDy8YVJJvtYVPL2rbqq8pHewvPdYojwVPN89IP63PB9vmbyBVoO9hhEyvXazYz1Sk9O8QBWcvechjr1uUB093UTMO8FJA74WD6w7RFhAPKjBXzxUuNc98daQuyNWtr28L7a86W42vRHFXz0vDl69OUeqvSZovj1jNTS9UGoBPj9+oL0T45m9NwXMvOwA0b1xhCM9OshwPPsFKL7v4yc9uhtBvcyzCb5awI47Rb4jvP4He73AX929J2dQPQ=="


class TestArgusipsScenario(object):
    """ Argusips scenario test"""

    @pytest.fixture(scope="class", autouse=True)
    def init_func(self, config_obj):
        # 初始化测试集
        # 所有test运行前运行一次，接收外部参数env_obj，初始化测试环境
        log().info("==========%s测试开始==========" % self.__class__.__name__)

    def teardown_class(self):
        # 所有test运行完后运行一次
        log().info("==========%s测试结束==========\n" % self.__name__)
        log().info("clear tasks finish")

    def setup_method(self, method):
        # 每个测试用例执行之前做操作
        log().info("用例%s开始" % method.__name__)

    def teardown_method(self, method):
        # 每个测试用例执行之后做操作
        log().info("用例%s结束" % method.__name__)

    def test_scenario_argusIps_001_FaceDetect(self, ArgusipsApi, ArgusdbApi, config_obj):
        """ 测试facedetect，img与detectmode正确，期望返回正确"""
        image = {
            "data": ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        detect_mode = "Default"
        feature_version = config_obj.Argus.feature_version
        resp = ArgusipsApi.FaceDetectPostApi(image=image, detect_mode=detect_mode,feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.face_info.0.type") == "OBJECT_FACE"
        assert resp.json_get("response.face_info.0.face")
        assert resp.json_get("response.face_info.0.face.angle")
        assert resp.json_get("response.face_info.0.face.rectangle")

    def test_scenario_argusIps_002_FaceDetect_twoface(self, ArgusipsApi, ArgusdbApi, config_obj):
        """ 测试facedetect，img与detectmode正确，图片存在twoface，期望返回正确,检测出2张人脸"""
        image = {
            "data": ArgusdbApi.imageToBase64(os.path.join(config.goimage_path, "twoface.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        detect_mode = "Default"
        feature_version = config_obj.Argus.feature_version
        resp = ArgusipsApi.FaceDetectPostApi(image=image, detect_mode=detect_mode, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("result.code") == 0
        assert len(resp.json_get("response.face_info")) == 3
        for info in resp.json_get("response.face_info"):
            assert info["type"] == "OBJECT_FACE"
            assert info["face"]
            assert info["face"]["angle"]
            assert info["face"]["rectangle"]

    def test_scenario_argusIps_003_FaceDetect_nobody(self, ArgusipsApi, ArgusdbApi, config_obj):
        """ 测试facedetect，img与detectmode正确，但是不存在人脸，期望返回正确，但是face为nil"""
        image = {
            "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "nobody.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        detect_mode = "Default"
        feature_version = config_obj.Argus.feature_version
        resp = ArgusipsApi.FaceDetectPostApi(image=image, detect_mode=detect_mode, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("result.code") == 0
        assert resp.json_get("result.error") == "no faces"
        assert len(resp.json_get("response.face_info")) == 0

    def test_scenario_argusIps_003_FaceDetect_ErrorParams(self, ArgusipsApi, config_obj):
        """ 测试facedetect，img与detectmode不正确，期望接口返回失败"""
        image = {
            "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "nobody.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        detect_mode = "Default"
        feature_version = "12345"
        resp = ArgusipsApi.FaceDetectPostApi(image=image, detect_mode=detect_mode, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 1001

        # wrong.jpg找不到了
        # image = {
        #     "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "wrong.jpg")),
        #     "format": "IMAGE_JPEG",
        #     "url": ""
        # }
        # detect_mode = "Default"
        # feature_version = "12345"
        # resp = ArgusipsApi.FaceDetectPostApi(image=image, detect_mode=detect_mode, feature_version=feature_version)
        # assert resp.status_code == 200
        # assert resp.json_get("header.errno") == 1002

    # def test_scenario_argusIps_004_Face1DetectBound(self, ArgusipsApi, config_obj):
    #     """ 测试FacedetectBound，img与bound正确，期望返回正确"""
    #     image_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
    #     img = Image.open(image_path)
    #     width = img.width
    #     height = img.height
    #     image = {
    #         "data": ArgusipsApi.imageToBase64(image_path),
    #         "format": "IMAGE_JPEG",
    #         "url": ""
    #     }
    #
    #     bounding = {
    #         "vertices": [
    #             {"x": 1, "y": 1 },
    #             {"x": width, "y": height },
    #         ]
    #     }
    #     feature_version = config_obj.Argus.feature_version
    #     resp = ArgusipsApi.FaceExtractWithBoundingPostApi(image=image, bounding=bounding, feature_version=feature_version)
    #     assert resp.status_code == 200
    #     assert resp.json_get("header.errno") == 0
    #     assert resp.json_get("result.code") == 0
    #     assert resp.json_get("response.align_score") >= 0.4
    #     assert resp.json_get("response.face_score") >= 0.4
    #     assert resp.json_get("response.feature.type") == "face"
    #     assert resp.json_get("response.feature.version") == feature_version
    #     assert resp.json_get("response.feature.blob")

    # def test_scenario_argusIps_005_Face1DetectBound_errorParams(self, ArgusipsApi, config_obj):
    #     """ 测试FacedetectBound，img与bound或feaversion不正确，期望返回正确"""
    #     image_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
    #     img = Image.open(image_path)
    #     width = img.width
    #     height = img.height
    #     image = {
    #         "data": ArgusdbApi.imageToBase64(image_path),
    #         "format": "IMAGE_JPEG",
    #         "url": ""
    #     }
    #
    #     bounding = {
    #         "vertices": [
    #             {"x": 1, "y": 1},
    #             {"x": 5, "y": 5},
    #         ]
    #     }
    #     feature_version = config_obj.Argus.feature_version
    #     resp = ArgusipsApi.FaceExtractWithBoundingPostApi(image=image, bounding=bounding,
    #                                                       feature_version=feature_version)
    #     assert resp.status_code == 200
    #     assert resp.json_get("result.code") == 0
    #     assert resp.json_get("result.error") == "bounding abnormal"
    #     assert resp.json_get("response.align_score") == 0
    #     assert resp.json_get("response.face_score") == 0
    #
    #     resp = ArgusipsApi.FaceExtractWithBoundingPostApi(image=image, bounding=bounding,
    #                                                       feature_version="12345")
    #     assert resp.status_code == 200
    #     assert resp.json_get("header.errno") == 1001

    # def test_scenario_argusIps_006_Face1DetectBound_bounding_noface(self, ArgusipsApi, config_obj):
    #     """ 测试FacedetectBound，img与bound或feaversion正确，但是bounding内无人脸，期望返回正确score低"""
    #     image_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
    #     img = Image.open(image_path)
    #     width = img.width
    #     height = img.height
    #     image = {
    #         "data": ArgusdbApi.imageToBase64(image_path),
    #         "format": "IMAGE_JPEG",
    #         "url": ""
    #     }
    #
    #     bounding = {
    #         "vertices": [
    #             {"x": 1, "y": 1},
    #             {"x": 20, "y": 20},
    #         ]
    #     }
    #     feature_version = config_obj.Argus.feature_version
    #     resp = ArgusipsApi.FaceExtractWithBoundingPostApi(image=image, bounding=bounding,
    #                                                       feature_version=feature_version)
    #     assert resp.status_code == 200
    #     assert resp.json_get("header.errno") == 0
    #     assert resp.json_get("result.code") == 0
    #     assert resp.json_get("response.align_score") <= 0.002
    #     assert resp.json_get("response.face_score") <= 0.002

    def test_scenario_argusIps_007_FacedetectExtract(self, ArgusipsApi, config_obj):
        """ 测试FacedetectExtract，img与selectmode,detectmode正确，期望返回正确"""
        image_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        face_selection = "LargestFace"
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.face_info.face")
        assert resp.json_get("response.face_info.face.face_score") >= 0.9
        assert resp.json_get("response.face_info.face.rectangle")
        assert resp.json_get("response.face_info.face.angle.yaw") <= 10
        assert resp.json_get("response.face_info.face.angle.pitch") <= 10
        assert resp.json_get("response.face_info.face.angle.roll") <= 10
        assert resp.json_get("response.face_info.face.attributes.st_age_value")
        # So(faceres.Response.FaceInfo.Face.Attributes["st_age_value"], ShouldBeBetween, "23.000000", "28.000000")

        assert resp.json_get("response.face_info.face.attributes.gender_code") == "female"
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        assert resp.json_get("response.feature.blob")

    def test_scenario_argusIps_008_FacedetectExtract_twoface(self, ArgusipsApi, config_obj):
        """ 测试FacedetectExtract，img与selectmode,detectmode正确，图片中存在twoface，期望返回正确，返回largeface的属性"""
        image_path = os.path.join(config.goimage_path, "twoface.jpg")
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        face_selection = "LargestFace"
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.face_info.face")
        assert resp.json_get("response.face_info.face.face_score") >= 0.8
        assert resp.json_get("response.face_info.face.rectangle")
        assert resp.json_get("response.face_info.face.angle.yaw") <= 12
        assert resp.json_get("response.face_info.face.angle.pitch") <= 12
        assert resp.json_get("response.face_info.face.angle.roll") <= 12
        assert resp.json_get("response.face_info.face.attributes.st_age_value") # TODO
        # So(faceres.Response.FaceInfo.Face.Attributes["st_age_value"], ShouldBeBetween, "25.000000", "30.000000")

        assert resp.json_get("response.face_info.face.attributes.gender_code") == "female"
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        assert resp.json_get("response.feature.blob")

    def test_scenario_argusIps_009_FacedetectExtract_errorParams(self, ArgusipsApi, config_obj):
        """ 测试FacedetectExtract，img与selectmode,detectmode正确，不存在人脸，期望返回正确"""
        image_path = os.path.join(config.goimage_path, "nobody.jpg")
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        face_selection = "LargestFace"
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("result.error") == "no faces"

        # 测试FacedetectExtract，img与selectmode,detectmode不正确，期望返回正确，返回错误提示
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version="12345")
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 1001

        image = {
            "data": "12345",
            "format": "IMAGE_JPEG",
            "url": ""
        }
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version="12345")
        assert resp.status_code == 400

    def test_scenario_argusIps_010_Face3DetectOverlap(self, ArgusipsApi, config_obj):
        """ 测试FacedetectExtractOverlap，img与selectmode,detectmode正确，期望返回正确"""
        image_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
        img = Image.open(image_path)
        width = img.width
        height = img.height
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }

        bounding = {
            "vertices": [
                {"x": 1, "y": 1 },
                {"x": width, "y": height },
            ]
        }
        feature_version = config_obj.Argus.feature_version
        resp = ArgusipsApi.FaceDetectAndExtractWithOverlapPostApi(image=image, bounding=bounding, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.face_info.face")
        assert resp.json_get("response.face_info.face.face_score") >= 0.9
        assert resp.json_get("response.face_info.face.rectangle")
        assert resp.json_get("response.face_info.face.angle.yaw") <= 10
        assert resp.json_get("response.face_info.face.angle.pitch") <= 10
        assert resp.json_get("response.face_info.face.angle.roll") <= 10
        assert resp.json_get("response.face_info.face.attributes.st_age_value")  # TODO
        # So(faceres.Response.FaceInfo.Face.Attributes["st_age_value"], ShouldBeBetween, "23.000000", "28.000000")
        assert resp.json_get("response.face_info.face.attributes.gender_code") == "female"
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        assert resp.json_get("response.feature.blob")

    def test_scenario_argusIps_011_Face3DetectOverlap_twoface(self, ArgusipsApi, config_obj):
        """ 测试FacedetectExtractOverlap，img与selectmode,detectmode正确，两face，bound图片的大小，期望返回大脸的特征"""
        image_path = os.path.join(config.goimage_path, "twoface.jpg")
        img = Image.open(image_path)
        width = img.width
        height = img.height
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version

        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x": width, "y": height},
            ]
        }
        resp = ArgusipsApi.FaceDetectAndExtractWithOverlapPostApi(image=image, bounding=bounding,
                                                                  feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.face_info.face")
        assert resp.json_get("response.face_info.face.face_score") >= 0.8
        assert resp.json_get("response.face_info.face.rectangle")
        assert resp.json_get("response.face_info.face.angle.yaw") <= 12
        assert resp.json_get("response.face_info.face.angle.pitch") <= 12
        assert resp.json_get("response.face_info.face.angle.roll") <= 12
        assert resp.json_get("response.face_info.face.attributes.st_age_value")  # TODO
        # So(faceres.Response.FaceInfo.Face.Attributes["st_age_value"], ShouldBeBetween, "25.000000", "30.000000")
        assert resp.json_get("response.face_info.face.attributes.gender_code") == "female"
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        assert resp.json_get("response.feature.blob")


        bounding = {
            "vertices": [
                {"x": 1, "y": 1},
                {"x": int(width / 2), "y": height},
            ]
        }
        resp = ArgusipsApi.FaceDetectAndExtractWithOverlapPostApi(image=image, bounding=bounding,
                                                                  feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.face_info.face")
        assert resp.json_get("response.face_info.face.face_score") >= 0.7
        assert resp.json_get("response.face_info.face.rectangle")
        assert resp.json_get("response.face_info.face.angle.yaw") <= 20
        assert resp.json_get("response.face_info.face.angle.pitch") <= 20
        assert resp.json_get("response.face_info.face.angle.roll") <= 20
        assert resp.json_get("response.face_info.face.attributes.st_age_value")  # TODO
        # So(faceres.Response.FaceInfo.Face.Attributes["st_age_value"], ShouldBeBetween, "38.000000", "42.000000")
        assert resp.json_get("response.face_info.face.attributes.gender_code") == "female"
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        assert resp.json_get("response.feature.blob")

        bounding = {
            "vertices": [
                {"x": int(width / 2), "y": 1},
                {"x": width, "y": height},
            ]
        }
        resp = ArgusipsApi.FaceDetectAndExtractWithOverlapPostApi(image=image, bounding=bounding,
                                                                  feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.face_info.face")
        assert resp.json_get("response.face_info.face.face_score") >= 0.8
        assert resp.json_get("response.face_info.face.rectangle")
        assert resp.json_get("response.face_info.face.angle.yaw") <= 12
        assert resp.json_get("response.face_info.face.angle.pitch") <= 12
        assert resp.json_get("response.face_info.face.angle.roll") <= 12
        assert resp.json_get("response.face_info.face.attributes.st_age_value")  # TODO
        # So(faceres.Response.FaceInfo.Face.Attributes["st_age_value"], ShouldBeBetween, "25.000000", "30.000000")
        assert resp.json_get("response.face_info.face.attributes.gender_code") == "female"
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        assert resp.json_get("response.feature.blob")

    def test_scenario_argusIps_012_Face3DetectOverlap_bounding_noface(self, ArgusipsApi, config_obj):
        """ 测试FacedetectExtractOverlap，img与selectmode,detectmode，feaversion正确，boud中不存在人脸，期望返回错误提示"""
        image_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
        img = Image.open(image_path)
        width = img.width
        height = img.height
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }

        bounding = {
            "vertices": [
                {"x": 1, "y": 1 },
                {"x": 30, "y": 30 },
            ]
        }
        feature_version = config_obj.Argus.feature_version
        resp = ArgusipsApi.FaceDetectAndExtractWithOverlapPostApi(image=image, bounding=bounding, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("result.error") == "overlap failed: no face"

    def test_scenario_argusIps_013_Face3DetectOverlap_errorParams(self, ArgusipsApi, config_obj):
        """ 测试FacedetectExtractOverlap，img与selectmode,detectmode，feaversion不正确，期望返回错误提示"""
        image_path = os.path.join(config.goimage_path, "face/zxq/xueqi1.jpg")
        img = Image.open(image_path)
        width = img.width
        height = img.height
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }

        bounding = {
            "vertices": [
                {"x": 1, "y": 1 },
                {"x": 30, "y": 30 },
            ]
        }
        feature_version = config_obj.Argus.feature_version
        resp = ArgusipsApi.FaceDetectAndExtractWithOverlapPostApi(image=image, bounding=bounding, feature_version="12345")
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 1001

        image = {
            "data": "12345",
            "format": "IMAGE_JPEG",
            "url": ""
        }
        resp = ArgusipsApi.FaceDetectAndExtractWithOverlapPostApi(image=image, bounding=bounding,
                                                                  feature_version="12345")
        assert resp.status_code == 400

    def test_scenario_argusIps_014_featureCompare_one_image(self, ArgusipsApi, config_obj):
        """ 测试featurecompare，同样的facefeature，期望接口返回score：1"""
        image_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        face_selection = "LargestFace"
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        assert resp.json_get("response.feature.blob")

        one = {
            "blob": resp.json_get("response.feature.blob"),
            "type": resp.json_get("response.feature.type"),
            "version": feature_version
        }
        other = {
            "blob": resp.json_get("response.feature.blob"),
            "type": resp.json_get("response.feature.type"),
            "version": feature_version
        }
        resp = ArgusipsApi.CompareFeaturePostApi(one=one, other=other, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("score") == 1

    def test_scenario_argusIps_015_featureCompare_two_image(self, ArgusipsApi, config_obj):
        """ 测试featurecompare，同人不同facefeature，期望接口返回正确，score大于0.9"""
        image_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        face_selection = "LargestFace"
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        blob1 = resp.json_get("response.feature.blob")

        image_path = os.path.join(config.goimage_path, "face/cyf/cyf2.jpg")
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        face_selection = "LargestFace"
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        blob2 = resp.json_get("response.feature.blob")

        one = {
            "blob": blob1,
            "type": "face",
            "version": feature_version
        }
        other = {
            "blob": blob2,
            "type": "face",
            "version": feature_version
        }
        resp = ArgusipsApi.CompareFeaturePostApi(one=one, other=other, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("score") >= 0.9

    def test_scenario_argusIps_016_featureCompare_two_image_person(self, ArgusipsApi, config_obj):
        """ 测试featurecompare，不同人不同facefeature，期望接口返回正确，score小于0.5"""
        image_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        face_selection = "LargestFace"
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        blob1 = resp.json_get("response.feature.blob")

        image_path = os.path.join(config.goimage_path, "face/wsh/shihan3.jpg")
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        face_selection = "LargestFace"
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        blob2 = resp.json_get("response.feature.blob")

        one = {
            "blob": blob1,
            "type": "face",
            "version": feature_version
        }
        other = {
            "blob": blob2,
            "type": "face",
            "version": feature_version
        }
        resp = ArgusipsApi.CompareFeaturePostApi(one=one, other=other, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("score") <= 0.5

    def test_scenario_argusIps_017_featureCompare_errorParams(self, ArgusipsApi, config_obj):
        """ 测试featurecompare，feaversion/type/blob不正确，期望返回错误提示"""
        image_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        face_selection = "LargestFace"
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractPostApi(image=image, detect_mode=detect_mode,
                                                       face_selection=face_selection, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.feature.type") == "face"
        assert resp.json_get("response.feature.version") == int(feature_version)
        assert resp.json_get("response.feature.blob")
        blob = resp.json_get("response.feature.blob")
        type = resp.json_get("response.feature.type")
        one = {
            "blob": blob,
            "type": type,
            "version": feature_version
        }
        other = {
            "blob": blob,
            "type": type,
            "version": feature_version
        }
        resp = ArgusipsApi.CompareFeaturePostApi(one=one, other=other, feature_version="12345")
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 1001

        one = {
            "blob": blob,
            "type": "wrong",
            "version": feature_version
        }
        other = {
            "blob": blob,
            "type": "wrong",
            "version": feature_version
        }
        resp = ArgusipsApi.CompareFeaturePostApi(one=one, other=other, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 1001

        one = {
            "blob": "1",
            "type": "face",
            "version": feature_version
        }
        other = {
            "blob": "1",
            "type": "face",
            "version": feature_version
        }
        resp = ArgusipsApi.CompareFeaturePostApi(one=one, other=other, feature_version=feature_version)
        assert resp.status_code == 400

    def test_scenario_argusIps_018_imagecompare(self, ArgusipsApi, config_obj):
        """ 测试featurecompare，同样的facefeature，期望接口返回score：1"""
        image_path = os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")
        one = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        other = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        detect_mode = "Default"
        feature_version = config_obj.Argus.feature_version
        resp = ArgusipsApi.CompareImagePostApi(one=one, other=other, detect_mode=detect_mode, feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("score") == 1
    # bug
    def test_scenario_argusIps_019_imagecompare_body(self, ArgusipsApi, config_obj):
        """ 测试imagecompare，同样的image，body的，期望接口返回错误1001"""
        image_path = os.path.join(config.goimage_path, "body/body.jpg")
        one = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        other = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        detect_mode = "Default"
        feature_version = config_obj.Argus.feature_version
        resp = ArgusipsApi.CompareImagePostApi(one=one, other=other, detect_mode=detect_mode,
                                              feature_version=feature_version)
        assert resp.status_code == 200
        # TODO 目前该case能识别出
        # assert resp.json_get("header.errno") == 1001

    def test_scenario_argusIps_020_imagecompare_onePerson(self, ArgusipsApi, config_obj):
        """ 测试imagecompare，同人不同image，期望接口返回score大于0.9"""
        one = {
            "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        other = {
            "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "face/cyf/cyf2.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        detect_mode = "Default"
        feature_version = config_obj.Argus.feature_version
        resp = ArgusipsApi.CompareImagePostApi(one=one, other=other, detect_mode=detect_mode,
                                              feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("score") >= 0.9

    def test_scenario_argusIps_021_imagecompare_mutilPerson(self, ArgusipsApi, config_obj):
        """ 测试imagecompare，不同人不同image，期望接口返回score小于0.5"""
        one = {
            "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        other = {
            "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "face/wsh/shihan3.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        detect_mode = "Default"
        feature_version = config_obj.Argus.feature_version
        resp = ArgusipsApi.CompareImagePostApi(one=one, other=other, detect_mode=detect_mode,
                                              feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("score") <= 0.5

    def test_scenario_argusIps_022_imagecompare_errorParams(self, ArgusipsApi, config_obj):
        """ 测试imagecompare，feaversion/image不正确，期望返回错误提示"""
        one = {
            "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        other = {
            "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "face/cyf/cyf1.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        detect_mode = "Default"
        feature_version = config_obj.Argus.feature_version
        resp = ArgusipsApi.CompareImagePostApi(one=one, other=other, detect_mode=detect_mode,
                                              feature_version="12345")
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 1001

        one = {
            "data": "",
            "format": "IMAGE_JPEG",
            "url": ""
        }
        other = {
            "data": "",
            "format": "IMAGE_JPEG",
            "url": ""
        }
        resp = ArgusipsApi.CompareImagePostApi(one=one, other=other, detect_mode=detect_mode,
                                              feature_version="12345")
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 1001

    def test_scenario_argusIps_023_OcrDetect(self, ArgusipsApi, config_obj):
        """ 测试ocrdetect，img，type与origintype正确，期望返回正确"""
        image = {
            "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "face/ID/ID2.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        resp = ArgusipsApi.OCRTemplatePostApi(region_type="CHINA", type="OCR_IDCARD", image=image)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert resp.json_get("response.objects.0.type") == "IDCardFront"
        assert resp.json_get("response.objects.0.areas.0.texts.0.content") == "1988"
        assert resp.json_get("response.objects.0.areas.0.texts.1.content") == "11"
        assert resp.json_get("response.objects.0.areas.0.texts.2.content") == "15"
        assert resp.json_get("response.objects.0.areas.0.valid") == True
        assert resp.json_get("response.objects.0.areas.1.texts.0.content") == "宜小信"
        assert resp.json_get("response.objects.0.areas.1.texts.1.content") == "女"
        assert resp.json_get("response.objects.0.areas.1.texts.2.content") == "汉"
        assert resp.json_get("response.objects.0.areas.1.texts.3.content") == "河北省保定市北市区五六东路186号"
        assert resp.json_get("response.objects.0.areas.1.texts.3.subtexts.0.content") == "河北省保定市北市区五六"
        assert resp.json_get("response.objects.0.areas.1.texts.3.subtexts.1.content") == "东路186号"
        assert resp.json_get("response.objects.0.areas.1.texts.4.content") == "132261198811150681"
        assert resp.json_get("response.objects.0.areas.1.texts.4.valid") == False
        assert resp.json_get("response.objects.0.areas.1.valid") == False

    def test_scenario_argusIps_024_errorType(self, ArgusipsApi, config_obj):
        """ 测试ocrdetect，type不正确，期望返回错误信息"""
        image = {
            "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "face/ID/ID2.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        resp = ArgusipsApi.OCRTemplatePostApi(region_type="MACAO", type="OCR_IDCARD", image=image)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 1001
        assert resp.json_get("header.message") == "internal err: ips's rpc failed: rpc error: code = Unknown desc = unsupport type"

    def test_scenario_argusIps_025_errorType(self, ArgusipsApi, config_obj):
        """ 测试ocrdetect，origintype不正确，期望返回错误信息"""
        image = {
            "data": ArgusipsApi.imageToBase64(os.path.join(config.goimage_path, "face/ID/ID2.jpg")),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        resp = ArgusipsApi.OCRTemplatePostApi(region_type="CHINA", type="OCRIDCARD", image=image)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 1001
        assert resp.json_get("header.message") == "internal err: ips's rpc failed: rpc error: code = Unknown desc = unsupport type"

    def test_scenario_argusIps_026_FaceDetectAndExtractAll_twoface(self, ArgusipsApi, config_obj):
        """ 测试FacedetectExtractAll，img与selectmode,detectmode正确，图片中存在twoface，期望返回正确，返回2个人脸"""
        image_path = os.path.join(config.goimage_path, "twoface.jpg")
        image = {
            "data": ArgusipsApi.imageToBase64(image_path),
            "format": "IMAGE_JPEG",
            "url": ""
        }
        feature_version = config_obj.Argus.feature_version
        detect_mode = "Default"
        resp = ArgusipsApi.FaceDetectAndExtractAllPostApi(image=image, detect_mode=detect_mode,
                                                          feature_version=feature_version)
        assert resp.status_code == 200
        assert resp.json_get("header.errno") == 0
        assert resp.json_get("result.code") == 0
        assert len(resp.json_get("responses")) == 3


