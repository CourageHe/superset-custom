
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import os
# 1、汉化
# 应用默认语言
BABEL_DEFAULT_LOCALE='zh'
# 启用语言选项
LANGUAGES = {
    'zh': {'flag': 'cn', 'name': 'Chinese'},
    'en': {'flag': 'us', 'name': 'English'},
}


# 2、数据库配置
DB_USER = os.getenv('DB_USER')
DB_USER_PW = os.getenv('DB_USER_PW')
DB_IP = os.getenv('DB_IP')
DB_NAME = os.getenv('DB_NAME')
# https://superset.apache.org/docs/databases/installing-database-drivers/
SQLALCHEMY_DATABASE_URI = "mysql://{v_db_user}:{v_db_user_pw}@{v_db_ip}:3306/{v_db_name}?charset=utf8".format(
    v_db_user=DB_USER, v_db_user_pw=DB_USER_PW, v_db_ip=DB_IP,v_db_name=DB_NAME,)


#3、登录权限二次开发 https://www.jianshu.com/p/063ccb8e2a75
try:
	# you'd better put all the import stuff here, since superset will ignore it
	from flask_appbuilder.security.manager import AUTH_REMOTE_USER
	from superset.security_models import MySecurityManager
except Exception as ex:
	raise Exception(ex)

# using customize MY security manager
CUSTOM_SECURITY_MANAGER = MySecurityManager
# AUTHENTICATION CONFIG
AUTH_TYPE = AUTH_REMOTE_USER
# setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = 'Gamma'
# Will allow user self registration
AUTH_USER_REGISTRATION = True




# 4、其他配置
SECRET_KEY = "EA67JrKiTTPCDs4EtUfcZ5ERHrU9QgKd1CCyh0PIIEYRe33v/bkRkFu6"

APP_NAME = "Superset看板"

CSV_EXPORT = {
    "encoding": "utf-8-sig"
}



