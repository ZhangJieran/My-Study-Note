<a href="#SetEnvVar">设置环境变量</a><br>
<a href="#SetModel">创建模型</a><br>
<a href="#UseModel">BaseChatModel方法</a> : invoke() , stream()...<br>
<a href="#MessageObj">BaseMessage消息类</a><br>
<a href="#prompt">提示词模板</a><br>
<a href="#tools">工具调用</a><br>
<a href="#tools">langchain内置工具列表</a><br>
<a href="#output">结构化输出</a><br>
<br>
<a href="#Agent">Agent</a><br>
<a href="#middleware">中间件</a><br>
<a href="#memory">记忆</a><br>








<br><br><br>
<div id="SetEnvVar">
<h3>设置环境变量</h3>
加载环境变量

``` 
from dotenv import load_dotenv
load_dotenv("py风格的文件路径（用.）")
```
这个函数是用来读取项目里的.env文件，把里面的键值对加载到当前Python进程的环境变量os.environ。如果找不到文件返回False。


``` 
os.getenv("键")
```
该函数用于读取.os.environ里的变量
</div>
<br><br><br><br><br><br><br><br>
<div id="SetModel">
<h3>创建模型</h3>
============================架构示意图=========================================<br>

``` 
父类                  BaseChatModel              ---工厂函数--->  init_chat_model()
                           |                           
                           V
子类    ChatOpenAI  ChatDeepSeek  ChatOpenRouter ......    ---调用---> RunnableBinding
```
=============================================================================<br><br>
<strong>使用子类创建模型实例 ( 以ChatOpenAI为例 )</strong>

```
ChatOpenAI(
    model    = "deepseek-v4",             # 具体的模型
    base_url = "https://deepseek.com"     # 大模型供应商API请求地址
    api_key  = "apia密钥"                 # api key
)
```

ChatOpenAI() 可以兼容很多模型，比如deepseek也可以用ChatOpenAI创建<br>
ChatDeekSeek() 专用于创建deepseek模型<br>
ChatOpenRouter() 是为OpenRouter设计的，这是一个第三方模型代理的网站,里面集成了很多模型<br>
<br>
<strong>用工厂函数创建模型实例</strong>
<br>
init_chat_model()是统一的工厂函数,返回BaseChatModel

``` 
init_chat_model(
    model_provider  = "deepseek",                    # 模型供应商名称
    model           = "deepseek-v4",                 # 具体的模型
    base_url        = "https://api.deepseek.com"     # 大模型供应商API请求地址
    api_key         = "apia密钥"                     # api key

    temperature     = float                          # 一般是[0,1]，但这里是[0,2]的值，越小输出越固定
    max_tokens      = int                            # 限制模型最大输出token数量 
    timeout         = float                          # 超时时间(s) 超时未响应，请求取消
    max_retries     = int                            # 请求失败时，最大重试次数
    streaming       = bool                           # 是否开启流式输出
    reasoning       = bool                           # 是否启用推理模式
    
    configurable_fields = ("model","max_token","temperature"...)
    表示允许模型方法里的config参数里的configurable修改的参数

)->BaseChatModel:
```
更详细的参数列表 -> <a href="#MoreArgs">点击跳转</a><br>

>[!TIP] Ollama
>
>```
>ollama run qwen3.5:4b   终端本地部署模型  
>```
>调用ollama部署的模型
>
>```
>init_chat_mode ( 
>   model_provider = ollama
>   model          = "qwen3.5:4b"
>   base_url       = "https://localhost:11434"
>   api_key        不用传
>)
>```


</div>
<br><br><br><br><br><br><br><br>

<div id="MessageObj">
<h3>消息类</h3>

============================架构图======================================<br>

``` 
父类                             BaseMessage
                                      |
                                      V
子类  SystemMessage  HumanMessage  AIMessage  ToolMessage  MessagesPlacehoder

```
========================================================================<br>
<br>
----------------------------------------------------------<br>
消息类 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  对应字典格式      
----------------------------------------------------------<br>          
SystemMessage&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{"role" : "system",......}<br>
HumanMessage&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{"role" : "user",......}<br>
AIMessage&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{"role" : "assistant",......}<br>
ToolMessage&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{"role" : "tool"......}<br>
----------------------------------------------------------<br>
<br>
<strong>创建消息对象列表</strong><br>
可以使用消息类，也可以用字典格式，也可以混用

