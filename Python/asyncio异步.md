<h3>异步库asyncio</h3>

```
await后必须是 async def 的函数
```


```
asyncio.sleep(int)  异步版本的sleep
```



<h3>事件循环</h3>

```
# 创建事件循环对象
EventLoop = asyncio.new_event_loop()

# 启用该对象
EventLoop.run_until_complete( 主协程 )

# 上面两步骤可以合并成这一步
asyncio.run( 主协程 )

# 返回当前在跑的事件循环对象
asyncio.get_running_loop()
```

事件循环绑定任务

```
EventLoop.create_task( async函数 )       返回任务对象
EventLoop.create_future( async函数 )     返回future对象
```
<br>


<strong>代码示例</strong>

```
async def task1():
    await ...                                            #step6 : 进入task1碰到await,cpu在事件循环队列里拿到task2
async def task2():                                     
    await ...                                            #step7 : task2遇到await,cpu继续寻找可以执行的任务...
                                                         #step8 : 假设task2先执行完成，task2添加到事件循环队列。cpu拿到task2，执行task2中await后的代码
                                                         #step9 : task1执行完成，task1添加到事件循环队列。cpu拿到task1，继续执行await后的代码
async def main():                                       
    EventLoop = asyncio.get_running_loop()               #step2 : 进入main函数，获得刚刚创建的事件循环
    task1 = EventLoop.create_task( task1() )             #step3 : task1 是协程对象，放入事件循环队列         
    task2 = EventLoop.create_task( task2() )             #step4 : task2 是协程对象，放入事件循环队列

    result1 = await task1                                #step5 : main协程被挂起,cpu拿到从队列里拿最前面的--task1
    result2 = await task2                                
                                                         #step10 : main里的两个await都执行完成，main被添加到事件循环队列，cpu拿到main

asyncio.run( main() )                                    #step1 : 启用主协程，main是主协程
```
 

```
result1 = await task1                               
result2 = await task2 

可以直接替换成
result:list[any] = await asyncio.gather( task1(),task2() )
```

<br><br>
<h3>异步函数</h3>

```
async def func():
    ......
    return 1

obj = func()              #不跑func里的代码逻辑，只返回一个协程对象

res = await obj           #这里才跑func的代码逻辑,最后res=1
```
<br>
await语义：挂起当前协程，直到furture为done

```
await Task对象/协程函数/future对象
```



<h3>future对象</h3>

```
# 创建future对象 ( fut状态为pending )
fut = EventLoop.create_future()

#遇到 await fut 
#等待,直到fut被设置为done,重新把当前函数加入事件循环队列
```
<strong>设置future</strong>

```
fut.set_result( val )

res = await fut
```
标记future为done<br>
await fut就会放行，且res = val

```
fut.set_exception(异常对象)
```
标记fut为done<br>
await fut就会抛出这个异常

```
fut.cancel()
```
标记fut为cancelled<br> 
返回bool代表是否取消成功

```
fut.add_done_callback(func)
```
回调函数，当fut被设置为done/cancelled时，立即实行func

<br>
<strong>代码示例：</strong>

```
import asyncio

async def test(fut):
    #一般是把fut传给其他协程，让其他协程设置fut
    fut.set_result("test协程执行完成，返回这个值给main")

async def main():
    EventLoop = asyncio.get_running_loop()
    fut = EventLoop.create_future()

    EventLoop.create_task( test(fut) )

    result = await fut
    print(f"main拿到fut的结果：{result}")

asyncio.run( main() )


输出：
test开始
main拿到fut的结果：test协程执行完成，返回这个值给main
```

