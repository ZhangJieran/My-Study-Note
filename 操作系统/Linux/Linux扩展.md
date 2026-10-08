&emsp;<a href="#ShellAndEnv">环境变量与shell</a>  <br>
&emsp;<a href="#OpenSSH">开启SSH服务</a>  <br>
&emsp;<a href="#Desktop">远程桌面</a>  <br>
&emsp;<a href="#Desktop">云服务的root权限</a>  <br>
&emsp;<a href="#file">文件互传</a>  <br>
&emsp;<a href="#live">客户端连接保活</a>  <br>








<br><br><br><br><br><br>
<div id="ShellAndEnv">
<h2><strong>环境变量与shell</strong></h2>
##############################################################<br>
配置文件&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;作用域&emsp;&emsp;&nbsp;&nbsp;执行时机<br>
~/.bashrc&emsp;&emsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;单用户&emsp;&emsp;新开终端&emsp;&emsp;<br>
~/.profile&emsp;&emsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;单用户&emsp;&emsp;开机<br>
/etc/profile&emsp;&emsp;&emsp;&emsp;&emsp;所有用户&emsp;&nbsp;&nbsp;新开终端<br>
/etc/environment&emsp;&emsp;所有用户&emsp;&nbsp;&nbsp;开机，只做环境变量，不执行脚本<br>
###############################################################
<br><br>

>[!TIP]
>1.&emsp;<strong>PATH 是一个变量，储存查找路径，写在前面的路径先查找，不同路径用 ： 分隔开</strong>
><br>
>&emsp;&emsp;e.g.PATH = "a/b/c : d/e : f/g/h"&emsp;会先查找a/b/c 再查d/e 再查f/g/h
><br><br>
>2.&emsp;<strong>$PATH 意思是取 PATH 的值</strong>

</div>
<br><br><br><br><br><br>



<div id="OpenSSH"></div>
<h2><strong>开启SSH服务</strong></h2>
################################################<br>
确保已经安装openssh-server&emsp;<em>(apt install openssh-server)</em>
<br>
systemctl start ssh&emsp;启动服务
<br>
systemctl status ssh&emsp;检验是否成功<br>
#################################################


<br>
windows连接指令

```
ssh 用户名@linux的ip地址
```
>[!WARNING]无法连接
>SSH的安全保护机制<br>
>本地之前连接过这个IP的服务器<br>
>服务器的SSH主机密钥发生了变更（比如服务器重装、重置了SSH配置、更换了系统）<br>
>本地保存的旧指纹和服务器当前的新指纹不匹配，SSH为了防止中间人攻击直接拒绝了连接。
>
>```
>解决方案：ssh-keygen -R linux_ip
>```

</div>
<br><br><br><br><br><br><br>






<div id="Desktop">
<h2>远程桌面</h2>

```
sudo apt install xrdp
```

安装远程桌面服务程序
```
sudo systemctl enable --now xrdp  开机自启动
sudo systemctl disable xrdp       关闭开机自启

sudo systemctl start xrdp         启动
```

启用 xrdp
```
sudo ufw allow from any to any port 3389 proto tcp
```
放开 xrdp 需要的防火墙端口

>[!CAUTION] 云服务器平台端也要放开 3389 端口


```
sudo vim /etc/gdm3/custom.conf
#进入文件修改:
WaylandEndable=false
```


windows 访问

```
启动"远程桌面"
填入linux机公网ip
```


</div>
<br><br><br><br><br><br>

<div id="file">
<h2>文件互传</h2>


<strong>windows向linux传文件</strong>

```
```

<strong>linux向windows传文件</strong>
powershell 执行
```
scp ubuntu@linux_ip :Linux文件路径 windows文件路径
```

</div>

<br><br><br><br><br><br>

<div>
<h2>云服务的root权限</h2>
云服务的的ubuntu用户默认在Ubuntu里已经被授予了sudo权限，不需要root密码，直接执行这条命令就能直接进入root交互环境：

```
sudo -i
```

给root设置自定义密码，解锁su root命令
```
sudo passwd root
```
</div>
<br><br><br><br><br><br>

<div id="live">

<h2>客户端连接保活</h2>
解决一段时间不操作ssh连接自动断开


```
编辑本机 SSH 配置 ~/.ssh/config（Windows 下是 C:\Users\34563\.ssh\config）：


Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
含义：每 60 秒发一次心跳，连续 3 次没响应才断开。这样空闲时连接不会断。


```
</div>
<br><br><br><br><br><br>