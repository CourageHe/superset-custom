#固定版本
FROM apache/superset
MAINTAINER CourageHes

# Switching to root to install the required packages
USER root

ADD superset_config.py /app/pythonpath

ADD security/remote_server_api.py /app/superset/remote_server_api.py
ADD security/security_models.py /app/superset/security_models.py
ADD security/security_views.py /app/superset/security_views.py

ADD security/login_my.html     /app/superset/templates/appbuilder/general/security/login_my.html

ADD assets/images/favicon.png /app/superset/static/assets/images/favicon.png
ADD assets/images/logo-horiz.png /app/superset/static/assets/images/superset-logo-horiz.png

# install mysql client
RUN pip install mysqlclient



USER superset
# 参考：https://zhuanlan.zhihu.com/p/585669109
ENTRYPOINT ["sh", "-c", "superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin && \
               superset db upgrade && \
               superset init && \
              sh -c /usr/bin/run-server.sh"]

CMD superset pybabel compile -d superset/translations