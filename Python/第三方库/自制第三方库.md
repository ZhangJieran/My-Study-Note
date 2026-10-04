先建一个根目录，假设将其命名为 myLibrary<br>

===================================项目结构===========================<br>

```
                ProjectName
                /         \
               V           V
      pyproject.toml     库名(import导入名)       
                          |            |                   
                          V            V
                      __init__.py    代码文件
```
======================================================================<br>

ProjectName下可以有README.md 作为说明,LICENSE 开源协议

<h3>pyproject.toml写法</h3>

``` 
[ build-system ] 
requires = ["setuptools>=61.0","wheel"]
build-backend = "setuptools.build_meta"
```
这里几乎是固定格式，不用改，setuptools是打包工具，要大于61.0才支持.toml文件

```
[ project ]
name = "库名"  pip安装名
version = "0.1.0" 库更新就变成0.1.1 0.2.0 ……
authors = [ { name = “ZhangJieran",email = "3456377465@qq.com" } ]
description = "介绍这个库"
requires-python = ">=3.8" 最低支持py3.8
dependencies = [ "opencv>=1.1","pillow>=1.2" ]  这个库依赖的第三方库
```

```
[ project.scripts ]  
SayHello = " tool.func : Hi "
```
非必须，可选<br>
当终端敲下SayHello 就会去 tool.func 里找 Hi 这个函数执行<br>
指令名 = "路径：函数名" &emsp;&emsp;这个路径是已经在ProjectName时的相对路径
<br>
这个文件主要做脚本用的，它会在pip所在的环境文件的Script文件里生成一个exe文件，这个exe文件依赖当前的py解释器


注意：以顶图为例，路径的起始并非ProjectName，是ProjectName下的“库名”这个文件
<br>
<br>
<h3>上传PyPI</h3>
终端位于ProjectName这一层
pip install –upgrade setuptools wheel build twine  安装打包工具<br>
python -m build<br>   
运行完项目会多出dist文件夹:<br>
.tar.gz源码包    .whl 安装包   这就是要上传的文件<br>
twine upload dist/* 上传PyPI
