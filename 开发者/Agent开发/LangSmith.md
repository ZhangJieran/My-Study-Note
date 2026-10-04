在 <a href="https://smith.langchain.com">https://smith.langchain.com</a>获取api_key
```
点击左侧导航栏Settings
```
<br><br>
.env中添加环境变量

```
#是否启用LangSmith
LANGSMITH_TRACING  = true

#LangSmith监控的WebUI地址
LANGSMITH_ENDPOINT = https://api.smith.LangChain.com

#创建api_key
LangSMITH_API_KEY  = <your api_key>

#自定义项目名称
LANGSMITH_PROJECT  = "pr=clear-harmony-32"
```


