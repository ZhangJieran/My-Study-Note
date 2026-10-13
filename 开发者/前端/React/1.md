<a href="#communicate">组件通信</a><br>
<a href="#xuanran">组件渲染</a><br>
<a href="#LocalCSS">局部CSS文件</a><br>
<a href="#event">事件处理</a><br>


<a href="#Hooks">Hooks</a><br>


<br><br><br><br><br><br><br><br>













<div>
React 组件要以大写字母开头

```js
React.createElement('标签名',{属性:值},子元素)
没有属性填null

React.createElement('div'，{className:'box'},hello)
相当于 <div class="box"> hello </div>
```
</div>
<br><br><br><br><br><br><br><br>















<div id="communicate">
<h2>组件通信</h2>

```js
// 非字符串的要用花括号包起来
<Welcome name="jack" age={18} />

export function Welcome(props){
    console.log(props.name)
    console.log(props.age)
}
```
<br>
<strong>利用JavaScript的解构语法,可以设置默认值</strong>

```js
export function Welcome({name="peter",age=0}){
    console.log(props.name)
    console.log(props.age)
}
```
>[!CAUTION] 传入null不会触发默认值
>默认值仅在不传或传入undefined时被使用，

<br>
<strong>也可以直接传组件</strong>

```js
<father> 
    <child></child>
</father>

export function father(props){
    // <child></child>会自动传给props的children属性
    return (
        <div>
            {props.children}
        </div>
    );
}
```
<br>
<br>

### createContext &&  useContext


```js
const Box = createContext()

function father(){
    Father_Data = 1;
    return(
        <Box.Provider value={Father_Data}>
        // 在这里声明子标签
            <son />
        </Box.Provider>
    );
}

function son(){
    const data = useContext(Box)
    ...
}
```
不会渲染<DataBox.Provider>标签,但它包裹的内容会渲染
</div>
<br><br><br><br><br><br><br><br>
























<div id="xuanran">
<h2>组件渲染</h2>
<h3>短路渲染</h3>

`{A && B}` A为假返回A,A为真返回B

```
{变量 && <p>hello</p>}  如果变量是false,undefined,null就不会渲染<p>hello</p>
```

>[!CAUTION] 
>
> ```
>(a.length&&<p>hello</p>)
>当a.length==0时不会渲染<p>
>因为返回0，而react只有在返回null,false,undefined
>才不会渲染，事实上，这种情况会渲染0
>```

<br>

### 列表渲染

```js
export function ProductsList() {  
    Products = [ 
        {
            id:1,
            price:10
        },
        {
            id:2,
            price:20
        }
    ];

     //利用map,遍历Products把里面的每个元素赋值给elem,index是数组下标
    const output_products = products.map( (elem,index)=> {             
                    return (
                        //react要求使用map时返回的标签必须带有key,且每个的key在列表中唯一
                        <div key={elem.id}> 
                            <p>{elem.id},{elem.price}</p>
                        </div>
                    );
                })

    return (
        <React.Fragment>
            <h2>this is Products</h2>
            {output_products}
        </React.Fragment>
    );
}
```
>[!WARNING] 开发时不建议用数组下标作为key

</div>
<br><br><br><br><br><br><br><br>


























<a id="LocalCSS"></a>

## 局部CSS文件

`.CSS`默认是全局的，这会造成命名冲突等一系列问题

`.module.css` 为逻辑上的局部文件，原理是导入该文件的时候会对里面所有样式重命名，避免冲突

<br>

`import styles from "..../文件名.module.css"`
>[!WARNING]此时类名已经改变，不知道是什么名字，需要用styles查询
>styles通过改写类名的方式避免冲突
<br>

假设该文件里定义了red,blue样式

```js
//styles实际上是一个对象
styles = {
    red:"自动生成的唯一类名",
    blue:"自动生成的唯一类名"
}
```


```js
//通过模板字符串语法，拿到对应的类名字符串
<div className={`${style.样式}`}>
```
<br><br><br><br><br><br><br><br>






























<a id="event"></a>

## 事件处理

react事件处理采用on+小驼峰命名法，如click事件是onClick

```js
// 触发时自动给handleClick注入一个事件对象参数
const handleClick = (e)=>{
    alert("Hello World!");
};

export const CustomButton = ()=>{
    return <button onClick={handleClick}>点击打招呼</button>;
};
```
传入自定义参数

```js

const handleClick = (e, data)=>{
    alert("Hello World!");
};

export const CustomButton = ()=>{
    // 如果你要传入自定义data参数，需要用箭头函数包裹绑定
    return <button onClick={(e) => handleClick(e, "自定义传入的数据")}>点击打招呼</button>;
};

```

