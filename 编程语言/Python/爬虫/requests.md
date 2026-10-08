<a href="#response">Response</a>
<a href="#BeautifulSoup">BeautifulSoup</a>

<br><br>
<div id="response"></div>
<h3>Response</h3>
<strong>属性</strong>

```
status_code     状态码
text            HTML源码
content         原始字节流
```

<strong>方法</strong>

```
get("网址",header=Dict[Any])
```
get里的header用来设置请求头追加/覆盖

```
cookie_dict = {
    "sessionid" : "abc123",
    "user_id"   : "12345",
    "token"     : "xyz999"
}

header = {
    "User-Agent" : "Mozulla/5.0(Windows NT 10.0;Win64;x64)",
    "Cookie"     : cookie_dict
    ......
}
```
返回Response

<div id="BeautifulSoup">
<h3>BeautifulSoup</h3>
BeatifulSoup是一个类，不属于requests<br>

```
pip install bs4
from bs4 import BeautifulSoup
```
它用于把Response.text以树状的形式展现出来

```
content = requests.get("https://.......").text
soup = BeautifulSoup(content,feature="html.parser")
```
第二个参数是解析器<br><br>

<strong>方法</strong>

```
findAll("标签",{"属性":"值", ......})

e.g.
soup.find_all("div",
    {
        "class" = "className",
        "id"    = "idNum",
        ......
    }
  )
```
找到特定的标签,以及这个标签下的子标签,返回可迭代对象


```
find_all()返回的内容会包含标签本身，如果只想要标签包含的的内容

find_all(......).string
```




</div>