<a href="#template">模板语法</a><br>
<a href="#event">事件处理</a><br>
<a href="#load">渲染</a><br>
<a href="#input">表单双向输入绑定</a><br>
<a href="#listen">侦听器</a><br>


异步

```
await nextTick()  
```
等待DOM渲染全部完成



<br><br><br><br><br><br>


<div id="template">
<h2>模板语法</h2>

<h3><strong>ref</strong></h3>
传入基本数据类型，对象，数组

```
<div>{{ content }}</div>
-------------------------
let content = ref(100)
```
>[!WARNING] x 包装在 Ref对象里的 .value里。
>返回这个 Ref 对象
>
>```
>let a = ref( x )
>a 是对象 a.value 才是 x
>```

<h3><strong>reactive</strong></h3>
传入对象，数组

```
<p>age = {{ state.age }} </p>
-----------------------------
let a = reactive( {
    age  : 18,
    name : "jack"
} )
```
>[!NOTE] 一般用ref处理单个变量，reactive处理一组数据
>实际开发中建议全用ref


<h3><strong>动态HTML标签</strong></h3>

```
<div v-html="VarName"></div>
-----------------------------
let VarName = "<a href="...">hello world</a>"
```
这个 div 标签就相当于下面这个 a 标签
<br>
<h3><strong>动态属性</strong></h3>

```
<div :class="myClass" :id="myId"></div>
----------------------------------------
let myClass = ref("className")
let myId    = ref("idName")
```

<h3><strong>计算属性</strong></h3>
把 {{...}} 里的复杂逻辑用计算属性替换<br>
有缓存机制，多次调用情况下性能更好

```
<p>{{ bookNum }}</p>
--------------------------
const bookNum = computed(  ()=>{
    return author.books.length>0?'Yes':'No'
})
```
</div>

<br><br><br><br><br><br>

<div id="event">
<h2>事件处理</h2>
使用 @ 或 v-on 监听DOM事件<br>
在事件触发时执行对应的JavaScript语法
<br>
<h3><strong>内联处理</strong></h3>

```
<p> {{ count }} </p>
<button @click="count++"> Add </button>
```
直接执行后面的js语句"count++"

<h3><strong>方法处理</strong></h3>

```
<button @click="funcName"> Add </button>
```
执行函数

<h3>事件对象event</h3>
<a href="./JavaScript.md">跳转JavaScript</a>


<h3>参数传递</h3>

```
<p> {{ count }} </p>
<button @click="myfunc(count)"> Add </button>
------------------------------
function myfunc(event,data){
    console.log(data)
}
```

<h3>事件修饰符</h3>
和js里的event.preventDefault()等类似

```
.stop   阻止默认事件
.prevent 阻止事件冒泡
.self    点击元素本身触发，不冒泡
.capture    捕获阶段触发事件
.once   该事件最多被触发一次
.passive    优化滚动性能
```
e.g.

```
<a @click.once="DoThis"> Do </a>
```
</div>
<br><br><br><br><br>

<div id="load">
<h2>渲染</h2>

<h3>条件渲染</h3>

```
<p v-if="VarName==='Jack'">jack你好</p>
<p v-else-if="VarName==='Bob'">bob你好</p>
<p v-else>你好</p>
```

```
<p v-show="...">hello</p>
```
v-if是html是否生成这个标签<br>
v-show是html源码生成这个标签，但是不渲染（css display属性的切换）
<br><br>
<h3>列表渲染</h3>

```
<ul>
    <li v-for="item in list">                        
        <span>{{ item.name }}</span>                  
        <span>{{ item.age }}</span>                     
    </li>                                             
</ul>
-------------------------------------
const list = ref([
    {name : "Jack",age: 18},
    {name : "Bob",age: 19},
    {name : "Mary",age: 20},
])
```
>[!TIP] 也可以这样写拿到数组下标
>
>```
><li v-for="(item,index) in list">
>```

>[!IMPORTANT] 建议都使用key为元素添加唯一标识
>```
><ul>
>    <li v-for="item in list":key="item.id">                        
>        <span>{{ item.name }}</span>                  
>        <span>{{ item.age }}</span>                     
>    </li>                                             
></ul>
>-------------------------------------
>const list = ref([
>    {id : 1 , name : "Jack", age : 18},
>    {id : 2 , name : "Bob" , age : 19},
>    {id : 3 , name : "Mary", age : 20},
>])
>```
</div>
<br><br><br><br><br><br>


<div id="input">
<h3>表单双向输入绑定</h3>
v-model双向数据绑定

```
<p>{{ password }}</p>
<input v-model="password">
```
随着用户的输入，password会实时变化<br><br>
<strong>修饰符</strong>

```
.lazy 只有在触发change事件(失去焦点/回车)后，v-model才同步更新数据
.trim 去除用户输入两端的空格
```
</div>
<br><br><br><br><br><br>




<div id="listen">
<h3>侦听器watch</h3>
侦听一个响应数据，如果数据发生变化，则触发watch

```
<template>
    <div>
        <input v-model.lazy="question">
    </div>

</template>

<script>
    const question = ref('')
    const answer   = ref('你的回答')

    watch(question,(newVal,oldVal)=>{
        ......
    })

</script>
```










</div>
<br><br><br><br><br><br>

