``` 
message = [
    {"role":"system","content":"你是一个ai助手"}，
    HumanMessage( content="你好，介绍一下你" ),
    ......
]
```
多轮对话添加记忆，一般往message里添加AIMessage。 AIMessage.content是模型输出的回答

<strong>HumanMessage</strong><br>

```
HumanMessage(
    content =  "你好",
    name    =  "Tom",
    id      =  "msg_1"
)
```
id全局唯一，name不唯一<br>
有些字段不同的模型厂商支持情况不一样,不支持时，返回的AIMessage里对应字段输出unknown<br>

<strong>AIMessage</strong><br>

```
AIMessage_ins.content       # AI的回答
AIMessage_ins.tool_calls    # list[ ToolCall ]
```

>[!NOTE] ToolCall 是字典 TypedDict
>```
>class ToolCall(TypedDict):
>   name : str
>   args : dict
>   id   : Option[str]
>```
<strong>ToolMessage</strong><br>

```
ToolMessage(
    content      = "<工具函数执行返回值>",
    name         = "getWeather",
    tool_call_id = "call_00_nUD2NCJQ4s"
)
```

<strong>content</strong><br>
content是发给模型的信息，可以直接是一个字符串，也可以是一个列表
<br><br>
e.g.给多模态模型发消息

```
msg = [HumanMessage(
    content = [
        {
            "type":"text",
            "text":"请解析图片内容"
        },
        { 
            "type":"image_url",
            "image_url": encode_image(...)
        }
    ]
)] 
```
<a href="./base64_image.py">encode_image() 见 base64_image.py </a>
<br>

<strong>content_blocks</strong><br>
不同厂商多模态调用/输出api不一样，为了统一，就有了content_blocks
<br>
输入：
```
msg = [HumanMessage(
    content_blocks = [
        {
            "type" : "text",
            "text" : "请解析图片内容"
        },
        { 
            "type"      : "image",
            "base64"    : encode_image(...),
            "mime_type" : "image/png"           #如果是其他类型的图片这里需要改成 "image/图片类型"
        }
    ]
)]
```
<a href="./base64_image.py">encode_image() 见 base64_image.py </a>
<br>
输出：

```
response = model.invoke(msg)
print(response.content_blocks)
```


</div>
<br><br><br><br><br><br><br><br>





<div id="UseModel">
<h3>BaseChatModel方法</h3>

``` 
invoke( input:list[BaseMessage] , config ,stop:list[str])    阻塞模式
ainvoke(...)   非阻塞模式
```
返回 AIMessage 实例<br>
input是消息列表 &emsp;遇到stop里的字符串就停止生成


``` 
stream(...)    阻塞式，流式输出
astream(...)   非阻塞式，流式输出
```
>[!TIP]<strong>流式输出打印示例</strong><br>
> 流式输出返回迭代器：
>
>``` 
>for chunk in model.stream("hello"):
>    print(chunk.text,flush=True,end="")
>```
>flush用于刷新缓存区域

```
batch(...)     阻塞式，批量处理多个输入的高并发场景
abatch(...)    非阻塞式
```
参数：list[ list[BaseMessage] ]<br>
返回 list [ tuple ( index , AIMessage ) ] &emsp;index表示这个回答对应原batch请求列表里的位置<br>
<br>
<strong>stop</strong><br>
模型输出匹配到stop里的字段就停止<br>
<strong>config</strong>

```
config={
    "run_name"  : "str"                         LangSmith中这次运行会显示为指定名称
    "tags"      : "list[str]"                   LangSmith筛选trace。给执行链路打上标签，区分不同的运行任务
    "callbacks" : "list[BaseCallbackHandler]"   设置回调处理器，在运行不同阶段触发，与LangSmith进行追踪调试
    metadata    : "Dict[str,Any]"               配置用户指定的信息，整个流程被包装为Runnable链时,可将这些参数传递给后续的链节点使用
    max_concurrency : int                       限制当前可运行对象的最大并发运行数(针对batch)
    recursion_limit : int                       运行时最大递归调用深度
    configurable    ：Dict[str,Any]             可配置的参数和init_chat_model一样，覆盖/添加模型参数   
}

```
configurable 里设置的参数须在 init_chat_model 的 configurable_fields 参数里有才会生效
</div>
<br>
<div id="MoreArgs">
<h3>更多参数</h3>
=================================== 模型推理参数 =========================================

