<a href="#StringMethod">字符串方法</a><br>
<a href="#ArrayMethod">数组方法</a><br>
<a href="#obj">对象object</a><br>
<a href="#Math">Math对象</a><br>
<a href="#Date">Date对象</a><br>
<br>
<br>
<a href="#DOM">DOM架构介绍</a><br>
<a href="#document">document对象</a><br>
<a href="#Element">Element对象</a><br>
<br>
<br>
<a href="#css">CSS操作</a>
<br>
<br>
<a href="#event">事件</a><br>
<a href="#Mouse">鼠标事件</a><br>
<a href="#EventObj">事件对象</a><br>
<a href="#keyboard">键盘事件</a><br>
<a href="#formEvent">表单事件</a><br>



<br>
<div>

```
alert("弹出框文字")
```
生成弹出框

```
document.write("输出到浏览器页面")
```
</div>
<br>

<div id="STringMethod">
<h3>字符串方法属性</h3>

```
str.charAt( index )               
```
 取下标为index的字符,当index不合法时返回空字符串""

 ```
str.concat( Other1,Other2... )    
```
字符串拼接 str+Other1+Other2...<br> 
返回新字符串，不改变str,如果other不是字符串，会强制转换成字符串

```
或者直接使用+： str + Other + Other
```

```
str.substring( start,end )        
```
取子串，end不写默到结尾。<br>
如果参数为负数，把负数变成0;如果start>end交换参数位置

```
str.substr( start,length )         
```
取子串

```
str.indexOf( Other,n )             
```
从n开始查找，返回Other在str里第一次出现的下标，找不到返回-1

```
str.trim()                         
```
返回去除两端 空格 \n \t \v \r 的字符串

```
trimEnd() trimStart()          
```
只去除一端

```
str.split(str,len)                     
```
按给定的 str 分割字符串,返回分割的数组,split参数可以是空字符串""。len为可选，返回的限制数组里最多有len个元素
<br>
e.g. 
```
var str = "hello|world|hi";
str.split('|');
```
 -> 返回['hello','world','hi']
</div>
<br>


<div id="ArrayMethod">
<h3>数组方法</h3>

```
arr.isArray()
```
判断是否是数组，返回bool（用typeof判断数组返回的是object）

```
arr.push( elem1,elem2... ) 
arr.pop() 
```
在数组末端添加元素，返回数组长度<br>
删除尾部元素，并返回被删除的元素

```
arr.unshift( elem1,elem2... )
arr.shift()
```
数组头部添加元素<br>
删除头部元素

```
arr.join( str )
```
把数组里的所有元素用str连接，返回字符串<br>

```
arr.concat( arr1,arr2... )
```
合并数组返回新数组，原数组保持不变

```
arr.reverse()
```
数组翻转(会改变原数组)

```
arr.indexOf( val，index )
```
从下标index搜索(默认从0开始)，返回给定元素第一次出现的下标,不存在返回-1
</div>
<br>
<div id="obj">
<h3>对象object</h3>

```
var user = {
    name     :  "JieRan",
    arr      :  ["hello","world"],
    
    getName  :  function(){
        ......
    },
    otherObj :  {
        ......
    }
    ......
}
```
可以用user.getName()调用这个函数
</div>
<br>

<div id="Math">
<h3>Math对象</h3>
<strong>方法：</strong>

```
random()                    生成 [0,1) 的随机数
abs()                       取绝对值
max/min( v1,v2,v3...... )   取最大/最小
floor()                     向下取整
ceil()                      向上取整
```

</div>
<br>


<div id="Date">
<h3>Date对象</h3>

```
Date.now()

...略过这部分
```
返回时间戳

</div>
<br>
<br>

<div id="DOM">
<h3>DOM架构介绍</h3>

```
                    Node节点
                        |
                        V
------------------------------------------------------------
Document       Element      Text        Comment  ......
------------------------------------------------------------

Document  整个HTML文件
Element   相当于标签   e.g. <div> <p> <h1>......
Text      纯文本       e.g. Hello World
Comment   注释节点     <!-- xx -->

HTML_Collection 是一个元素为Element的列表
NodeList        是元素为Node的列表
```
浏览器会自动实例化Document得到document


</div>
<br>
<br>
<br>

<div id="document">
<h3>document对象</h3>

<strong>获取元素</strong>
```
document.getElementsByTagName( "标签名称" )
document.getElementsByClassName( "class名称" )
document.getElementsByName( "标签name属性" )
```
返回一个类似数组对象的实例（HTML_Collection实例）<br>

```
document.getElementById( "标签Id属性" )
```
getElementById(没有s)返回Element对象<br>

```
document.querySelector( "css选择器" )         
document.querySelectorAll( "css选择器" )
```
querSelector只会返回匹配的第一个&emsp;querySelectorAll返回全部<br>
<br>
<strong>创建元素</strong>

