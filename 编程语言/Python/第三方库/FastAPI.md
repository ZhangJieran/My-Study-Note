<a href="#install">安装fastapi</a><br>
<a href="#use">使用</a><br>

<a href="#CORS">CORS</a><br>
<br><br><br><br><br><br><br><br>




<div id="install">

## 安装fastapi 

`pip install "fastapi[standard]" `uvicorn也一起安装了<br>
</div>
<br><br><br><br><br><br><br><br>

<div id="use">

## 使用

<details>
<summary><strong>示例</strong></summary>

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/路径") #判断路由
def myFunc(arg1,arg2):
    return ...

# 访问http://127.0.0.1:8000/路径/myFunc?arg1=xxx&arg2=xxx 获得返回值
```


手动指定

```py
app.get("/路径")
def myFunc():
    # 手动定义响应头
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "X-Custom-Header": "我自己加的自定义头",
        "Cache-Control": "no-store"
    }

    returnJson = {
        ...略，定义返回的json
    }
    # 手动指定状态码、响应头、内容
    return JSONResponse(
        content=retrunJson,
        status_code=200,
        headers=headers
    )

```
</details>
<br>

#### 启动API

- <strong>终端运行</strong> &emsp; `uvicorn 文件名不带后缀:FastAPI实例名 --host 0.0.0.0 --port 8000 --reload` <br>
reload的意思是代码被修改就自动重启api<br>
host是监听IP,port是端口号
- <strong>代码里写</strong>&emsp;`uvicorn.run(app, host="0.0.0.0", port=8000)`
</div>
<br><br><br><br><br><br><br><br>








<div id="CORS">

## CORS

<details>
<summary><strong>示例</strong></summary>

```py
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["https://..."],  # 允许的跨源请求
    allow_methods = ["GET","POST"],   # 允许的方法
    allow_headers = ["*"]             # 允许的请求头(*是所有的意思)
)
```

</details>

</div>
<br><br><br><br><br><br><br><br>
