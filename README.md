# Price_Tag
#1，安装docker
#2，在命令行中运行：
#docker pull tomcat:latest #获取当前云端最新版本的tomcat服务装在docker里
#3，将war包放到tomcat的目录下
#4，将Dockerfile中 ADD 命令后面的目录改为本地目录
#5，将docker-compose.yml中的镜像目录改为本地目录 
#6，在docker中构建：
#docker build -t python/tomcat . # . 代表当前目录
#docker build -t search/tomcat .
#7,启动服务 #docker run
##PS compose里面的镜像路径也要改成本地路径，没有的话用sudo建一个
##PS html前端的ip地址需要改一下