<a href="..\JavaScript.md">更多事件见JavaScript.md</a>
<br><br><br><br><br><br><br><br>

















<div id="Hooks"></div>

## Hooks


<details>
<summary><strong>useState</strong></summary>

---

`const [Var,setVar] = useState(0)`  Var是定义的变量，初始值为0，setVar是设置状态的函数


e.g.
`setVar(Var+1)` 使Var增加1


>[!IMPORTANT] useState 只能在对应组件函数内部定义，且位于函数顶层

<br>

### 惰性初始化

`useState(function)` 传函数,只会在初始渲染时调用这个函数,每次重新渲染不调用

<br><br>

>[!WARNING] <strong>状态不会在事件函数内部实时更新</strong>
> <details>
><summary>详情</summary>
>
>触发事件时，渲染只会执行一次，而不是遇到一次setVar就执行一次<br>
>每次使用setVar都会记录一个状态更新请求<br>
>React会等当前事件处理函数里所有代码全部跑完,把所有状态更新攒到一起批量处理<br>
>
>
>```js
>function updateVar(Var,setVar){
>   setVar(Var+1)    
>   setVar(Var+2)
>   console.log(Var)
>}
>// 只有事件处理函数结束才会处理Var的更新 
>// 所以打印日志时Var还是原来的值,且这里一次性触发两个状态更新,新的覆盖旧的
>// +1会被+2覆盖,即Var只+2
>
>export function AddVar(){
>    const [Var,setVar] = useState(0) 
>    return <button onClick={()=>updateVar(Var,setVar)}> Var值：{Var} </button>
>} 
>```
>
>```js
>setVar((prev) => {
>    return prev + 1;
>    })
>```
>可以使用prev拿到正真的最新状态值,返回更新的状态
></details><br>
>可以使用prev拿到正真的最新状态值
<br><br>

>[!WARNING] state是不可变的
><details>
><summary>解决办法</summary>
>
>============================================================================<br>
>
>useState中处理对象
>
>```js
>const {MyObj,setMyObj} = useState({
>    name : "jack",
>    age  : 18
>})
>
>// 想要修改MyObj 就必须复制粘贴整个对象，然后修改向要的字段
>// 但其实可以利用解包处理
>setObj({
>    ...MyObj,
>    age:19
>})
>```
>
><strong>可以利用immer里的produce修改<br>
>draft是可变的
></strong>
>`import {produce} from "immer"`
>
>```js
>setMyObj(
>    produce( draft=>{
>        draft.age = 19
>    })
>)
>//对于数组可以直接修改:
>setMyObj(
>    produce( draft=>{
>        draft.push( xxx )
>    })
>)
>
>```
>============================================================================<br>
></details>

</details>

----
<br>


<details>
<summary><strong>useReduce</strong></summary>

```js
//设置初始状态,如果是函数
const initialState = 0; 

//状态更新函数，返回更新的状态
function reducer(state,action){
    switch(action){
        case "actionxxx": { 
            return state+1
        } case "actionxxx": { 
            return state-1
        } default: { 
            return state
        }
    }
}

export function Myfunc(){
    const [state,dispatch] = useReducer(reducer,initialState);
    return (
        //根据传入的action决定如何更新状态
        <button onClick={()=>dispatch(actionxxx)}></button>
    );
}
```


<details>
<summary>useReducer也有惰性初始化的特性</summary>

```js
const initialState = 0; 

//状态更新函数，返回更新的状态
function reducer(state,action){
    switch(action){
        case "actionxxx": { 
            return state+1
        } case "actionxxx": { 
            return state-1
        } default: { 
            return state
        }
    }
}

// 初始化函数
function init(initialState){
    ...
}

export function Myfunc(){
    // 添加init参数，作为初始化函数
    const [state,dispatch] = useReducer(reducer,initialState,init);
    return (
        <button onClick={()=>dispatch(actionxxx)}></button>
    );
}

```
</details>
</details>
<br>





<details>
<summary><strong>useEffect</strong></summary>

---

用于执行副作用操作

`useEffect(回调函数,依赖数组)`


|组件初始渲染必触发一次useEffect|额外触发时机
|---|---
|依赖数组不填  |组件更新执行
|依赖数组为[ ]  |None
|添加依赖项    |依赖项变化时执行
<br>

#### 回调函数的返回值是一个函数，用于执行清除副作用操作( 组件卸载时自动执行 )

```ts
useEffect( 
    () => {
        // 副作用逻辑
        retrun ()=> {
            // 清除副作用逻辑
        }
    },
    [xxx]
)
```

---

</details>




