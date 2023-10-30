#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from commonlib import config, time_utils, sign_utils
from defines.belt.api.user_service_swagger import UserSwaggerApi


"""
使用说明：


"""


class UserSwaggerBusiness(UserSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(UserSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
        self.TOKEN_NAME = "X-Belt-Token"
        self.TOKEN_VALUE = "%s"  # token默认信息

    def init_interface(self, inte_obj):
        """初始化接口函数，需要统一初始化的参数写在这里
        inte_obj:是接口的对象，比如想要统一初始化host：inte_obj.set_host(env_config.host)
        """
        self.set_interface_prefix_path(inte_obj)
        inte_obj.set_host(self.host)
        if self.token:
            inte_obj.set_headers(self.TOKEN_NAME, self.TOKEN_VALUE % self.token)

        if inte_obj.path == '/console/v1/user_accounts':
            inte_obj.set_headers('X-Belt-Action', 'CreateUserWithAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/accounts/ocr':
            inte_obj.set_headers('X-Belt-Action', 'OCRIDCard')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/user/policygroups':
            inte_obj.set_headers('X-Belt-Action', 'GetAllPolicyGroupsByUserID')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/policygroups':
            inte_obj.set_headers('X-Belt-Action', 'ListPolicyGroup')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/policygroups/group_id':
            inte_obj.set_headers('X-Belt-Action', 'GetPolicyGroupAssociatedInfoByID')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/user_accounts/login_forgot_poassword':
            inte_obj.set_headers('X-Belt-Action', 'UserLoginForgotPassword')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/user_accounts/verify_user_register_info':
            inte_obj.set_headers('X-Belt-Action', 'VerifyUserRegisterInfo')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users':
            if inte_obj.method == "get":
                inte_obj.set_headers('X-Belt-Action', 'GetUserList')
                inte_obj.set_headers('X-Belt-Version', 'v1')
            elif inte_obj.method == "post":
                inte_obj.set_headers('X-Belt-Action', 'CreateUser')
                inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/access_mode/user_id':
            inte_obj.set_headers('X-Belt-Action', 'UpdateUserAccessMode')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/associated_info/user_id':
            inte_obj.set_headers('X-Belt-Action', 'GetUserAssociatedInfoByID')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/base_info':
            if inte_obj.method == "get":
                inte_obj.set_headers('X-Belt-Action', 'GetUserBaseInfo')
                inte_obj.set_headers('X-Belt-Version', 'v1')
            elif inte_obj.method == "post":
                inte_obj.set_headers('X-Belt-Action', 'UpdateUserBaseInfo')
                inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/code':
            inte_obj.set_headers('X-Belt-Action', 'SendSmsCode')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/code/verify':
            inte_obj.set_headers('X-Belt-Action', 'VerifySmsCode')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/current_user/code':
            inte_obj.set_headers('X-Belt-Action', 'SendCurrentUserSmsCode')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/current_user/code/verify':
            inte_obj.set_headers('X-Belt-Action', 'VerifyCurrentUserSmsCode')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/desc_info/user_id':
            inte_obj.set_headers('X-Belt-Action', 'UpdateUserDescInfo')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/security_set/cellphone':
            inte_obj.set_headers('X-Belt-Action', 'SecuritySetUpdateUserCellphone')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/security_set/email':
            inte_obj.set_headers('X-Belt-Action', 'SecuritySetUpdateUserEmail')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/security_set/password':
            inte_obj.set_headers('X-Belt-Action', 'SecuritySetUpdateUserPassword')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/sub_user/password':
            inte_obj.set_headers('X-Belt-Action', 'UpdateSubUserPassword')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/user_id':
            inte_obj.set_headers('X-Belt-Action', 'DeleteUser')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/user_id/accesskeys':
            inte_obj.set_headers('X-Belt-Action', 'CreateUserAKSK')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/user_id/accesskeys/access_key_id':
            inte_obj.set_headers('X-Belt-Action', 'DeleteAccessKey')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/user_id/batch_policygroups':
            inte_obj.set_headers('X-Belt-Action', 'BatchAddPolicyGroupToUser')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/user_id/policygroups/group_id':
            inte_obj.set_headers('X-Belt-Action', 'RemovePolicyGroupFromUser')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/user_name_exist':
            inte_obj.set_headers('X-Belt-Action', 'UserNameExistInAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == '/console/v1/users/user_id/accesskeys/excel_export':
            inte_obj.set_headers('X-Belt-Action', 'ExportUserAKSKExcel')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        else:
            inte_obj.set_headers('X-Belt-Action', inte_obj.path_action)
            inte_obj.set_headers('X-Belt-Version', inte_obj.path_version)


    def createPhoneUser(self, username, password, verify_code="1234"):
        """ 创建手机号用户"""
        mode = "1"
        password = sign_utils.getMd5(password)
        email = None
        phone = username
        code = verify_code
        email_code = None
        resp = self.ConsoleUserService_CreateUserWithAccountPostApi(mode=mode, password=password, email=email,
                                                                       phone=phone, code=code, email_code=email_code)
        return resp

    def deleteSubUser(self, user_id):
        resp = self.ConsoleUserService_DeleteUserPostApi(user_id=user_id, code=None, force=None)
        return resp


    def getSubUser(self, description):
        resp = self.ConsoleUserService_GetUserListGetApi(nick_name=None, description=description,
                                                            blocked=None,
                                                            order=None, page_request_offset=None,
                                                            page_request_limit=None,
                                                            page_request_total=None)
        return resp