```
top_p               = p ， p∈[0,1]              取累计概率大于p的词为候选词
n                   = num                       一次生成n条独立的候选答案
reasoning_effort    = low/medium/high           思考深度
presence_penalty    = num , num∈[-2.2]          存在奖惩：只要某个词出现过，就降低/升高这个词出现的概率
                                                (正数=惩罚重复，负数=鼓励重复)
store               = bool                      是否在模型供应商服务器保存本次对话
logit_bias          = {token_id:偏移分数,...}    人为修改某个token的生成概率
```
======================================================================================

```
model_kwargs
```
存放OpenAI Compatible API支持，但LangChain没有列出的字段

```
extra_body
```
存放模型厂商基于OpenAI API协议扩展的字段<br>
e.g. OpenAI没有Thinking字段，但DeepSeek有：

```
extra_body={ "thinking":{"type:"enable"} }
```
</div>




<br><br><br><br><br><br><br><br>



<div id="prompt">
<h3>提示词模板</h3>
<strong>from langchain.prompts import PromptTemplate</strong>

```
# 参数是 消息对象 , 字典 , 元组 ......都可以
template = ChatPromptTemplate([
                {"role":"system","content":"你是ai助手,你叫{name}"},
                {"role":"human","content":"你好"},
                {"role":"assitant","content":"我很好，谢谢"},
                {"role":"human","content":"{userinput}"}
])

# 1 返回ChatPromptValue
res = template.invoke( { 
        "name"      : "小智",
        "user_input": "hello" 
    } )

# 2 返回list[BaseMessage]
res = template.format_messages(name="小智",user_input="hello")

```
model.invoke(...) 参数兼容 ChatPromptValue<br>

>[!WARNING] 使用消息对象无法声明变量:
>
>```
>SystemMessage(content=f"你叫{name}")
>res = template.format_messages(name="小智")
>```
>name不会被赋值为小智

<br>
<h3>模板特化</h3><br>
<strong>特化，预填充变量</strong>

```
template = ChatPromptTemplate([
                {"role":"system","content":"你是ai助手,你叫{name}"},
                {"role":"human","content":"你好"},
                {"role":"assitant","content":"我很好，谢谢"},
                {"role":"human","content":"{userinput}"}
])

#特化，预填充变量
NewTemplate = template.partial(name = "Jack")
```
<strong>占位符placehoder</strong>

```
template = ChatPromptTemplate([
                {"role":"system","content":"你是ai助手,你叫{name}"},
                {"placeholder":"{conversation}"}
])

# placeholder 用来传入消息列表
res = template.invoke({
    "conversation":[
        {"role":"human","coontent":"How is everything going?"},
        {"role":"assistant","content":"great"},
        {"role":"human","coontent":"hi"}
    ]
})

```
placeholder 是一个消息列表 list[ BaseMessage ]




</div>
<br><br><br><br><br><br><br><br>


<div id="tools">
<h2>工具调用</h2>

<h3>定义BaseTool</h3>

<strong>函数本身的描述</strong>

```
@tool
def MyFunc(arg1,arg2...):
    """
    描述，必须有
    """
    pass
```
或者

```
@tool(description="描述")
def MyFunc(arg1,arg2...):
    pass
```
<br>

<strong>函数参数的描述</strong><br>
args_schema:

```
class WeatherInput(BaseModel):
    city : str = Field (
        description = "具体的城市"
        default     = "北京"
    )

    # unit 是 typing.Literal 类型,该参数的值只能从列表中选
    unit: Literal["celsius", "fahrenheit"] = Field(
        description = "温度单位，支持摄氏度/华氏度",
        default     = "celsius" 
    )

@tool(args_schema=WeatherInput)
def GetWeather( city:str,unit:Literal["celsius", "fahrenheit"] ):
    pass
```






<br>
<h3>调用BaseTool</h3>

```
MyFunc.invoke( ToolCall实例 )
```
返回ToolMessage


