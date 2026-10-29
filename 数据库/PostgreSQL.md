
<a href="#PostgreSQL">PostgreSQL安装与启动</a><br>
<a href="#dataType">数据类型</a><br>
<a href="#basicuse">PostgreSQL基本使用</a><br>
<a href="#func">常用函数</a><br>
<a href="#visit">修改配置文件</a><br>


<br><br><br><br><br><br><br><br><br>

<div id="PostgreSQL">
<h2>PostgreSQL安装与启动</h2>

```
sudo update apt
sudo apt install postresql postgresql-contrib -y 安装主程序与扩展组件
```

启动客户端

```
sudo -u postgres psql
```
</div>
<br><br><br><br><br><br><br><br><br>













<a id="dataType"></a>

## 数据类型

<details>
<summary><strong>整数</strong></summary>

|整数类型|字节
|---|---
|smallint| 2字节
|int| 4字节
|bigint| 8字节
</details>
<br>


<details>
<summary><strong>浮点数</strong></summary>

|浮点数类型|解释
|---|---
|numerice |定点数,金融必用,无精度丢失
|real| 单精度浮点数
|double precision| 双精度浮点数
</details><br>

<details>
<summary><strong>字符串</strong></summary>

|字符串类型|解释
|---|---
|test| 无上限长度字符串
|varchar(n) |变长字符串，限制最大长度为n
</details>
<br>

<details>
<summary><strong>布尔BOOLEAN</strong></summary>

```
true/false/null
```
</details><br>

<details>
<summary><strong>数组</strong></summary>

声明`类型[]` e.g.`text[]`

```SQL
INSERT INTO demo(字段)
VALUES (ARRAY['hello','world']);
```
</details>
<br>

<details>
<summary><strong>JSON/JSONB</strong></summary>

用单引号包起来
e.g.

```SQL
INSERT INTO demo(字段)
VALUES ('{"name":"jack","age":10}');
```
</details><br>


<details>
<summary><strong>时间</strong></summary>

|类型|含义
|---|---
|date|日期
|time|时间
|timestamp|时间戳
|timestampz|带时区时间戳

`now()` 返回当前timestampz
</details>

#### UUID
全局唯一id,分布式场景 

<br><br><br><br><br><br><br><br><br>








<div id="basicuse">
<h2>PostgreSQL基本使用</h2>


<br>
创建用户

```
CREATE USER 用户名 WITH PASSWORD '密码';
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

|1|1
|---|---
|`CREATE DATABSE/SCHEMA xxx`|创建
|`DROP DATABASE/SCHEMA <名> CASCADE`|删除库,加CASECADE表示联级删除
|`\l`| 查看有哪些库,退出用 \q
|`\c <库名>`|进入库
|`\dn`|查看schema

<details>
<summary><strong>表操作</strong></summary>

建表

```SQL
CREATE TABLE <schemaName>.<TableName> (
    字段 类型 约束,
    字段 类型 约束,
    ...
);
```

继承
```SQL
// 继承OtherTable
CREATE TABLE <tableName>(
    字段 类型 约束,
    ...
)INHERITS( <OtherTable> );
```

#### 改表结构

|操作|命令
|---|---
|查看表具体内容|`\d <schema>.<table>`
|查看schema下的所有表|`\dt <schema>.<table>`
|添加字段|`ALTER TABLE <schema>.<table> ADD COLUMN <字段> <类型> <约束>`
|删除字段|`ALTER TABLE <schema>.<table> DROP COLUMN <字段>`
|修改字段类型|`ALTER TABLE <schema>.<table> ALTER COLUMN <字段> TYPE <类型>`
|重命名字段|`ALTER <schema>.<table> RENAME COLLUMN <字段> TO <字段>`


</details>

<details>
<summary><strong>CRUD</strong></summary>

增

```SQL
INSERT INTO <tableName> (字段，字段 ...)
VALUES 
    ('字符串1',124,true,ARRAY['t1','t2']),
    ('字符串2',124,true,ARRAY['t1','t2']);
```


删

```
# 清空数据
truncate table <tableName>
# 清除数据以及数据结构
DROP TABLE <tableName>
```



改

```SQL
UPDATE <tableName> 
SET 字段 = xxx , 字段 = xxx
WHERE ... ;
```


查

```SQL
SELECT xxx FROM <tableName>;
SELECT xxx FROM <tableName> WHERE ... AND/OR ...;
SELECT xxx FROM <tableName> WHERE 字段 LIKE 'hello__orld'; 

SELECT xxx FROM xxx WHERE created_at>='2026-01-01';

数组查询
SELECT xxx FROM xxx WHERE '文档' = ANY(数组字段);
SELECT xxx FROM xxx WHERE 数组字段 @> ARRAY['文档','封面'];   # 与逻辑，同时包含
SELECT xxx FROM xxx WHERE 数组字段 && ARRAY['文档','封面'];   # 或逻辑，包含其中一个

Json查询
如果取出来的还需继续取字段，用->，最后用->>取出来的是text,用int转成整数
SELECT xxx FROM xxx WHERE (Json字段 -> 'group' -> 'name' ->> 'age')::int = 20;
筛选有某一字段的json
SELECT xxx FROM xxx WHERE json字段 ? '字段'; 

排序
SELECT xxx FROM xxx order by 字段 asc/desc; 升/降序查询，asc表示升序，desc降序

查2条
SELECT xxx FROM xxx limit 2
```

一个'_'占一个字符

</details>
</div>

<br><br><br><br><br><br><br><br><br>








## 常用函数

<details>
<summary><strong>字符串处理</strong></summary>

|函数|作用
|---|---
|`CONCAT(a,b)`|拼接
|`SUBSTR(string,start,len)`|截取字符串
|`REPLACE(string,from,to)`|替换
|`COALESCE(value,default)`|返回第一个非NULL,如果字段是NULL,就给它默认值
|`UPPER()/LOWER()`|转换大小写
||
</details><br>

<details>
<summary><strong>数值计算</strong></summary>

|函数|作用
|---|----
|`ABS()`|绝对值
|`ROUND(umeric,int)`|四舍五入,int是要保留小数位数
|`CEIL()/FLOOR()`|向上/下取整

</details><br>

<details>
<summary><strong>日期时间</strong></summary>

|函数|作用
|---|---
|`NOW()`|当前完整时间(日期 时间 时间戳)
|`AGE(timestamp1,timestamp2)`|时间差,timestamp1-timestamp2
</details><br>





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













