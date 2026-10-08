<a href="#template">模板语法</a><br>
<a href="#event">事件处理</a><br>
<a href="#load">渲染</a><br>
<a href="#input">表单双向输入绑定</a><br>
<a href="#listen">侦听器</a><br>
<a href="#GetDOM">获得DOM元素</a><br>
<a href="#DOMHook">DOM钩子</a><br>
<a href="#props">Props & emit 组件通信</a><br>
<a href="#slot">slot</a><br>
<a href="#async">异步</a><br>



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
<button @click="myfunc(arg1,arg2...)"> Add </button>
------------------------------
function myfunc($event,arg1,arg2...){
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

<div id="GetDOM">
<h2>获得DOM元素</h2>

需要目标DOM元素有ref属性

```
<TagName ref="RefName">...</TagName>
```

使用useTemplate获得Element
```
import {useTemplateRef,onMounted} from 'vue'

const a = useTemplateRef('RefName') 
```
</div>

<br><br><br><br><br><br>
<div id="DOMHook">
<h2>DOM钩子</h2>

- beforeCreate &emsp;组件创建前
- created&emsp;组件创建后
- beforeMount&emsp;DOM被渲染之前
- Mounted&emsp;DOM渲染完成后

组件被挂载了

- beforeUpdated &emsp;数据发生变化前
- updated&emsp;数据发生变化后

组件被取消挂载

- beforeUnmounted
- unmounted

```
onMounted(()=>{
    ...
})
```

>[!WARNING] Vue3的setup模式中，没有beforeCreate created
>如果需要，需退回到Vue2的写法：setup()函数

</div>
<br><br><br><br><br><br>

<div id=props>
<h2>Props & emit 组件通信</h2>
<h3>父组件传子组件</h3>
<strong>父组件传子组件</strong>

- `<ChildComp :keyName="val" />`
把val传给ChildComp组件，用keyName作为键

<strong>子组件接收</strong>

- ` const props = defineProps(['keyName'])`
  props.key就是val

- `defineProps(['keyName'])`
 keyName直接当值为val的变量用




<h3>子组件传父组件</h3>

```
# 子组件内
const emit = defineEmits(["自定义事件名称"])  # 声明emit可以往外冒哪些自定义事件
function functionName(){
    emit("自定义事件名称",传给父组件的参数)
}

# 父组件内
<ChildComp @自定义事件名称="functionName" />
function functionName(参数){
    ...
}


emit负责往外冒泡，父组件的<ChildComp @自定义事件名称="functionName" />会监听emit
当子组件的emit被触发时,父组件根据emit里的"自定义事件名称"参数判断，触发functionName函数
```


<h3>兄弟组件互传</h3>
通过父组件作为桥梁

- 父组件中

```
const fatherVar
provide("key",fatherVar)    先注入
```

- 两个兄弟组件中

&emsp;&emsp;&emsp;通过key拿到 `const receive = inject("key")` 

如此两个兄弟组件内都拿到了同一个变量

>[!WARNING] 父子通信
>通过Props实现：父子必须是紧邻关系<br>
>通过provide,inject则无限制，只要是后代都行
</div>
<br><br><br><br><br><br>


<div id="slot">
<h2>slot</h2>

定义插槽组件SlotComp
```
<div>
    <slot name='s1'> </slot> 
</div>
```

使用插槽

```
<SlotComp>
    <template #s1>
        插入的内容
    </template>
</SlotComp>
```

</div>
<br><br><br><br><br><br>


<div id="async">
<h2>异步</h2>

惰性加载组件

```
const AsyncComp = defineAsyncComponent({
    loader:()=> import('组件路径'),  异步加载的组件
    delay: 100                      加载组件前的延时时间(ms)
    loadinfComonent:组件名,          加载中时展示的组件
    errorComponent:组件名,           加载失败时展示的组件
})
```
AsyncComp是组件 `<AsyncComp />`使用

- 如果需求没那么严格可以直接 `defineAsyncComponent(()=>import('组件路径'))`



</div>

<br><br><br><br><br><br>










