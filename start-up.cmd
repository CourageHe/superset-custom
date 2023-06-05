
@REM 删除原容器
docker stop superset && docker rm superset
@REM Windows中多行执行一个命令，使用 '^' 连接
@REM 数据库密码不能含 '%' '@'

@REM 第一个参数为服务名
set service_name=%1
@REM 第二个参数为镜像版本号
set image_version=%2

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


