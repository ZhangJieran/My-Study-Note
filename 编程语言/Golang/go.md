<a href="#defer">defer</a><br>
<a href="#returndefer">函数匿名返回</a><br>
<a href="#slice">slice</a><br>
<a href="#map">map</a><br>
<a href="#string">string</a><br>
<a href="#assertType">类型断言</a><br>
<a href="#gorutine">并发原语</a><br>
<a href="#reflect">反射</a><br>
<a href="#file">文件操作</a><br>


<div id="defer">
<h3>defer</h3>

```
defer func_a<br>
defer func_b<br>
```
func会推迟到函数return的前一刻执行,defer是一个栈的结构,这里先注册的func_a再注册func_b所以先执行func_b再执行func_a
</div>
<br>
<div id="returndefer">
<h3>函数匿名返回</h3>
创建临时对象res->把return值赋给res->执行defer->返回res
对于匿名返回和命名返回的函数，在defer语句上有差异

``` 
func add1(x int) (res int){              func add2(x int) int {
	res = x                               res := x
    defer func(){res = res*2}()			   defer func(){res = res*2}()
	return res+1 						   return res+1	
}									   }

令x = 1
add1返回4   add2返回2. 
```
add1先创建临时变量res ，res=x 
此时到达return语句，创建临时变量，但返回的临时变量已经有了，故跳过  return值赋给res：res=res+1  执行defer：res=res*2,       return res
add2 函数内声明的res，res:=x 
到达return语句：创建临时变量res2，res2=res+1
执行defer：res = res+2    return res2
</div>
<br>


<div id="slice">
<h3>slice</h3>

```
make(切片类型,len,capacity)    e.g.make([]int,0,10) 
```
创建切片，返回创建的切片<br>

```
append( 原切片，元素args/slice …… )  
```
追加元素，不修改原切片，返回新切片,自动扩容。可以追加元素，也可以追加切片<br>

```
for index,val := range s{
    ......
}
```
切片的遍历。

```
s = append(s[:i],s[i+1])   删除下标为i的元素
```
删除切片元素

```
len（slice）
```

获得切片长度

``` 
copy(s1,s2) 把s2拷贝给s1
```
深拷贝。s1必须已经申请好空间

</div>
<br>
<div id="map">
<h3>map</h3>

``` 
for key,val := range map {
    ......
}

val,ok := map[key]
```
ok是bool类型。表示key是否在map中存在


</div>
<br>

<div id="string">
<h3>string</h3>
string 中的每个字符是 rune 类型<br>
string 是不可变类型<br>
============================ 注意 ================================

```
string[ index ]  返回byte

for index,char := range string{        这里的char是rune
    .......
}
```
==================================================================

```
string[ low:high ]
```
切片操作。

``` 
len(string)
```
返回 <strong>字节数</strong>

``` 
"ab" + "cde"  
```
支持 + 重载

``` 
[]byte  []rune  string   之间可以相互类型转换

e.g.
[]byte(string)  []rune(string)  string( []byte )
```
类型装换<br>

“strings”包

</div>

<br><br><br><br><br><br>


<a id="assertType"></a>

## 类型断言

<details>
<summary><strong>展开</strong></summary> 

---

>[!WARNING] x.(type)
>该语法仅在switch语句中生效
>
>```golang
>switch x.(type) {
>    case int:
>        ...
>    default :
>        ...
>}
>```
<br>

`v,ok := a.(类型)` 类型断言

```golang
v,ok := a.int()
```
<br>
一般空接口用得比较多

```golang
type Test struct {
    number int
}
a := make(map[int]Test)
a[0] = Test{number:1}
// a[0].number  会报错，静态检查认为a[0]是any类型不具备number
// 先断言，再使用
a[0].(Test).numer
```
---

</details>

<br><br><br><br><br><br>

<a id="gorutine"></a>

## 并发原语


<details>
<summary><strong>gorutine</strong></summary>

---

```golang
sync.WaitGroup：

Add(n int) 计数器+n,n可以是负数
Done()	把计数器减 1 （等价于 Add(-1)）
Wait()	阻塞当前 goroutine，直到计数器归零
// main结束不会等待其他rutine结束，使用Wait解决这一点
```





```golang
// 创建协程计数器
var Count sync.WaitGroup  

// 定义协程
func coroutine(){
    ...
    // 协程计数器-1
    Count.Done() 
}

func main(){
    // 协程计数器+1
    Count.Add()
    go coroutine()
    ...
    // 只有协程计数器=0时，主线程才会结束
    Count.Wait()
}
```

---

</details>
<br>

<details>
<summary><strong>MPG</strong></summary> 

---

```
M是一个物理线程
P维护一个装着G的队列
G要执行的任务

M必须要有P挂载才会执行，否则M就闲着，毕竟没有P,M拿不到G

M1-P-G1-G2 , M2   Gorutine ：
最开始P绑定在M1上执行G1,此时G1发生系统调用需要等待
此时P就会换绑到M2上，由M2执行G2。等待G1被唤醒，那么G1会重新进入P的队列。

注意G不会和P绑定：
比如G1原本在P1里，某时G1系统调用，脱离了P1，等G1被唤醒后它可能进入P2的队列

可能会有疑问：虽然P跑到M2去了但M1在等G1,这么看不还是M1被闲置了？
实际上M1确实被闲置了，但M1闲置≠CPU闲置，操作系统会把这个M1线程挂起,CPU去处理其他线程
```



