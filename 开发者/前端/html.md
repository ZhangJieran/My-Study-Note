块级元素：div form h1-h6 hr p table ul......&emsp;从上到下排列，每个元素独占一行<br>
内联元素：a b em i span strong......&emsp;行内元素<br>
行内块级元素：img button input......不换行,块级元素可以识别宽高（width="10px"），内联不行

<a href="#form">form</a>表单；表单元素{<br>
&emsp;<a href="#input">input</a>&emsp;
<br>}

<a href="#Mark">html语义化标签</a><br>
<a href="#script">script</a><br>


<br>
<div id="form">
    <strong>form</strong> 
    
``` 

<form action="url" method="get|post" name="myform">  </form>

action 服务器地址 
name   表单名称
method 提交数据的方式  get提交url看得到，post看不到        


表单按钮<button type="submit"> <input type="submit">
        <button type="reset"> <input type="reset">

表单域 <input> <textarea>多行文本框 <select>下拉选择框

```
</div>
<br>
<div id="input">
    <strong>
        input
    </strong>

``` 
<input type=""> 
```
password密码&emsp;&emsp;text文本&emsp;&emsp;radio单选框&emsp;&emsp;checkbox多选框&emsp;&emsp;file上传文件<br>
submit提交&emsp;&emsp;value按钮上显示的文字&emsp;&emsp;placeholder框内显示的文字
</div> 

<div id="Mark">
<h3>html语义化标签</h3>
<a href=".../markdownImg/html语义化标签.jpg">图片</a>


</div>

<br>
<div id="script">
<h3>script</h3>
1.直接写

```
<script>
    JavaScript代码......
</scripy>
```
2.引入JavaScript文件

```
<script type="text/javascript" src="./MyFile.js">   </script>
```

3.引入网络文件

```
<script src="https://....../xxx.js">   </script>
```


</div>