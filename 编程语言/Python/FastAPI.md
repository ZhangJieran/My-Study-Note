









#### 安装fastapi 

`pip install "fastapi[standard]" `uvicorn也一起安装了<br>


```
from fastapi import FastAPI

app = FastAPI()

@app.get("/路径") #判断路由
def myFunc(arg1,arg2):
    return ...

# 访问http://127.0.0.1:8000/路径/myFunc?arg1=xxx&arg2=xxx 获得返回值
```



手动指定

```

app.get("/路径")
def myFunc():
    # 手动定义响应头
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "X-Custom-Header": "我自己加的自定义头",
        "Cache-Control": "no-store"
    }

    returnJson = {
        ...略，这是返回的json
    }
    # 手动指定状态码、响应头、内容
    return JSONResponse(
        content=retrunJson,
        status_code=200,
        headers=headers
    )

```


<br>

#### 启动API

- <strong>终端运行</strong> &emsp; `uvicorn 文件名不带后缀:FastAPI实例名 --host 0.0.0.0 --port 8000 --reload` <br>
reload的意思是代码被修改就自动重启api<br>
host是监听IP,port是端口号
- <strong>代码里写</strong>&emsp;`uvicorn.run(app, host="0.0.0.0", port=8000)`






