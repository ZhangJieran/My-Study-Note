<h2>样式</h2>
<a href="#weilei">伪类</a>&emsp;
<a href="#input">input/form</a>&emsp;
<a href="#vedio-img">vedio/img</a>&emsp;
<a href="#define">选择器定义方式</a>&emsp;
<a href="#table">table</a>&emsp;
<a href="#box">盒子</a>&emsp;
<a href="#location">定位</a>&emsp;
<br><br>

<a href="#common">一般属性</a>&emsp;{
    <a href="#character">字体属性</a>
    <a href="#background">背景属性</a>
    <a href="#text">文本属性</a>
}
<br><br>

<a href="#document">文档流</a>&emsp;{
    <a href="#float">浮动</a> 
}
<br><br>

<a href="#css3">CSS3新特性</a>{
    <a href="#radius">圆角</a>
    <a href="#shadow">阴影</a>
    <a href="#animation">动画</a>
}
<br>


==============================<strong>内部样式表</strong>==================================<br>

``` 
<head>
    <style>
        选择器{
            属性1：属性值1；
            属性2：属性值2；
        }
    </style>
<head>
```
要放在《style》《/style》里声明是css渲染设置

<div id="common"></div>
<strong><em>一般属性</em></strong><br>
<div id="character">
字体属性:<br>

``` 
.box {
    color       :   blue ;        字体颜色
    font-size   :   16px ;        字体大小
    font-family :   KaiTi ;       字体
    font-weight :   700 ;         字体粗细(取值范围100-900)
    font-style  :   italic ;      斜体
}
```
</div>
<br>
<div id="background">
背景属性:<br>

``` 

background-repeat&emsp;&emsp;background-color(blue)&emsp;&emsp;background-image( url("test.jpg") )&emsp;&emsp;background-size&emsp;&emsp;background-position

.box {
    background-color    : red;                                背景颜色
    background-image    : url("图片路径");                     背景图片
    background-repeat   ：repeat/repeat-x/repeat-y/no-repeat; 背景图片铺设方式
    background-size     : 100% 80%/100px 80px/cover/contain;  调整背景图比例,前面是宽后面是高。
                                                              cover保持图片比例且使完全覆盖盒子
                                                              contain保持比例并使在盒子内最大
    background-postion  : 50% 80%                             盒子里的图片渲染位置
    opacity             : 0.2                                 透明度，1为完全不透明
}
```
</div>
<br>
<div id="contain">
容器属性：<br>

``` 
div {
    width  : 400px;
    height : 400px;
}
```
</div>
<br>
<div id="text">
文本属性:

```
.box {
    text-align      : left/right/center;                文本位置
    text-decoration : underline/overline/line-throught; 下划线/上划线/删除线
    text=index      : 50px;                             首行缩进
}
```
</div>

<br>============================<strong>内联样式</strong> ======================================
<br>
<br>
只对当前标签生效  e.g.<div style=”color : red;font-size : 20px” >

============================<strong>外部样式表</strong>====================================<br> 
写在 .css 文件里，引入方式：

```
<head>
    <link rel=”stylesheet” href=”文件路径/文件名.css”> 
</head>
```

=========================================================================
<br>
<div id="define">
<strong>选择器的定义</strong>


```
<head>
    <style>
        .类选择器名{
            属性：属性值;
            ......
        }
        #id选择器名{
            属性：属性值;
            ......
        }
        *{
            属性：属性值;
            ......
        }

        # 子类选择器
        父选择器名>子选择器名{
            属性：属性值；
            ......
        }
        # 后代选择器
        父选择器名 子选择器名{
            属性：属性值；
            ......
        }
        
        # 相邻元素选择器
        选择器1 + 选择器2{
            属性：属性值；
            ......
        }
        # 伪类选择器
        选择器：伪类名{
            属性：属性值；
            ......
        }

    </style>
</head>
```
```
<div class="类选择器名"> 类选择器和class属性绑定 </div>
```

```
<div id="类选择器名"> id选择器和id属性绑定 </div>
```
```
*代表通用选择器，所有的标签都会应用里面设置的属性
```
```
<div class="父选择器名">
    <子选择器名>子类选择器，后代选择器生效</子选择器名>
        <子选择器名>仅后代选择器生效</子选择器名>
</div>
```
子选择器只会对父选择器下一层生效，后代选择器对所有都生效,子选择器中间是>后代选择器中间是空格
子选择器前面可以加 ‘.’ 代表这是类选择器 
此时子选择器应为
```
<div class="父选择器名">
    <标签 class=“子选择器名”></标签>
</div>
```
同理，父选择器前也可以不加‘.’

