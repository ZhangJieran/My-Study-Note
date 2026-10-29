 <a href="#VisibleGraph">图结构可视化</a><br>
<a href="#State">状态</a><br>
<a href="#node">节点</a><br>
<a href="#edge">边</a><br>
<a href="#while">循环 ReAct</a><br>
<a href="#managed">托管状态类型</a><br>
<a href="#compile">compile</a><br>
<a href="#checkpointer">checkpointer</a><br>

<br><br><br><br><br><br><br><br>

<div>
<details>
<summary><strong>LangGraph框架概览</strong></summary>

```py
# 定义状态
class OverAllState(TypedDict):
    logs:Annotated[list[str],add]  # add是追加的意思
    cur_id:str

# 定义节点
def node_1():pass
def node_2():pass 

builder = StateGraph( state_schema=OverAllState ) 获取建造者

# 添加节点
builder.add_node( node_1 )
builder.add_node( node_2 )

# 添加边
builder.add_edge(START,"node_1")
builder.add_edge("node_1","node_2")
builder.add_edge("node_2",END)

# 获取图:CompiledStateGraph
MyGraph = builder.compile()
```

</details>
</div>
<br><br><br><br><br><br><br><br>



<div id="VisibleGraph">

## 图结构可视化

```py
MyGraph : CompiledStateGraph

print( MyGraph.get_graph().draw_mermaid() )
```
print打印出来的复制粘贴到markdown代码块(mermaid代码块)
即可看到可视化图



</div>
<br><br><br><br><br><br><br><br>








<a id="State"></a>




## 状态

<details>
<summary><strong>状态分类</strong></summary>

|状态|StateGraph字段|含义
|---|---|---
|全局状态|state_schema |
|输入状态|input_schema |invoke 传入state格式
|输出状态|output_schema|invoke 输出state格式
|私有状态||图内部传递的临时状态
</details><br>

<details>
<summary><strong>状态更新</strong></summary>

```
node函数里return -> 查看该字段是否有reducer :
有-> 根据reducer更新该字段
无-> 直接覆盖
```

``` python
class MyState(BaseModel):
    # 添加reducer,add_messages是内置的reducer
    # 表示更新消息列表时追加，不写则是覆盖
    messages:Annotated[list[BaseMessage],add_messages]
    state_id:int

def node(state:MyState)->dict:
    return {
        # 所有的key都要是字符串
        "messages":[AIMessage(content="hello",id='10')],
        "state_id": state.state_id + 1
    }
```
</details><br>

<details>
<summary><strong>reducer</strong></summary>

#### add_messages(old_msg:list[BaseMessage],new_msg:list[BaseMessage])

```
返回合并后的list[BaseMessage]
会根据id合并，同一message会被覆盖
```

>[!CAUTION]同一message判断标准只有id
>比如HumanMessage和AIMessage id相同，会被判定为重复message<br>

#### 自定义reducer:

```py
func MyReducer(old,new):
    ...
    return ...
```

</details>

<br><br><br><br><br><br><br><br>






<a id="node"></a>

## 节点

```py
# 定义节点
def node(state,config:RunnableConfig):
    ...

# 参数是节点名称和对应的节点函数
builder.add_node(str,func)
```



<details>
<summary><strong>Command跳转</strong></summary>

```py
func node():
    ...
    return Command(
        update:dict = ...,      #更新状态
        goto:str    = NodeName,
    )

```
</details><br>



<details>
<summary><strong>add_node()更多参数</strong></summary>

```py
add_node(
    str,
    func,
    # 重试控制
    # 重试次数耗尽/不再触发重试错误类型白名单里，报错
    retry_policy=RetryPolicy(
            max_attempts=int,      # 最大重试次数
            retry_on:Sequence      # 哪些异常要触发重试,不写默认所有异常
            initial_interval:float,# 第一次重试等地时间(s)
            backoff_factor:float,  # 重试后等待时间放到倍数
            jitter:bool,           # 是否为重试间隔添加随机抖动
    ),
    # 超时控制
    # 超时抛出NodeTimeoutError交给retry_policy判断是否需要重试
    # 仅适用于异步节点
    timeout=TimeoutPolicy(
        run_timeout=60,       # 单次节点运行最长时间
    ),
    # 一般返回状态最近更新，并Command到其他节点
    error_handler：func,
    # 节点缓存,保存输出，下次输入一样时直接返回保存的输出
    cache_policy = CachePolicy(
        ttl=int, # ttl 缓存存活时间(s),默认None永不过期
        key_func # 缓存py自带的数据结构不用指定key_func,其它要  
    )
)


# 编译时需指定缓存后端(这里是内存)
builder.compile(cache=InMemoryCache())
```
</details>
<br>


