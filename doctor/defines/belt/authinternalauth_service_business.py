#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from commonlib.decorator import wait
from defines.belt.api.authinternalauth_service_swagger import AuthinternalauthSwaggerApi


"""
使用说明：


"""


class AuthinternalauthSwaggerBusiness(AuthinternalauthSwaggerApi):
    """ 业务类代码写在这里"""
    def __init__(self, host, token=None, config_obj=None, ext_info=None):
        super(AuthinternalauthSwaggerBusiness, self).__init__(host, token, config_obj, ext_info)
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
        if inte_obj.path == "/console-internal/v1/account/phone_or_email":
            inte_obj.set_headers('X-Belt-Action', 'AdminGetPhoneOrEmailByAccountID')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/accounts":
            inte_obj.set_headers('X-Belt-Action', 'AdminGetAccountList')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/accounts/account":
            inte_obj.set_headers('X-Belt-Action', 'AdminUpdateAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/accounts/auth_data":
            inte_obj.set_headers('X-Belt-Action', 'AdminGetEnterpriseAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/accounts/auth_data/unredacted_info":
            inte_obj.set_headers('X-Belt-Action', 'AdminGetEnterpriseAccountUnRedactedInfo')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/accounts/auth_status":
            inte_obj.set_headers('X-Belt-Action', 'AdminUpdateAccountStatus')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/accounts/business_assignment":
            inte_obj.set_headers('X-Belt-Action', 'AdminBusinessAssignment')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/accounts/industry_info":
            inte_obj.set_headers('X-Belt-Action', 'AdminGetIndustryInfo')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/cost_management/accounts":
            inte_obj.set_headers('X-Belt-Action', 'AdminGetCostManagementAccountList')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/inquiry_accounts":
            inte_obj.set_headers('X-Belt-Action', 'AdminGetInquiryAccountList')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/policygroups":
            inte_obj.set_headers('X-Belt-Action', 'AdminListPolicyGroup')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/user/policygroups":
            inte_obj.set_headers('X-Belt-Action', 'AdminGetAllPolicyGroupsByUserID')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/user_accounts":
            inte_obj.set_headers('X-Belt-Action', 'CreateInternalUserWithAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/users/base_info":
            inte_obj.set_headers('X-Belt-Action', 'AdminGetUserBaseInfo')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/users/cellphone_set":
            inte_obj.set_headers('X-Belt-Action', 'ConsoleInternalUpdateUserCellphone')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/users/code":
            inte_obj.set_headers('X-Belt-Action', 'AdminSendSmsCode')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/users/code/verify":
            inte_obj.set_headers('X-Belt-Action', 'AdminVerifySmsCode')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/users/current_user/code":
            inte_obj.set_headers('X-Belt-Action', 'SendCurrentAdminUserSmsCode')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/users/current_user/code/verify":
            inte_obj.set_headers('X-Belt-Action', 'VerifyCurrentAdminUserSmsCode')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/users/user_id/batch_policygroups":
            inte_obj.set_headers('X-Belt-Action','AdminBatchAddPolicyGroupToUser')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/accounts/user_info":
            inte_obj.set_headers('X-Belt-Action','AdminGetAccountUserList')
            inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/white_list_accounts":
            if inte_obj.method == "get":
                inte_obj.set_headers('X-Belt-Action', 'GetWhitelistAccounts')
                inte_obj.set_headers('X-Belt-Version', 'v1')
            if inte_obj.method == "post":
                inte_obj.set_headers('X-Belt-Action', 'CreateWhitelistAccount')
                inte_obj.set_headers('X-Belt-Version', 'v1')
        elif inte_obj.path == "/console-internal/v1/white_list_accounts/delete":
            inte_obj.set_headers('X-Belt-Action','DeleteWhitelistAccount')
            inte_obj.set_headers('X-Belt-Version', 'v1')