```
<选择器1>选择器1下方相邻的同级选择器</选择器1>
<选择器2>这个选择器会受到相邻选择器影响</选择器2>
```

<p>伪类表示元素处于特定状态下的样式 :</p>

```
<div class=伪类选择器名>处于某状态时触发效果</div>
e.g. 
.box:hover{
    color:red;
    backgroudd:green;
}

<div class="box">hello</div>
```
hover表示的状态是鼠标悬停在上面，所以当鼠标停在hello上时，它会变红,背景变绿

</div>
<br>

<div id="weilei">
============================
<strong>伪类</strong>=============================================<br>
a标签<br>
link 超链接未访问状态&emsp;&emsp;visited 超链接访问后&emsp;&emsp;hover 鼠标悬浮在元素上&emsp;&emsp;active 鼠标点击瞬间<br>
<u>定义的时候必须依照 LVHA 的顺序</u><br>
子元素伪类<br>
first-child 第一个子元素&emsp;&emsp;
last-child  最后一个子元素&emsp;&emsp;
nth-child(n) 第n个子元素,也可以写2n(偶数)2n+1(奇数)<br>
表单伪类<br>
focus 选中输入框的时候&emsp;&emsp;
checked 单/复选框被勾选&emsp;&emsp;
disabled 表单控件禁用状态<br>
其他<br>
not(选择器) 取反，排除匹配元素<br>
</div>
==============================================================================
<br>
<div id="input">
<h3>input</h3>

```
input {
  width: 200px;                 宽度 
  height: 30px;                 高度
  border: 1px solid #ccc;       边框
  padding: 4px;                 内边距 
  font-size:16px;               文字大小 
  background-color:#fff;        背景色
  color:#333;                   文字颜色
}
```

<strong>form</strong>

```
<form action="url" target="" method="get/post" name="myform">  </form>
```
action服务器地址<br>
get把数据提交url可以看到，post看不到<br>
target表单提交成功后，服务器返回的页面在哪个窗口显示_self覆盖当前页面 _blank新开一个页面
</div>
<br>
<div id="vedio-img">
<h3>vedio/img</h3>

``` 
vedio/img {
    object-fit:fill/contain/cover/none; 
    控制视频如何放入vedio盒子里
    fill 填满盒子（视频可能变形）   contain 保持原比例<br>
    cover 铺满盒子，保持比例,多余部分被裁剪     none 保持比例，超出盒子部分溢出

    object-position:top right;
    水平可选 left center right 
    垂直可选 top center bottom 
    用百分比%       e.g.object-position 80% 30% 画面中心在盒子80%水平 30%垂直位置
    像素px坐标 px   e.g.object-position 20px 10px 画面右移20px,下移10px 
    
    
    width:100%;
    height:auto;
}

```

</div>
<br>

<div id="table">
<h3>table</h3>

``` 
table {
    border           : 1px solid red;   边框粗细，实线,颜色
    border-collapse  : collapse;    折叠边框(合并<td>的边框)
    width            : 500px;
    height           : 100px;
}
td {
    text-align       : left/center/right; 表格内文本的位置
    padding          : 20px 10px;         内边距
    background-color : red;               背景色
    color            : white;             字体颜色 
}
```
</div>
<br>

<div id="box">
<h3>盒子</h3>

``` 
盒子模型
—————————————————————————————————————————————————
|                    margin外边距                |
|      ___________________________________      |
|      |             border边框           |     |
|      |     —————————————————————————    |     |
|      |     |     padding内边距     |    |      |        
|      |     |    ———————————————   |     |     |
|      |     |    |              |  |     |     |
|      |     |    |   content    |  |     |     |
|      |     |    |              |  |     |     |
|      |     |    ————————————————  |     |     |
|      |     |                      |     |     |
|      |     ————————————————————————     |     |
|      |                                  |     |
|      ————————————————————————————————————     |
|                                               |
——————————————————————————————————————————————— |
```
margin是盒外