>[!NOTE] ToolMessage 的 content 属性
>函数的返回值在这里

>
>[!NOTE] ToolCall 是字典
>```
>class ToolCall(TypedDict):
>   name : str
>   args : dict
>   id   : Option[str]
>```

绑定工具

```
BindedModel = model.bind_tools( list[ BaseTool|func ] , tool_choice=auto )
```
tool_choice = none(不调用工具) | auto(自行决定) | any(必须调用工具) | tool名(强制调用指定工具)

</div>


<br><br><br><br><br><br><br><br>


<div id="output">
<h2>结构化输出</h2>



<h3>Pydantic</h3>

```
class MyEnum(int,Enum):
    n1 = 1
    n2 = 2

class Person(BaseModel):
    name : str       = Field(description="姓名",default = "Jack") #设置默认值
    age  : int       = Field(description="年龄")
    occupation : str = Field(description="职业")
    
    # 限定选择范围,可以用Literal/枚举类型
    status : Literal[0,1] = Field(description="...")
    status : MyEnum = Field(description="...")

# 可以采用这种嵌套的结构
class PersonList(BaseModel):
    person : list[Person]
```

<strong>更多Field字段</strong><br>

```
Field(
    description 描述
    min_length  最小长度
    max_length  最大长度
    el = 小于等于xxx
    ...
)
```

>[!NOTE] 尽量少嵌套
>模型能力有限，一般最多嵌套三层

<br>
<br>
<h3>Model结构化输出</h3>
<strong>with_structured_output()</strong>

```
model2 = model.with_structured_output(PersonList)
model2.invoke(...)  返回 PersonList 实例
```




<strong>开启include_raw 拿到AIMessage</strong>

```
with_structured_output( CLASS,include_raw=True,method="provider" )
```
返回字典 ： "raw" : AIMessage , "parsed" : CLASS<br> 
method="provider"开启模型原生约束解码能力



<br>



<h3>Agent结构化输出</h3>

```
class MyClass(BaseModel):
    # 使用Pydantic定义结构化输出
    ...

agent = create_agent(
    ...
    response_format = ProviderStrategy( schema=MyClass ) 
                     /ToolStrategy( schema=MyClass )   
)
```
>[!TIP]优先使用ProviderStrategy，如果有些模型不支持，再用ToolStrategy
>ProviderStrategy 模型原生结构化输出能力，约束解码<br>
>ToolStrategy 伪装成虚拟工具，本质不是用模型的结构化输出能力


>[!WARNING] Agent和Model结构化输出的区别
>with_strutured_output 每次都是结构化输出<br>
>response_format 只在Agent循环最后一次结构化输出，中间推理不受影响



</div>
<br><br><br><br><br><br><br><br>

<div id="Agent">
<h2>Agent</h2>




```
agent = create_agent(
    model  = mymodel,
    name   = "agent01",
    tools  = [tools,tool2...]
    system_prompt   = "...",
    middleware      = list[AgentMiddleware]
)

```

```
agent.invoke({
    "messages":[BaseMessage]
})
```
返回字典 { "messages" : [BaseMessage], "Structured_response" : 结构化输出实例    }<br><br>

<h3>错误处理</h3>

```
agent = create_agent(
    ...
    handle_errors = True  
)
```
默认行为,出现错误会自动重试

```
1. handle_errors = False  # 不会重试，遇到错误直接报错
2. handle_errors = "str"  # 遇到错误，ToolMessage.content = "str" 给大模型
3. handle_errors = (错误类型,错误类型2...)
4. handle_errors = callable
```

4举例 : 

```
def DealError(error:Exception)->str:
    return xxx       # 返回值行为：ToolMessage.content = 返回值

agent = create_agent(
    ...
    handle_errors = DealError
)
```


<h3>stream输出</h3>

```
agent.stream( input =  { ... },
    stream_mode = values         # 每一步都输出完整AIMessage,是整个list[BaseMessage]
                / updates( 默认) # 只展示每次更新的消息，只是一个AIMessage
                / messages       # 返回流式输出消息对象本身，遍历打印chunk[0].content
                / custom         # 用于输出进度信息
                / checkpoints                    
                / tasks          # 会输出当前任务的开始结束时间，任务结果错误信息
                / debug          # 和tasks类似,多了任务步骤,task类型，时间戳等
)
```


