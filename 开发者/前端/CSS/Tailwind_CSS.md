
<a href="#DefineToolClass">自定义工具类</a>


## 配置

- 安装
`npm install tailwindcss @tailwindcss/vite`

- vite.configs.ts文件

```ts
import tailwindcss from '@tailwindcss/vite'
export default definedConfig({
    plugins:[
        ...,
        tailwindcss()
    ]

})
```

- index.css文件
`@import "tailwindcss";`





<br><br><br><br><br><br>

<div id="DefineToolClass"></div>

## 自定义工具类

<details>
<summary><strong>@utility</strong></summary>
写原生css,把它变成工具类

```css
@utility MyClass {
    color : red;
    width : 100;
}
```
<br>

传递参数（ 使用`-*` ）

```css
@theme {
    --MyColor-1 : red;
    --MyColor-blue : blue;
}

@utility MyClass-* {
    color : --value(; MyColor-* )
}

<div class="MyClass-1">
</div>
```

</details>

<details>
<summary><strong>@apply</strong></summary>

@apply 使用已有的工具类，组合成新的类

```css
.MyClass {
    @apply w-100 bg-red-500 ... ;
}
```
</details>



<details>
<summary><strong>@variant</strong></summary>

### 主题提切换

```css
.box {
    @apply bg-color-white w-20 h-20;
    
    @variant dark {
        @apply bg-black
    }
}
```

等价于,可以用于主题切换

```css
.box {
    @apply bg-white-500 w-20 h-20;
}

.dark .box {
    @apply bg-black-500 w-20 h-20;
}

```

### 定义伪类变体

```ts
@import "tailwindcss";

.test {
    @apply bg-amber-500 size-16;
    @variant hover {
        @apply bg-cyan-600;
    }
}
```

</details>
<br><br><br><br><br><br>







```css
bg-red-xxx     背景颜色
text-red-xxx   字体颜色
w-xxx           宽
h-xxx           高


```