``` 
标签 {
    width   : 100px;
    height  : 200px;
    padding : 50px 10px 20px 30px;   上右下左  
    border  : 5px solid blue;        边框粗细，实线，蓝色
    margin  : 50px 10px 20px 30px;   外边距看不到，是两个盒子之间的间隔
}
```

```
box-sizing : content-box/border-box
```
content-box : width=content宽度
border-box  ：width=content+padding+border<br>

全局设置box-sizing : border-box 这样增加padding/border只会压缩盒子内部空间，而非扩大盒子。盒子大小和设置的始终一致

<strong>弹性盒子模型</strong>

``` 
在大盒子里嵌套小盒子
<div class="container">
    <div class="box1"> </div>
    <div class="box2"> </div>
    <div class="box3"> </div>
</div>
```

```
.container {
    display          : flex;                        设置为弹性盒子
    flex-direction   : row/column;                  设置主轴线为水平/垂直 (默认row)
    justify-content  : flex-start/flex-end/center;  弹性容器的主轴线水平位置
    align-items      : flex-start/flex-end/center;  弹性容器的主轴线垂直位置 
}

.box1 {
    flex/flex-grow : 2; 
}
.box2 {
    flex/flex-grow : 2; 
}
.box3 {
    flex/flex-grow : 1; 
}

flex/flex-grow 子元素在父容器沿主轴线的权重
box1,box2 占大盒子的2/5, box3 占1/5
```
flex-direction 是子元素之间的相对位置排列关系<br>
justify-content align-items 是主轴线在大盒子里的位置<br>
</div>
<br>

<div id="document">
<h3>文档流</h3>
<div id="float">
<strong>浮动</strong>

``` 
    标签{
        float   : left/right;         脱离文档流
        clear   : left/right/both;    清除浮动
        z-index : 10;                 值越大，盒子出现堆叠的时候越处于上层
}
```


</div>
</div>
<br>

<div id="location">
<h3>定位</h3>

``` 
.box{
    position     : relative/absolute/fixed/stiky;
    left/right   : 100px;                       设置在页面的位置  
    top/bottom   : 40px;
}   

.box
```
relative 还在标准流中，absolute/fixed 会脱离文档流<br>
fixed 即使页面滚动，也一直固定在一个位置<br>
相对定位和绝对定位都是相对于具有定位的父级元素进行调整。如果父级元素没有定位，则向上层查找<br>
sticky:未到达设定位置时跟着页面滚动，到达后被粘住,top为粘住的位置



</div>

<div id="css3">
<h3>CSS3新特性</h3>

<strong id="radius">圆角</strong><br>
``` 
border-radius : 10px/50%;  把盒子的四个尖角变成圆角，100%就是圆
```
border-redius 可以填4个值来更精细地设置圆角<br>

<strong id="shadow">阴影</strong><br>

```
box-shadow : 10px 10px 10px red;    设置盒子阴影
```
四个值分别是：水平阴影位置 垂直阴影位置 阴影模糊度 阴影颜色<br>
阴影位置是相对盒子的位置

<strong id="animation">动画</strong><br>
动画的定义：

```
<style>
    @keyframes 名字 {
        0% {
            css样式
        }
        percent {
            css样式
        }
        ......
        100% {
            css样式
        }
    }
</style>
```
或者可以直接from to

```
<style>
    @keyframes 名字 {
        from {
            css样式
        }
        to {
            css样式
        }
        
    }
</style>
```

动画的执行：

```
animation : name        duration  timing-function  delay  iteration-count  direction;

e.g.
animation : myAnimation    3s        linear          0s         3            normal;
```
——————————————————————————<br>
name&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;动画名称<br>
duration&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;动画持续时间<br>
timing-function&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;动画效果速率(如下)<br>
delay&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;延时执行时间<br>
iteration-count&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;循环次数(infinite无限循环)<br>
direction&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;动画播放方向(如下)<br>
animation-play-state&emsp;&emsp;&emsp;&emsp;播放状态(如下)<br>
——————————————————————————<br>

```
============= timing-function ============
ease                  逐渐变慢
linear                匀速
ease-in               加速
ease-out              减速
ease-in-out           先加速后减速
==========================================
```

```
========== animation-play-state ========
running                     执行
pause                       暂停
========================================
```

```
======== direction ===========
normal          向前播放
alternate       第偶数次向前播放
                第奇数次向后播放
==============================
```

</div>











