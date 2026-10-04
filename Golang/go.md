<a href="#defer">defer</a><br>
<a href="#returndefer">函数匿名返回</a><br>
<a href="#slice">slice</a><br>
<a href="#map">map</a><br>
<a href="#string">string</a><br>
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