```golang
runtime.NumCPU() 获取当前计算机cpu核数
runtime.GOMAXPROCS(int) P最大个数
// P个数默认是NumCPU 如果设置了GOMMAXPROCS数量就是这个
```
<br>

### G分配给P的规则

|三种队列|解释
|---|---
|P 的本地队列（runq）	|每个 P 私有，容量约 256
全局队列（sched.runq）	|所有 P 共享，当本地队列满时溢出到这里
netpoller 就绪队列	|I/O 完成被唤醒的 G，先到这里再进队列

```
P 本地队列有 G?     → 有就直接跑
        ↓ 没有
查全局队列?         → 有就拿一批（一次拿多个）
        ↓ 没有
从其他 P 偷任务?    → 偷别的 P 本地队列的"后半部分"
        ↓ 没有
从 netpoller 找就绪 G?
        ↓ 还没有
进入自旋（spinning）等待，或休眠
```

---

</details>


<br>
<details>
<summary><strong>管道</strong></summary> 

---

`v,ok := <-chanIns`

|状态	|v|	ok
|---|---|---
|有数据（无论是否已关闭）|	真实值	true
|无数据 + 未关闭|	——	|阻塞等待
|无数据 + 已关闭	|零值	|false

<br>

```golang
for val:= range chanIns {
    // 退出条件：ok == false
}
```

---

</details>
<br><br><br><br><br><br><br><br>



<a id="reflect"></a>

## 反射

```golang
x := Person{name:"jack",age:10}

// 获取类型信息
t := reflect.TypeOf(x)    // t是一个reflect.Type 它描述Person

// 类型名称 "Person"
t.Name() 

// 返回底层类型 reflect.Struct 
// reflect.kind:  reflect.Struct  reflect.Int64  reflect.String...     
t.Kind() 

// 获取值信息
v := reflect.ValueOf(x.age) 
val := v.Int()拿到原始值

```

<br>

### reflect.TypeOf(...).Kind() 底层类型种类

```
kind = reflect.TypeOf(...).Kind()
switch kind {
    case reflect.Int:
        ...
    case reflect.String:
        ...
}
```

<br><br><br><br><br><br><br><br>


<a id="file"></a>

## 文件操作


|方法|作用
|---|---
|`os.Mkdir(path, 权限)`|创建文件夹
|`os.MkdirAll(path,权限)`|创建多级目录
|`FilePtr,err := OpenFile(path,打开模式,权限)`|权限参数只有os.O_CREATE时要写
|`file.Close()`|关闭文件流
|`io.EOF`|文件末尾

|打开模式|含义
|---|---
|os.O_APPEND|追加
|os.O_RDWR|读写
|os.O_RDONLY|只读
|os.O_WRONLY|只写
|os.O_CREATE|创建文件
|os.O_TRUNC|清空
||
e.g.

```
os.OpenFile(path,os.O_CREATE|os.O_WRONLY,0666)
创建文件并只写，0666是权限
```

### 二次封装
|方法|作用
|--|--
|`FilePtr,err:=os.Open(path)`|返回文件指针,默认WRONLY
||

<br>





<details>
<summary><strong>使用文件指针读写</strong></summary>

---

|方法|作用
|--|--
|`n,err:=FilePtr.Read([]byte)`|n为读取到的字节数<br>每次最多读[ ]byte长度这么多字节
|`n,err:=FilePtr.Write([]byte) `|写文件 n为写入字节数
||



>[!NOTE]Read()
>传入一个缓冲区域buf,必须是[ ]byte类型<br>
>把buf读满了就不读了<br>
>无数据可读时err==io.EOF

---

</details>


<details>
<summary><strong>bufio</strong></summary>

---

|方法|作用
|--|--
|`NewReader()`|创建Reader
|`ReadString(分隔符)`|返回string,读到分隔符或EOF为止
|`NewWriter()`|   创建Writer
|`WriteString(string)`|写入,返回int写入字节数和err
<br>

```golang
FilePtr,err := os.Open(...)
defer FilePter.Close()

// 1. 读
reader := bufio.NewReader(FilePtr)
// 传入分隔符,这里是按行读取,返回string类型
str,err := reader.ReadString('\n')

// 2.写
writer := bufio.NewWriter(FilePtr)
// 写入缓存
writer.WriteString(string)  
// 刷新缓存写入文件
writer.Flush() 
```
---

</details>

<br><br>





>[!IMPORTANT]循环读取边界条件
><strong>Read</strong><br>
>最后一次读取不会返回err,因为即使最后一次读不满len([]byte)也不会读超，下一次读才返回err<br>
><strong>Reader</strong><br>
>通常最后一次读取会返回err,因为没遇到分隔符就先读到EOF



</details>
<br>












