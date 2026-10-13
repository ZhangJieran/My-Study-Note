<a href="#compile">命令行编译</a><br>
<a href="#type">类型声明</a><br>
<a href="#class">类</a><br>
<a href="#interface">接口interface</a><br>
<a href="#board">泛型</a><br>
<a href="#js">引入.js文件</a><br>
<a href="#decorator">装饰器</a><br>

<br><br><br>

<div id="compile">

## 命令行编译

|指令|作用
|---|---
|`npx tsc 文件名`|编译指定ts文件
|`npx tsc --init`|生成tsconfig.json文件，规定ts如何转换成js
|`npx tsc --watch 文件`|只要该文件的 ts 发生变化就实时转成 js


<details>
<summary><strong>tsconfig.json文件</strong></summary>

```js
{
    "comilerOptions":{
        "target" : "es2026",    // 转成的js版本
        "outDir" : "./dist",    // 所有编译后的JS文件统一输出到这个目录
        "noEmitOnerror" : true  // 报错的时候，不要把ts转成js
    }
}
```
</details>
</div>
<br><br><br><br><br><br>





<div id="type">

## 类型声明

<details>
<summary><strong>unknow 是安全版的 any</strong></summary>

---

```ts
const a: any = false
//这是合法的，x明明是string类型，可它存储的是一个boolean值！
x: string = a
```
如果是unknown这里就会报错<br><br>


```ts
const a :unknown = 'hello'
const x :string

// 1.ts认为这是合法的，类型收窄已经确保a是string类型
if(typeof a === 'string'){
    
    x = a
}
// 2.断言
x = a as string
```
---
</details>




<details>
<summary><strong>never和void</strong></summary>

---
用于函数返回值

### never

`const a: never` a不能存任何值<br>
如果不指定never,即使return不写返回值，也会返回undefined

```ts
function demo: never{
    throw new Error('运行异常')
}
```

>[!NOTE]返回never的函数一般是死循环函数或者不能正常结束的函数

### void
可以返回undefined<br>

它和undefined的区别在于，你不能对返回void的函数返回值做任何操作<br>
void的语义是开发者不应该使用函数的返回值

```ts
function demo1():void{
    return undefined
}
function demo2():undefined{
    return undefined
}
const a = demo1() //这是不合法的！
const b = demo2() //合法
```

---
</details>




<details>
<summary><strong>tuple</strong></summary>

---
>[!WARNING] tuple不是关键字
>const a: tuple 错误❌

<strong>tuple是固定类型，固定长度的特殊数组,且数组可以存储多种类型</strong><br>
e.g.

```ts
// a是第一个元素是string，第二个元素是number的数组
const a: [string,number] 
// b第一元素是string,后面可以有无限多个number元素
const b: [string,...number[]]
```

---
</details>



<details>
<summary><strong>enum</strong></summary>

---

```ts
enum 名{
    Enum1,
    Enum2,
    ...
}
```


---
</details>

<details>
<summary><strong>type 自定义类型</strong></summary>

---
联合类型

```ts
type NewType = string | number // 可以是string或number类型
type Gender = '男'|'女'        // 该类型只能存男女
```
<br>
交叉类型

```ts
type Area = {
    height : number;
    width  : number;
};
type Address = {
    num  : number;
    room : string;
};
 
type House = Area & Address 
```
---
</details>
</div>
<br><br><br><br><br><br><br><br>

<div id="class">

## 类

<details>
<summary><strong>基础语法</strong></summary>

---

```ts
class MyClass {
    public    name  : string
    protected age   : number
    private   gender: string
    constructor(name:string,age:number,gender:string) {
        this.name = name
        this.age  = age 
    }
}

//简写形式
class MyClass {
    constructor(
        public    name   : string,
        protected age    : number,
        private   gender : string
    ){ }
}
```

#### 继承与方法

方法也可以加public等修饰，默认是公开

```ts
class A

class B exends A {
    ...
    // 定义方法
    Func1(){
        ...
    }
    // 重写父类方法
    override Func2(){
        ...
    } 
}
```

---
</details>

<details>
<summary><strong>抽象类</strong></summary>

```ts
abstract class Package {
    constructor(public weight:number){}
    // 具体方法
    PrintPackage(){...}
    // 抽象方法
    abstract caculate(x:number):number
}
```
</details>
</div>
<br><br><br><br><br><br><br><br>

<div id="interface">

## 接口interface

<details>
<summary><strong>写法示例</strong></summary>

```ts
interface 对象名 {
    字段a  : 类型
    字段b  : 类型    
    方法(参数:类型) :返回类型
}
```
</details>

### 接口的使用

<details>
<summary><strong>定义类</strong></summary>

```ts
class Person implements PersonInterface {
    ...
} 
```
</details>

<details>
<summary><strong>定义对象</strong></summary>

```ts
interface UserInterface {
    name : string
    age? : number
    run:(n:number)=>void 
}
const user: UserInterface = {
    name:"jack",
    age = 18,
    run(n:number){
        ...
    }
}
```
</details>

<details>
<summary><strong>定义函数</strong></summary>

```ts
interface CountInterface {
    (a:number,b:number):number;
}
const count:CountInterface = (x,y)=>{
    return x+y
}
```
</details>


<details>
<summary><strong>接口继承和重复定义</strong></summary>
继承

```ts
interface A extends B {
    ...
}
```
<br>
重复定义

```ts
interface A {
    ...
}
interface A {
    ...
}
// A接口最后是两次定义内容的总和
```
</details>
</div>
<br><br><br><br><br><br><br><br>


<div id="board">

## 泛型

<details>
<summary><strong>写法示例</strong></summary>

```ts
function Myfunc<T,U>(x:T,y:U) T|U {
    console.log(x)
    console.log(y)
    return Date.now()%2 ? x : y ;
}

Myfunc<number,string>(100,"hello");
```


</details>

</div>
<br><br><br><br><br><br><br><br>





<div id="js">

## 引入 .js 文件

<strong>通过.d.ts文件实现</strong><br>

>[!CAUTION]关键注意点：自己写的.d.ts文件必须被tsconfig.json的include配置覆盖到
>比如include: ["src"]，不然TS编译器根本找不到这些声明文件<br>
>一般.d.ts文件放在src/types/目录下

<details>
<summary><strong>写法示例</strong></summary>
<br>
假设要引入的是demo.js

```ts
function add(x,y) {
    return x+y;
}
```


创建 `demo.d.ts`文件并写入

```ts
declare function add(x:number,b:number):number;
export { add }
```

```ts
// 导入还是导入.js文件
import {add} from "xxx/demo.js"
```
</details>
</div>
<br><br><br><br><br><br><br><br>



<div id="decorator">

## 装饰器

<details>
<summary><strong>类装饰器</strong></summary>
<br>

````ts
function decoratordemo(target:Function){
    // 拿到原型类
    targetClass = target.prototype
    // 重写或新添方法
    targetClass.Myfunc = function(){
        ...
    }
}

````
</details>


</div>
<br><br><br><br><br><br><br><br>







