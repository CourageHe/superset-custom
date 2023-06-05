"""
this file should be the api of your remote server
for example, your login service from your company
e.g. provide email and password, send this information to your remote server
waiting for the response from remote server. If remote server authorized this email and password
then it will be ok to login this user.
"""

import os
import json
import requests

import logging
logger = logging.getLogger(__name__)

def authenticate(username, password):
	"""

	:param username:
	:param password:
	:return:
	"""
	auth_remote_host = os.getenv('AUTH_REMOTE_HOST')
	manage_admin = os.getenv('MANAGE_ADMIN')
	manage_password = os.getenv('MANAGE_PASSWORD')

	auth_url = '%s/manage/loginForm' % auth_remote_host
	# param_dict_json = dict(phoneNum=username, password=password,loginType=4,mobileValidCode='',identify='IUKGEQ')
	param_dict = {'phoneNum':username, 'password':password,'loginType':4,'mobileValidCode':'','identify':'IUKGEQ'}

	headers = ""

	if username == manage_admin:
		if password == manage_password:
			userinfo = dict(username=username)
			return userinfo
		else:
			return None
	logger.info(param_dict)
	# form表单 post请求
	auth_result = requests.post(auth_url, data=param_dict, headers=headers)
	# # json数据 post请求
	# auth_result = requests.post(auth_url, json=param_dict_json, headers=headers, verify=False)

	if auth_result.status_code != 200  or json.loads(auth_result.text)['code'] != '000000':
		logger.warn("failed to auth user: %s, status: %s, response: %s " %
	                (username, auth_result.status_code, auth_result.text))
		return None
	userinfo = dict(username=username)
	return userinfo