```
document.createElement( "标签名" )
```
创建一个标签,Element

```
document.createTextNode("请输入文本")
```
创建一个文本，返回Text

```
DOM节点1.appendChild( DOM节点2 )
```
将节点1挂载到节点2下
<br>
<br>
```
document.createAtttribute( "属性名" )
属性名.value = ...
```
创建一个属性,返回Attr对象

```
Element.setAttributeNode( Attr对象 )
```
将属性添加到Element里

</div>
<br>

<div id="Element">
<h3>Element对象</h3>

```
Element.id

Element.className
Element.classList.add( "class" )        添加class
Element.classList.remove( "class" )     移除class
Element.classList.contains( "class" )   判断有没有某个class
Element.classList.toggle( "class" )     如果有就移除，没有就添加
```
<br>

```
Element.innerText
Element.innerHTML
```
innerText 是纯文本<br>
innerHTML 能识别html语法<br>
e.g.

```
Element.innerText = "<a href="https://...">hello</a>"
Element.innerHTML = "<a href="https://...">hello</a>"
前者网页显示    <a href="https://...">hello</a>
后者网页显示    hello 并且点击可以跳转
```
<br>


```
Element.querySelector( "css选择器" )         
Element.querySelectorAll( "css选择器" )
```
只会在Element的后代中找<br>

```
Element.value 
```
表单方框里输入的内容
<br>
<strong>获取元素位置</strong>

```
clientHeight        获取元素高度/宽度content+padding
clientWidth    

offsetWidth         获取元素高度/宽度content+padding+border
offsetHeight
```
<br><br>
```
offsetTop
offsetLeft
```
到父级元素上/左边界的间距


```
document.documentElement.scrollTop
document.documentElement.scrollTop
```
获得页面滚动的距离



</div>
<br>
<div id="css">
<h3>CSS操作</h3>
三种方法

```
element.setAttribute(
    "style",
    "background-color:red;"+
    "border:1px;"+
    ......
    )
```

```
Element.style.width = "200px";
Element.backgroundColor = "red";
......

```

```
Element.style.cssText = "width:100px;"+
                        "height:200px"+
                        ......
```

</div>
<br>
<div id="event">
<h3>事件</h3>
HTML事件<br>
缺点：HTML和JS代码混在一起

```
<button onclick="clickHandle()">按钮</button>
<script>
    function clickHandle(){
        console.log("点击了按钮");
        ......
    }
</script>
```

DOM0级事件<br>
缺点：只能添加一个事件
```
<button id="btn">按钮</button>
<script>
    var btn = document.getElementById("btn");
    btn.onclick = function(){
        consile.log("点击了按钮1");
        ......
    }

    btn.onclick = function(){
        consile.log("点击了按钮2");
        ......
    }   
    //会把上面的覆盖

</script>
```

DOM2级事件

```
<button id="btn">按钮</button>
<script>
    var btn = document.getElementById("btn");
    btn.addEventListener("click",function(){
        console.log("点击了按钮");
        ......
    })
</script>
```

</div><br>


<div id="Mouse">
<h3>鼠标事件</h3>

```
click           单击              
dbclick         双击            
mousedown       按下鼠标      
mouseup         释放鼠标      
mousemove       鼠标在节点内部移动 

mouseenter      鼠标进入一个节点触发 
mouseleave      鼠标离开某个节点触发 

mouseover       进入节点及其子节点触发      
mouseout        离开节点及其父节点触发       

wheel           鼠标滚轮触发               
```

示例
```
Element.onclick = function(){
    ......
}
```


</div><br>




<div id="EventObj">
<h3>事件对象</h3>

```
Elemnt.onclick() = function($event,data1,data2...){
                        ...
                    }
```
event参数就是事件对象<br>
data是传递的参数
<br><br>
<strong>属性</strong><br>

```
event.target     触发此次事件的Element
even.type        事件名称
event.keyCode    和键盘事件有关，代表每个按键的唯一标识
```

<strong>方法</strong>

```
event.preventDefault()     阻止标签的默认事件
event.stopPropagation()    阻止事件冒泡（触发定义在别的节点上的监听器）
```

</div><br>

<div id="keyboard">
<h3>键盘事件</h3>

```
keydown   按下触发
keyup     松开触发
keypress  无值键不触发，有值键先触发onkeydown再触发onkeypress
```
</div><br>




<div id="formEvent">
<h3>表单事件</h3>

```
input     表单内输入内容时触发(连续触发)
change    表单内输入内容触发(非连续触发)只有按下回车或失去焦点才触发

reset       清空表单
submit    向服务器提交数据

select    选中输入框里的内容时触发
```


</div><br>
