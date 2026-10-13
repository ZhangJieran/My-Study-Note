<a href="#VisibleGraph">图结构可视化</a>
<a href="#State">状态</a>



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








<div id="State">

## 状态

``` python
class MyState(BaseModel)
    pass

def node(state:MyState)->MySrate:
    pass
```


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

