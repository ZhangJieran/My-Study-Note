<a href="#code">代码模板</a><br>
<a href="#crawlerIns">locator抓取标签示例</a><br>


<h3>录制</h3>

```
playwright codegen https://www.baidu.com
```

<strong>导航</strong>

```
page.goto("网址")    跳转网页
page.reload()        刷新
page.go_back()       前进
page.go_forward()    后退
```
<br>

<strong>页面内容</strong>

```
page.title()      HTML中的title
page.url          当前网页的地址
page.content()    当前网页完整的HTML源码
```
<br>
<strong>页面动作</strong>

```
page.set_viewport_size( {"width":180,"height":300} )  设置窗口大小
page.screenshot(path="存储路径")                       截图
page.evaluate("js代码")                                执行js代码
page.wait_for_timeout(ms)                             页面等待
page.wait_for_selecor("选择器")                        等待选择器出现，超时抛出异常
```
<br>
<h3>元素动作</h3>
<strong>元素定位</strong>

```
page.locator("标签")
page.locator("#id")
page.locator(".className")
page.locator("div[data-v-3432e3]")

对于多层的，可以缩小范围：
page.locator(".className1 .className2 标签1.....")按嵌套层级关系空格分隔，class标签id等任意组合
```
返回Locator对象<br><br>
Locator对象操作：

如果匹配到多个locator，只会对其中一个操作

```
page.locator("...").first.wait_for(state="visible")
locator.all()   ->   返回List[Locator]
```
***locator.all()前，要先page.locator("...").first.wait_for(state="visible"),<mark><strong>否则 locator.all()为空</strong></mark>
<br>
因为locator.all()不会等元素加载完成才抓<br>
***<mark><strong>page.locator("...":visible)</strong></mark>利用伪类只抓取可见的我的建议是<br>
***很多时候html上只有一个标签，但抓出来却有多个,这可能和隐藏标签，Vue多渲染有关（暂时还搞不太清，但用伪类可以解决这种情况）

<mark><strong>对于在iframe里的元素，是匹配不到的</strong></mark>，必须要先 a=page.frame_locator("iframe")<br>
然后再a.locator(.....)

```
<div class="hello hi what">
    <span class="active none">
    </span>
</div>

抓取方式
loc = page.locator(.hello.hi.what)
loc = loc.locator(span.active.none)
或者直接一行
loc = page.locator(.hello.hi.what span.active.none)

同一个标签里有多个class，这些class都连着写，父级标签的和子级标签的要用空格分开

=====================================================
<div class="hi"> hello </div>
<div class="hi"> 你好 </div>
对于标签和class都一样的，用filter区分:
page.locator(".hello").filter(has_text="hello")


```


```
locator.click()             点击
locator.text_content()      获取文本
locator.fill("填入内容")     填入,一般用于input等
locator.press("按键")       按键输入
```






<h3 id="code">代码模板</h3>

```
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("初始网址")
    #-----------------------
    
          自定义代码

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

```
<br><br>
<div id="#crawlerIns">
<h3>locator抓取标签示例</h3>
网页html

```
<div>
    <div class="tag act">
        <p>
            hello world
        </p>
    </div>
<div>

<div>
    <div class="tag act">
        <p>
            hi
        </p>
    </div>
<div>

```
抓取

```
loc = page.locator("div div.tag.act p:visible") #建议每次用locator都加上visible
loc.first.wait_for(state="visible")             #一定要有这个。否则很可能什么都没抓到
locs:list[Locator] = loc.all()                  #一定要先wait_for，才能.all()
```
如果想看标签包裹的文字 locatorIns.text_context()

```
被嵌套在<iframe>下的标签playwright看不到

假设上述示例的html代码就在<iframe>下
framePage = page.frame_locator("iframe:visible")
#只需要先定位到这个<ifame>后面的就一样了
loc = page.locator("div div.tag.act p:visible") 
loc.first.wait_for(state="visible")             
locs:list[Locator] = loc.all()                  

```
</div>





