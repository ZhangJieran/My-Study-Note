<a href="#engine">*gin.Engine</a><br>
<a href="#context">*gin.Context</a><br>
<a href="#html">HTML模板渲染</a><br>
<a href="#file">文件上传</a><br>
<a href="#Cookie">Cookie 和 Session</a><br>



<br><br><br><br><br><br><br><br>



>[!CAUTION] Gin中中间件使用gorutine
>不能使用原始上下文的 c *gin.Context<br>
>必须使用副本c.Copy()<br>
>```
>Gin使用sync.Pool管理*gin.Context对象
>当handler开启协程，并return后:
>gorutine还在跑(没有用WaitGroup的话)
>但sync认为该c *gin.Context可以复用，因为之前用它的handler已经跑完了
>于是另一个handler拿到c并写入数据
>但是后台还在运行的goroutine持有c的指针！尽管c的handler已经变了
>```
>```golang
>engine.GET("/",func(c *gin.Context){
>   cCopy:=c.Copy()
>   go func(){
>       ...           
>   }()
>
>   ...
>})
>
>```




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



<br><br><br><br><br>

<a id="engine"></a>

## *gin.Engine


>[!TIP]<strong>可以把 *gin.Engine理解成最顶层的 *gin.Router</strong>
<details>
<summary><strong>方法概览</strong></summary>



|方法|解释
|---|---
|`Static("path1","path2")`|当请求路径以path1开头时<br>去本地的path2目录下找
|`LoadHTMLGlob("包含html文件夹路径")`<br>`LoadHTMLFiles("html文件路径"...)`|见下面模板渲染
|`GET/POST/PUT(code int,handler ...func)`|第一个参数是状态码<br>后面就是执行的func
|`ShouldBind(&结构体)`|通过结构体元信息说明的映射关系给结构体赋值<br>返回error
|`Group("路由")`|路由分组,返回*gin.RouterGroup
|`Next()`|暂停执行现在的函数，去执行后面的中间件以及最终处理函数<br>最后再回来执行该函数剩下部分
|`Abort()`|不会再继续执行后买你的handler函数，但当前的handler会执行完
|`Use(...func)`|配置全局中间件



>[!IMPORTANT] handler执行链
>全局Use->父Group Use->当前Group Use->GET等方法里带的中间件
</details>


<details id="Bind">
<summary><strong>路由分组</strong></summary>

```golang
UserRouters := Engine.Group("/usr")

UserRouters.GET("/get"...) // 相当于“/usr/get”
UserRouters.POST("/post"...)
...
```

</details>







<details id="Bind">
<summary><strong>ShouldBind</strong></summary>

#### ShouldBind(结构体指针)

```golang
// 发来的json里有字段a,b时自动给Name,Age赋值
// 发来的form里有字段c,d时自动给Name,Age赋值
type UsrInfo struct {
	Name string `json:"a" form:"c"`
	Age  int    `json:"b" form:"d"`
}

func main() {
    r.Default()

	
    r.GET("/GetNum", func(c *gin.Context) {
        usr := &UsrInfo{}
        c.ShouldBind(usr) 
	})


	r.Run()
}
```

|字段|触发
|---|---
|`json`|解析JSON请求体
|`form`|URL查询字段+表单 e.g.`usr/hi？a=11`
|`yaml`|yaml请求体
</details>










<details>
<summary><strong>GET</strong></summary>
<br>

<strong>
:占位符名 ( 假设给定占位符 :id ) <br>
对于路由"/usr/:id"，可以localhost/usr/content 访问,此时Param("id")就是content<br>
对于路由"/usr:id"，可以localhost/usrcontent 访问,此时Param("id")就是content<br>
</strong>

```go
GET("/usr/:id",func(c *gin.Context){
   id := c.Param("id")  // 注意：Param 返回字符串
})
```

<strong>
获取传入的变量:<br>
/usr/content?字段=10
</strong>


```go
// 返回string
c.Query("字段") //没有这个字段就返回""
c.GetQuery("字段") //返回(string,bool)
c.DefaultQuery("字段",默认值 string)
```
</details>

<details>
<summary><strong>POST</strong></summary>

</details>



---

</details>



<br><br><br><br><br><br><br><br><br>











<a id="context"></a>

## *gin.Contex

<details>
<summary><strong>方法</strong></summary>

---

|方法|解释
|---|---
|`String(int,string,...any)` |类似于Printf的写法，多了第一个参数(状态码)
|`JSON(int,any)`|第一个参数是状态码,第二个一般传`map[string]any`
|`JSONP(int,any)`|
|`Set(Key,Val)`|仅在本次网络请求生效，把键值对放入上下文传递
|`Get(Key)`|返回(val bool),通过Key拿到Val


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

<br><br><br><br><br>

<a id="html"></a>

## HTML模板渲染

<details>
<summary><strong>例子</strong></summary>

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
<br><br><br><br><br><br><br><br>








<a id="file"></a>


## 文件上传


<details>
<summary><strong>单文件上传</strong></summary>


```golang
POST(...,func(c *gin.Context){
    // <input type="file" name="FileName">
    file,err := c.FormFile("FileName")
    // 获取文件名
    log.Println(file.Filename)
    // 保存本地
    c.SaveUploadFile(file,"保存路径/"+file.Filename)    
})
```
</details>
<br>


<details>
<summary><strong>多文件上传</strong></summary>

```golang
POST(...,func(c *gin.Context){
    // 拿到提交的整个表单
    form,err := c.MultipartForm()
    // <input type="file" name="FileName">
    files := form.File["InputName"]
    
    for i,file := range files {
        c.SaveUploadFile(file,"./"+file.Filename)
    }    
})
```
</details>
<br>







<a id="Cookie"></a>

## Cookie 和 Session

<details>
<summary><strong>Cookie</strong></summary>

```go
c.SetCookie(
    name string,      // Cookie名
    value string,     // Cookie值
    maxAge int,       // Cookie有效时长(s)。maxAge<0表示删除Cookie
    path string,      // Cooke生效的路由前缀
    domain string,    // Cookie发送到哪个域名(只写域名)，不带端口，路径，协议头
    secure bool,      // Cookie只在https中生效 
    httpOnly bool,    // 禁止前端js读取document。cookie
)
```
<br>
e.g.

```go
c.SetCookie("usrname","Jack",3600,"/","localhost",false,false)
```

domain实现二级域名共享Cookie

```go
// a.test.com 和b.test.com 都能共享这个Cookie
c.SetCookie("usrname","Jack",3600,"/",".test.com",false,false)
```
</details>
<br>



<details>
<summary><strong>Session</strong></summary>

```go
github.com/gin-contrib/sessions
github.com/gin-contrib/sessions/cookie


// engine是路由引擎 
// 配置session中间件
// 创建基于cookie的存储引擎,传入一个密钥用于加密
store := cookie.NewStore([]byte("secret"))
// 配置session中间件
engine.Use(sessions.Sessions("mysession",store))

engine.GET("/",func(c *gin.Context){
    // 获取 session 对象
    session := session.Default(c)
    // 设置session
    session.Set("usrname","Jack")
    session.Save()
    // 读取session
    session.Get("usrname")
})


```

</details>