</div>
<br><br><br><br><br><br><br><br>

<div>
<h2 id="middleware">中间件</h2>

```
agent = create_agent(
    ...
    middleware = list[AgentMiddleware]
)
```

写在前面的before钩子先执行，写在前面的after钩子后执行
<br>
<h3>自定义中间件</h3><br>
根据执行时机区分

自定义钩子的两种写法



```
class MyMiddleware(AgentMiddleware):

    def before_agent(self,state:AgentState,runtime:Runtime):
        # AgentState 是当前会话状态对象
        # 基本上用state["messages"] 最多。包含所有消息list[BaseMessage]
        # runtime 暂时先pass
        
    def before_model(...):
        pass

    def after_model(...):
        pass
    def after_agent(...):
        pass


    # 发起LLM请求前
    def wrap_model_call(request,handler):
        # 只有调用这个，才会真正请求给模型发送请求
        # request 是请求信息
        # 可以用来短路调用模型，修改请求信息，修改返回信息等
        
        res = handler(request)     # 这一步发送请求，返回模型响应信息
        return res                 # 返回值加入到state["messages"]里


    # 调用工具前
    def wrap_tool_call(request,handler):
        #和wrap_model_call类型
```
agent 是每次调用agent前后执行，可以理解成整个invoke<br>
model 是每次调用LLM模型请求前后执行，一个invoke里可能执行好几次model


```
@def before_agent    
@def before_model
@def wrap_tool_call
@def wrap_model_call
@def after_model
@def after_agent

======== e.g. =========
@before_agent
def MyMiddleware(state,runtime):
    pass    
```
>[!CAUTION] AgentState
>state参数是一个thread_id全局共用的，如果只想在局部修改需要拷贝一下

>[!TIP] 装饰器参数can_jump_to = ["end","tools","model"]
>直接跳转到某个流程节点<br>
>end 跳转到第一个after_agent钩子<br>
>tools 跳转至工具节点<br>
>model 跳转至模型节点或第一个before_model钩子<br>
>
>```
>@before_agent(can_jump_to=["end"])
>def MiddlewareFunc():
>   ...
>   if ... :
>       retunrn {
>           "messages" : [                 
>                AIMessage("...")
>            ],
>           "message_override" = False,          # 追加到消息列表，True是替换
>           "jump_to":"end"    
>}
>```


<br>


<h3>内置中间件</h3><br>

<strong>SummarizationMiddleware</strong><br>
上下文压缩中间件<br>
到达触发条件时，把上下文压缩为HumanMessage放到消息列表最开始的位置

```
SummarizationMiddleware(
    model   = ... ,
    trigger = [
        ("tokens",100),  # 历史token数量达到某值触发
        ("messages",6),  # 历史消息条数达到某值触发
        (fraction,0.1)   # 历史token达到 (模型最大输入token*fraction) 触发
    ],
    keep =  ("tokens",1500)  
    summary_prompt = "历史信息摘要如下{messages}" # 可以自定义提示词，但{messages}不能动
)
```

```
keep字段 : 
    tokens   压缩时最近保留原始信息的token数
    messages 保流最近原始消息条数
    fraction 保留最近原始消息占模型上下文窗口的比例
    # 只能三选一
```
<br>
<strong>HumanInTheLoopMiddleware</strong><br>
人工审核中间件<br>
调用工具前拦截


```
HumanInTheLoopMiddleware(
    interrupt_on = {
        "get_weather" : True,       # 调用 get_weather 工具时拦截
        "read_email"  : False,      # 调用 read_email 时不拦截
        "send_email"  : {           # 人工选择的选项
            "allowed_decisions" : ["approve","reject","edit"],
            "desctiption"       : "该工具拦截时的描述信息"
        },
        description_prefix = "通用的拦截时的描述信息"
    }
)
```

>[!CAUTION] 确保位于同一会话
>config = {"configuarable":{"thgread_id"}:"1"}

<br>
<strong>PIIMiddleware</strong><br>
隐私保护

