@REM 第一个参数为服务名
set service_name=%1

@REM 第二个参数为镜像版本号
set image_version=%2

@REM 输出日志
echo "%date% [INFO] project: %service_name%, image_version: %image_version%"

docker build -t %service_name%:%image_version% .

start-up.cmd %service_name% %image_version%
