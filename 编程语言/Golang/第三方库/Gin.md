
```golang
// 创建默认路由引擎,返回*gin.Engine
engine := gin.Default()  
// 配置路由
engine.GET("路由",func(c *gin.Context){
    // 返回字符串
    c.String(200,"hello %v","jack")  
})
// 启动在8000端口启动Web服务
engine.Run(":8000")
```

>[!TIP] 传参
>参数嵌在路径里:<br>
>
>```go
>GET("/usr/:id",func(c *gin.Context){
>   id := c.Param("id")  // 注意：Param 返回字符串
>})
>```

<br><br><br><br><br>



<details>
<summary><strong>*gin.Engine</strong></summary>

---

|方法|解释|例子
|---|---|---
|`Static("path1","path2")`|当请求路径以path1开头时<br>去本地的path2目录下找|`Static("/assets","./assets")`
|`LoadHTMLGlob("包含html文件夹路径")`<br>`LoadHTMLFiles("html文件路径"...)`|见下面模板渲染|&emsp;&emsp;&emsp;&emsp;\
|`GET/POST/PUT`|第一个参数是路由<br>第二个参数func|&emsp;&emsp;&emsp;&emsp;\



---

</details>
<br><br>
<details>
<summary><strong>*gin.Context</strong></summary>

---

|方法|解释
|---|---
|`String(int,string,...any)` |类似于Printf的写法，多了第一个参数(状态码)
|`JSON(int,any)`|第一个参数是状态码,第二个一般传`map[string]any`
|`JSONP(int,any)`|

```go
func(c *gin.Context) {
    c.String(200,"值：%v",100)
}

func(c *gin.Context) {
    c.JSON(200,map[string]any{
        "success" : true,
        "msg"     : "Hello",
    })
}

func(c *gin.Context) {
    c.JSONP(200,map[string]any{
        "success" : true,
        "msg"     : "Hello",
    })
}
```

---

</details>

<br><br>

<details>
<summary><strong>模板渲染</strong></summary>

---

```
myapp/
├── main.go
└── templates/
    ├── index.html
    └── user.html
```

```go
r := gin.Default()
// 加载 templates 目录下所有 .html（支持子目录，如 templates/**/*.html）
r.LoadHTMLGlob("templates/*")
// 一个一个指定加载：
r.LoadHTMLFiles("templates/index.html", "templates/user.html",...)

r.GET("/", func(c *gin.Context) {
    c.HTML(http.StatusOK, "index.html", gin.H{
        "title":   "我的首页",
        "name":    "小天",
        "items":   []string{"Go", "Gin", "Template"},
        "isLogin": true,
    })
})
```
#### 对应 index.html 里通过 {{ .变量 }} 的形式拿到值
#### {{ funcName .var1 .var2 }} 相当于调用函数funcName(var1,var2) 

---

</details>