```
PIIMiddleware(
    pii_type = email credit_card url mac_address ip  信息种类
    strategy = redact mask hash block                保护隐私信息的方法
    detector = dict[str,Detector]                    检查敏感信息的函数(有默认的)
    apply_to_input  = bool 是否在调用模型前检查
    apply_to_output = bool 是否在调用模型后检查
    apply_to_result = bool 是否在调用工具后检查
)
```
<br>
<strong>ToDoListIMiddleware</strong><br>
通过调用 write_todos(内置) 工具实现<br>
把模型生成的规划加入上下文，防止模型忘记

```
agent = create_agent(
    ...
    middleware = list[ToDoListMiddleware()]
)
```

<br>
<strong>ModelCallLimitMiddleware</strong>
限制模型输出次数

```
ModelCallLimitMiddleware( 
    tool_name      = "限制的工具名称" | None    # None是全局限制
    thread_limit   = 2,
    run_limit      = 3,
    exit_behavior  = "end" 
)
```

```
thread_limit  同一个id会话，最多允许调用次数
run_limit     一次invoke,最多调用次数
exit_behavior 达到限制后的行为 end是直接结束 error是抛异常
```
<br>
<strong>ToolCallLimitMiddleware</strong><br>
限制工具调用次数

```
ToolCallLimitMiddleware( 
    thread_limit   = 2,
    run_limit      = 3,
    exit_behavior  = "end" 
)

thread_limit  同一个id会话，最多允许调用次数
run_limit     一次invoke,最多调用次数
exit_behavior 达到限制后的行为 end直接结束 error抛异常 continue继续调用模型
```

<br>
<strong>ModelFallbackMiddleware</strong><br>
主模型出现问题无法访问时，启用备用模型

```
ModelFallbackMiddleware(
    BaseChatModel_1,
    BaseChatModel_2,
    ...
)

```

<br>
<strong>LLMToolSelectorMiddleware</strong><br>
工具太多时，用子模型筛选工具

```
LLMToolSelectorMiddleware(
    model          = 子模型,
    max_tools      = int,            # 最多选择的工具数量
    always_include = [ToolName,...]  # 总是选择某些工具，这些工具不算入max_tools
)
```

<br>
<strong>ToolRetryMiddleware</strong><br>
工具调用失败采用指数退避策略重试<br>
每次失败后都等待一段时间重试，每次等待时间呈指数增长

```
ToolRetryMiddleware(
    max_retries    = int,     最大重试次数
    backoff_factor = float,   每次重试失败等待时间乘float
    initial_delay  = float,   第一次重试前的初始等待时间
    max_delay  =  float,      最大等待延迟上限
    jitter     =  bool,       是否开启抖动,等待时长加入随机的微笑扰动
    on_failure =  "continue"  达到最大重试次数任然失败,continue表示把错误信息给agent让agent自己决策
    retry_on   =  (TimeoutError,...),  捕获指定的异常时才重试
)
```
<br>
<strong>ToolRetryMiddleware</strong><br>
模式调用失败时采用指数退避策略重试

```
ModelRetryMiddleware(
    max_retries    = int,     最大重试次数
    backoff_factor = float,   每次重试失败等待时间乘float
    initial_delay  = float,   第一次重试前的初始等待时间
    max_delay  =  float,      最大等待延迟上限
    jitter     =  bool,       是否开启抖动,等待时长加入随机的微笑扰动
    on_failure =  "continue"  达到最大重试次数任然失败,continue表示把错误信息给agent让agent自己决策
    retry_on   =  (TimeoutError,...),  捕获指定的异常时才重试
)
```
<br>
<strong>LLMToolEmulator</strong><br>
工具尚未开发完成,先测试工具调用

```
LLMToolEmulator(model = ...)  # 使用该模型模拟工具执行
```


<br>
<strong>ContextEditingMiddleware</strong><br>
工具上下文编辑中间件,只清理工具消息

```
ContextEditingMiddleware(
    edits = [
        ClearToolUseEdit(
            trigger = int,    触发token数量
            keep = 0          触发清理时，保留最近几次工具调用信息
        )
    ]
    checkpointer = InMemorySaver()
)
```
<br>
<strong>FilesystemFileSearchMiddleware</strong><br>

基于系统的Glob和Grep检索工具，为Agent赋予本地文件搜索和分析的能力<br>
自动往tools 里添加glob和grep工具

