
<a href="#PostgreSQL">PostgreSQL安装与启动</a><br>
<a href="#basicuse">PostgreSQL基本使用</a><br>
<a href="#visit">修改配置文件</a><br>


<br><br><br><br><br><br><br><br><br>

<div id="PostgreSQL">
<h2>PostgreSQL安装与启动</h2>

```
sudo update apt
sudo apt install postresql postgresql-contrib -y 安装主程序与扩展组件
```

```
sudo systemctl status postgresql 查看程序运行状态
```

```
sudo systemctl start postgresql   启动程序
sudo systemctl enable postgresql  开机自启动
sudo systemctl disable postgresql 关闭自启动
```

</div>

<br><br><br><br><br><br><br><br><br>


<div id="basicuse">
<h2>PostgreSQL基本使用</h2>

启动客户端

```
sudo -u postgres psql
```
<br>
创建用户

```
create USER 用户名 WITH PASSWORD '密码';
```
<br>
创建数据库

```
create DATABASE 数据库名 OWNER 所属用户;
```
<br>
赋权

```
GRANT ALL PRIVILEGES ON DATABASE 数据库名 TO 用户名;
```
<br>

查看数据表

```
\l 回车 ，退出用 \q
```
</div>

<br><br><br><br><br><br><br><br><br>




<div id="visit">
<h2>修改配置文件</h2>

```
psql "postgresql://用户名:密码@IP地址:5432/数据库名?sslmode=disable"
```

>[!WARNING] 默认监听的是本地回环监听，用IP地址连接会报错，这需要修改配置文件才行
>
>```
>======== step1 : 放通网络限制 ========
>查看配置文件位置
>sudo -u postgres psql -c "SHOW config_file;" 
>
>修改：listen_addresses = '*'
>
>防火墙5432端口也要放行
>
>======== step2 : 放通访问限制 ========
>查看配置文件位置
>sudo -u postgres psql -c "SHOW hba_file;" 
>
>在文件最后添加:
>host 数据库名 用户名 0.0.0.0/0 scram-sha-256
>```
最后重启服务即可
</div>




存储结构

```
Database数据库 -> Schema分区 -> Table数据表
```

<br>
查看分区

```
\dn    查看所有分区
select current_schema();  查看当前所在分区

```
<br>

查看数据表

```
\dt
```













