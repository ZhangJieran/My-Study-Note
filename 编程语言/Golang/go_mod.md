|指令|作用|例子
|---|---|---
|`go mod init 模块名`|生成go.mod 文件|`go mod init demo`
|`go get 库地址`|安装第三方库|`go get github.com/gin-gonic/gin`

<br>

```
project
|—— go.mod
|—— main.go
|——package_i
   |—— module_i
```


package1.go 中要有package package1这行代码，表示这个go文件属于package1

main.go 里通过 import”模块名/package1” 导入包
一个包里的go文件之间，不需要import，直接就能相互用
import 别名 "模块名/package1" 也可以


func init()
执行流程： 全局声明 -> init() -> main()