```
FilesystemFileSearchMiddleware(
    root_path = "路径",
    allowed_extentions = [".py",".js"...] 允许检索的文件后缀
    use_ripgrep = True,        设置为True可获得比Grep更快的性能，前提是系统已安装ripgrep
    max_file_size_mb = 10      单个文件最大读取限制(单位：MB) 防止读取超大日志或二进制文件
)

```
<br>
<strong>Shell tool</strong><br>
为Agent提供可以执行命令的shell环境
<br>
<strong>Filesystem</strong><br>
用于查看目录，读取文件，写文件，改文件中间件
来自deepagents框架
<br>
<strong>Subagent</strong><br>
便捷地创建子agent中间件
来自deepagents框架
</div>
<br><br><br><br><br><br><br><br>


<div id="memory">
<h2>记忆</h2>
<h3>短期记忆</h3>
State 历史消息列表
Chekpointer 某个时刻state快照
Thread ID State的唯一标识<br><br>
<strong>基于内存存储的记忆</strong>

```
checkpointer = InMemorySaver()  创建一个内存级别的记忆存储

config = {
    "configurable":{
        "thread_id" : "1"
    }
}

agent = create_agent(
        ...
        checkpointer = checkpointer
    )

agent.invoke({
    "messages":[...],
    config = config       
})
```

```
agent.get_state(config)  获得这个state的信息
```
<strong>基于PostgresSQL存储的记忆</strong>

```
from langgraph.checkpoint.postgres import PostgresSaver

DB_URL = "postgresql://用户名:密码@IP地址:5432/数据库名?sslmode=disable"

with PostgresSaver.from_conn_string(DB_URL) as checkpointer:
    #初始化数据库
    checkpointer.setup()

    agent = create_agent(
        ...
        checkpointer = checkpointer
    )

    ...
```

>[!TIP] agent被限制在with块内。解决办法：
>不是工程标准办法，只是个人的经验补丁
>
>```
># 外部定义变量，利用yield特性防止代码跳出with块
>agent = None
>
>def func():
>   global agent # 声明agent
>   
>with PostgresSaver.from_conn_string(DB_URL) as checkpointer:
>       checkpointer.setup()
>
>       agent = create_agent(
>           ...
>            checkpointer = checkpointer
>       )
>       yield    # 使函数卡在这里，避免离开with块
>
># 加载函数  
>g = func()
>next(g) 
>```



>[!IMPORTANT] 基于数据库和内存存储记忆的区别
>基于内存: 程序进程结束，记忆就消失了，下一次运行不会记得上一次的运行时的记忆<br>
>基于数据库: 记忆不会随程序进程结束而消失



<br>
<h3>长期记忆</h3>

创建embeding模型

```
embedding_model = init_embeddings( model , api_key , base_url )
```


```
IndexConfig = {
    "embed":func,              # 自定义embed函数,或者传embeding模型
    "dims":6,                  # 向量维度
    "fields":["$","key"]       # 把value里的哪个key做向量化？$表示整个value
}
```

<strong>基于内存存储的记忆</strong>

```
#这里填 IndexConfig
store = InMemoryStore(index:IndexConfig = None)   

store.put(
    namespace : tuple,
    key       : str,
    value     : dict[str,any],
    index     : bool           # index=True 生成向量，开启语义化检索
) 

store.get(namespace,key)  返回Item对象
store.search(
    namespace_prefix:tuple,   # namespace路径
    filter:dict[str:any]|None # 过滤条件,返回带filter的Item
    query:str|None,           # 基于语义查询
    limit:int,                # 最多取limit条数据
    offset:int,               # 取之前跳过offset条数据
)

store.delete(namespace,key)
```
<br>
<br>
<strong>基于PostgresSQL存储的记忆</strong><nr>

```
from langgraph.checkpoint.postgres import PostgresStore

DB_URL = "postgresql://用户名:密码@IP地址:5432/数据库名?sslmode=disable"

with PostgresStore.from_conn_string(DB_URL , index:IndexConfig) as store:
    #初始化数据库
    store.setup()
    store.put(...)

    ...
```

>[!CAUTION] 在创建store时写了IndexConfig
>调用store.put()<br>
>put 的 index字段默认值为True


</div><br>
<br><br><br><br><br><br><br><br>







































































