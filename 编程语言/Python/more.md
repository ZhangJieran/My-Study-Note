<a href="#dataclass">@dataclass</a><br>

<br><br><br><br><br><br><br><br>
<div id="dataclass">
<h2>@dataclass</h2>

类的装饰器,自动实现 

```
__init__ __eq__ __repr__
```

```
__eq__ 比较每一个属性值，类型。
```

自动实现> < >= <=
```
@dataclass(order=True)
```
实现行为:将class里的属性依次放入元组，比较元组

</div><br>