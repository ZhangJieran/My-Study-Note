```
.claude/
├── skills/
|   ├── skill-name/
|       ├── SKILL.md
|       ├── ......
├── commands/
    ├── commands-name.md
    ├── ...
```
<br><br><br><br>










## skills


|1|1
|---|---
|元数据层| 始终加载入模型上下文
|指令层Instruction|当模型发现任务与该skill匹配时加载
|资源层|模型根据instruction里的指令


```
skill-name/
├── SKILL.md          # 元数据 + 指令说明 (必须)
├── scripts/          # 可执行代码
├── references/       # 文档资料
├── assets/           # 静态资源
└── ...               # 任何其他文件或目录
```



<details>
<summary><strong>SKILL.md</strong></summary>
<br>

**元信息(机器可读头部)**


|字段|写法
|---|---
|name|必须与skill根目录名称一致<br>只能有 1.数字 2.小写字母 3."-"符号
|description|述技能的作用以及何时使用(最多1024字符)
|licence|开源许可
|compatibility|表示环境需求（预期产品、系统包、网络访问等）
|metadata|自定义键值对
|allowed-tools|该skill被激活时，只能使用这里列出的工具


```
---
name : 会议总结助手
description : 该技能用于根据会议录音总结内容
licence : 
compatibility: compatibility: Requires git, docker, jq, and access to the internet

metadata:
  author: example-org
  version: "1.0"

allowed-tools: Bash(git:*) Bash(jq:*) Read
---
```
元数据置顶且被"---"包裹，下面写Instruct


</details><br>

<br><br><br><br><br><br>



## commands

commands本质是弱化版的skill  <br>


(2026/10/18 commands已被合并入skills)

`/ command` 把对应的md文件的instructtion注入上下文
<br>
skill也可以使用`/ SkillName`注入上下文

command 只能手动注入,模型不会主动读<br>
skill 可以手动注入，模型也可以根据上下文自主判断读取

```
---
name:命令名称      // 和聊天框里的 "/command" 对应
description:...
---

instruction

```

