<a href="#redis配置文件">redis配置文件</a><br>
<a href="#data">数据结构</a><br>
<a href="#rediscli">redis-cli</a><br>


<br><br><br><br><br><br><br><br>

<a id="redis配置文件"></a>

## redis配置文件

修改 `/ect/redis/redis.conf`

<details>
<summary><strong>配置详情</strong></summary>

|配置项|作用
|---|---
|`bind 0.0.0.0`| 监听地址
|`daemonize yes`| 守护进程，后台运行     
|`requirepass 123456`|设置密码,访问redis必须输入密
|`database 1`|redis数据库数量，默认16
|`maxmemory 512mb`|redis最大使用内存
|`dir .`|指定工作目录
|`logfile "redis.log"`|日志文件，默认为空不记录日志<br>日志文件在工作目录下
</details>
<br><br><br><br><br><br><br><br>






<a id="data"></a>

## 数据结构

key是string类型

|val类型|示例
|---|---
|String|`"hello world"`
|Hash|`{name:"jack",age:21}`
|List|`{A->B->C}`
|Set|`{A,B,C}`
|SortedSet|`A:1,B:2,C:3`
|GEO|`{A:(120.3,30.5)}`<br>坐标(经度，纬度)
||

<details>
<summary><strong>String</strong></summary>

|命令|含义
|---|---
|`SET`|添加/修改键值对
|`GET`|获取val
|`MSET`|批量添加多个键值对
|`MGET`|批量获得多个键值对
|`INCRBY`|指定步长自增
|`INCRBYFLOAT`|指定步长浮点数自增


- `SET [key] [val] NX`新增，只有key不存在才添加。存在则不会修改
- `SET [key] [val] EX [seconds]`新增，并设置有效日期
</details><br>

<details>
<summary><strong>Hash</strong></summary>

key field val

|命令|含义
|---|---
|`HSET`|添加/修改key的field的值
|`HGET`|获取val
|`HMSET`|批量添加
|`HMGET`|批量获得
|`HGETALL`|获得一个hash类型key中所有的field和val
|`HKEYS`|获得key中所有的field
|`HVAlS`|获得key中所有val
|`HINCRBY`|自增,并指定步长
|`HINCRBYFLOAT`|浮点型的自增

</details><br>


<details>
<summary><strong>List</strong></summary>
双向链表<br>

|命令|含义
|---|---
|`LPUSH / RPUSH`|添加key
|`LPOP / RPUSH`|移除并返回首元素
|`LRANGE`|返回指定角标范围所有元素<br>LRANGE 0 -1 一次返回所有元素
|`LLen`|链表长度

>[!CAUTION]LRANGE [l,r] 左右都是闭区间


</details><br>



<details>
<summary><strong>Set</strong></summary>

|命令|含义
|---|---
|`SADD`|添加元素
|`SREM`|移除元素
|`SCARD`|返回元素个数
|`SISMEMBER`|某个key是否在Set中
|`SMEMBERS`|获取集合中所有元素

<br>

|算法|含义
|---|---
|`SINTER`|求交集
|`SDIFF`|求差集合
|`SUNION`|求并集

</details><br>


<details>
<summary><strong>SortedSet</strong></summary>

|命令|含义
|---|---
|`ZADD`|添加元素
|`ZREM`|移除元素
|`ZCARD`|返回元素个数
|`ZSCORE`|获取指定元素的score值
|`ZRAMK`|获取指定元素的排名
|`ZCOUNT`|统计score值在指定范围内的元素个数
|`ZINCRBY`|score自增
|`ZRANGE`|指定排名内的元素
|`ZRANGEBYSCORE`|指定score内的元素

<br>

|算法|含义
|---|---
|`ZINTER`|求交集
|`ZDIFF`|求差集合
|`ZUNION`|求并集

</details><br>


<br><br><br><br><br><br><br><br>




<a id="rediscli"></a>

## redis-cli

`redis-cli [options] [commands]`<br>

一般先 redis-cli [options]连上再输[commands]


<details>
<summary><strong>redis-cli</strong></summary>

|options|含义
|---|---
|`-h 127.0.0.1`|指定连接的IP地址，默认127.0.0.1
|`-p 6379`|指定连接端口，默认6379
|`-a 123456`|指定redis访问密码

</details>
<br>

<details>
<summary><strong>通用命令</strong></summary>

|通用命令|含义
|---|---
|`help [command]`| 查看指定命令的介绍 
|`KEYS`|查询符合模板的所有key
|`DEL`|删除
|`EXISTS`|判断key是否存在
|`EXPIRE`|给key一个有效期，过期自动删除
|`TTL`|查看一个key的有效期，-2表示已经过期，-1表示永久有效

</details>
<br><br><br><br><br><br><br>
