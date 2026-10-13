<a href="#npm">npm</a>

<div id="npm">

## npm

### 源配置

- 设置源头(阿里源):
` npm config set registry https://registry.npmmirror.com `

- 查看源:
` npm config get registry `


### 创建项目
- ` npm create vite@latest ` &emsp;创建项目
- `cd 项目`    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;进入项目根目录
- `npm install`&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;安装依赖

### 运行项目
- `npm run dev`   运行项目源码
- `npm run build` 打包项目源码(生成dist文件)
- `npm run preview` 运行dist文件

>[!TIP] 这些npm命令其实是vite命令
><details>
><summary>展开</summary>
>项目根目录/package.json<br> 
>这里配置npm命令
>
>```js
>"scripts": {
>    "dev": "vite",
>    "build": "run-p type-check \"build-only {@}\" --",
>    "preview": "vite preview",
>    "build-only": "vite build",
>    "type-check": "vue-tsc --build"
>},
>```

</details>
</div>
















