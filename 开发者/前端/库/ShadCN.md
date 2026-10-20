>[!IMPORTANT] 依赖tailwindcss


- 编辑tsconfig,json

```json
{
  "files": [],
  "references": [
    {
      "path": "./tsconfig.app.json"
    },
    {
      "path": "./tsconfig.node.json"
    }
  ],
////////////////////  新增  ///////////////////////
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"]
    }
///////////////////////////////////////////////////
  }
}
```
- 编辑tsconfig.app.json
```json
{
  "compilerOptions": {
    // ...
    "paths": {
      "@/*": [
        "./src/*"
      ]
    }
    // ...
  }
}
```
<br><br>

更新 vite.config.ts<br>
安装并更新，以便 Vite 能解决别名：@types/nodevite.config.ts@

```
npm install -D @types/node
```

```ts
import path from "path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})
```
<br><br>

运行CLI<br>
在你的项目中运行init命令来设置shadcn/ui：shadcn
```
npx shadcn@latest init
```






## 使用

```
npx shadcn@latest add button
```
```ts
import { Button } from "@/components/ui/button"

function App() {
  return (
    <div className="flex min-h-svh flex-col items-center justify-center">
      <Button>Click me</Button>
    </div>
  )
}

export default App
```