<details>
<summary><strong>全图默认节点配置</strong></summary>

```py
builder.set_node_defaults(
    retry_policy,
    timeout,
    error_handler,
    cache_policy
)
```
</details><br>








<br><br><br><br><br><br><br><br>

<a id="edge"></a>

## 边

```py
# 与,只有node1,node2都执行完才会执行node3
add_edge(["node1","node2"],"node3")  
```

<details>
<summary><strong>条件选择</strong></summary>

```py
add_conditional_edges(
    self,
    source:str,             # 条件分支起始节点
    path:func,              # 路由规则 
    path_map:dict[str:str]  # 路由规则的返回值(k)映射为节点(v)
)                           # 也可以不用path_map,但路由返回值必须要和节点名字一样     
```

示例

```py
def router(state:OverallState)->list[Literal["node1","node2"]]:
    if ... :
        return ["node1","node2"]
    else : 
        return ["node2"] 
builder.add_conditional_edges(
    START,
    router,
    path_map={
        "node1":"firstNode",
        "node2":"secondNode"
})
```
</details><br>

<details>
<summary><strong>Send动态添加边</strong></summary>

必须是add_conditional_edges<br>
<br>
并行执行

```py
func router(...):
    ls = [Send("nodeName": str,update  : dict) for ... in ...]
    return ls   

# 列表里填允许动态生成的节点
builder.add_conditional_edges("nodeName",router,["nodes"])
# 动态生成的nodeName节点走完后走NextNode
builder.add_edge("nodeName","NextNode") 
```


</details>

<br>
<details>
<summary><strong>Command跳转</strong></summary>

写在节点里面

```py
func node():
    ...
    return Command(
        update:dict = ...,
        goto:str    = NodeName,
    )

```
</details>
<br><br><br><br><br><br><br><br>






<a id="while"></a>

## 循环 ReAct

<details>
<summary><strong>ReAct循环</strong></summary>

```py
# 创建LLM模型并绑定工具
model = init_chat_model(...)
model = model.bind_tools([tool1,tool2])

class OverallState(BaseModel):
    messages:list[BaseMessage]

def LLMNode():
    ...

def ToolNode(state:OverallState):
    # 拿到模型返回的工具调用信息
    messages = state.messages
    ai_msg = messages[-1]
    tool_calls = ai_msg.tool_calls
    
    for tool_call in tool_calls:
        if tool_call["name"] == "ToolName":
            if 调用失败 :
                messages.append(ToolMessage(
                    content="调用失败",
                    tool_call_id = tool_call["id"]
                ))
            else :
                messages.append(ToolName.invoke(tool_call))
        else if toolcall["name"] == ...:
            ...
    return {
        "messages":messages
    }

# 构建图
builder = StateGraph()
...
# 实现循环,router里写跳出循环逻辑
builder.add_conditional_edges("LLMNode",router)
builder.add_edge("ToolNode","LLMNode")
builder.add_edge("OutputNode",END)
```
</details>



<br><br><br><br><br><br><br><br>

<a id="managed"></a>

## 托管状态类型
<br>
先在状态里声明,后面无需自己维护，直接拿来用

```py
class OverallState(BaseModel):
    remaining_steps:RemainingSteps
```

<details>
<summary><strong>langgraph.managed</strong></summary>

|类|含义
|---|---
|`RemainingSteps`| recursion_limit剩余超步数量


</details>

<br><br><br><br><br><br><br><br>






<a id="compile"></a>

## compile

```
builder.compile(
    checkpointer=...,
    cache=...

)
```


<br><br><br><br><br><br><br><br>







## checkpointer

|类名|检查点后端
|---|---
|InMemmorySaver|内存
|SqliteSaver|SQLite
|PostgresSaver|PostgreSQL
|RedisSaver|Redis

<br><br><br><br><br><br><br><br>













<div id="">
</div>
<br><br><br><br><br><br><br><br>

















<div id="">
</div>
<br><br><br><br><br><br><br><br>











<div id="">
</div>
<br><br><br><br><br><br><br><br>












<div id="">
</div>
<br><br><br><br><br><br><br><br>








<div id="">
</div>
<br><br><br><br><br><br><br><br>










<div id="">
</div>
<br><br><br><br><br><br><br><br>

