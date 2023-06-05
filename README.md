# Superset 定制化

>  [Superset](https://airbnb.io/projects/superset/) 是一款由 Airbnb 开源的“现代化的企业级 BI（商业智能） Web 应用程序”，其通过创建和分享 dashboard，为数据分析提供了轻量级的数据查询和可视化方案。

本项目支持Windows Docker环境部署，各文件夹下的`cmd`文件即为windows的可执行文件，可进行打包镜像、部署服务操作。

本项目是基于`superset`提供的`apache/superset`镜像的基础上二次开发，实现了**汉化**、数**据库切换为`MySQL`**、**第三方账号登录**等功能。通过本项目在`docker`环境中可快速配置，实现`superset`定制化使用。

+ 如需取消汉化：注释`superset_config.py`中第一部分配置；
+ 如需取消使用`MySQL`数据库：注释`superset_config.py`中第二部分配置；
+ 如需取消第三方登录：注释`superset_config.py`中第三部分配置；

### 配置

项目配置在`start-up.cmd`中，通过`docker run`命令设置环境变量，以供程序内部调用。

```bash
docker run -d -p 8080:8088  ^
    --restart=always ^
    --name superset ^
    -e DB_IP=127.0.0.1 ^
    -e DB_NAME=superset ^
    -e DB_USER=couragehe ^
    -e DB_USER_PW="123456" ^
    -e MANAGE_ADMIN=admin ^
    -e MANAGE_PASSWORD=123456 ^
    -e AUTH_REMOTE_HOST="http://login.youserver.com" ^
    %service_name%:%image_version% 
```

数据库：

+   DB_IP(数据库ip地址)
+   DB_NANE(数据库名)，启动前应先行建立该数据库。
+   DB_USER(数据库用户名)
+   DB_USER_PW(数据库密码)，由于`python`语言的特性，数据库密码不得含`% @`字符

管理员：

+   MANAGE_ADMIN(管理员用户名)，管理员用户名需与`Dockerfile`中 `--username`配置相同，如需修改管理员用户名，两处需同步修改方可生效。
+   MANAGE_PASSWORD(管理员密码)

登录主机：

+   AUTH_REMOTE_HOST(登录主机)，其中登录地址、请求参数等配置见`security/remote_server_api.py`,文件中含登录请求示例，可根据该示例自行实现登录服务。

其他配置：

+ 网页title，可在`superset_config.py[APP_NAME]`处配置
+ 应用左上角logo，可在`assets/images`文件夹中进行替换。
+ 网页logo，可在`assets/images`文件夹中进行替换。

## 使用步骤

1、打包镜像

(第一个参数为`镜像名`，第二个参数为`镜像版本`)

```cmd
>build.cmd superset 0.0.1
```

2、启动服务

指定新镜像启动为容器，开启服务。(第一个参数为`镜像名`，第二个参数为`镜像版本`)

```cmd
>start-up.cmd  superset 0.0.1
```



服务运行成功后可通过`8080`端口进行访问。

如果在本机运行，可以通过`http://localhost:8080`打开，默认账号密码：`admin/123456`

superset使用手册：https://blog.csdn.net/m0_37606374/article/details/120386913





参考：https://superset.apache.org/docs/intro

参考：https://zhuanlan.zhihu.com/p/585669109

参考：https://www.jianshu.com/p/063ccb8e2a75

