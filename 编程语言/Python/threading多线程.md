
```
new = threading.Thread( target=func )    添加线程
new.start()                              启动线程
new.join()                               阻塞
```

```
from queue import Queue    #线程队列

que = queue.Queue( maxsize=5 )

# 放数据,如果队列满了，会阻塞等待空位
que.put(val)  

# 获取数据，如果队列为空，会阻塞等待数据
que.get()     

# 当前队列元素数量
que.qsize() 
```













