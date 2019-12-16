# timeit 模块：准确测量小段代码的执行时间（python 内置）
timeit 模块中的三个函数
- timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000)：
    创建一个Timer实例，参数分别是stmt（需要测量的语句或函数），setup（初始化代码或构建环境的导入语句），timer（计时函数），number（每一次测量中语句被执行的次数）
- timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=3, number=1000000)：
    创建一个Timer实例，指定整个试验的重复次数，返回一个包含了每次试验的执行时间的列表，利用这一函数可以很方便得实现多次试验取平均的方法。
- timeit.default_timer()：
    默认的计时器，一般是time.perf_counter()，time.perf_counter()方法能够在任一平台提供最高精度的计时器（它也只是记录了自然时间，记录自然时间会被很多其他因素影响，例如计算机的负载）

## 示例

```python
import timeit

def test():
	L = []
	for i in range(100):
		L.append(i)
if __name__ == '__main__':
	print (timeit.timeit("test()", setup="from __main__ import test"))
	
	x = list(range(2000000))
	t0 = timeit.timeit("x.pop(0)", "from __main__ import x", number=1000)
	print("cost {} seconds ".format(t0))
```

## 在命令行测试

命令格式： `python -m timeit [-n N] [-r N] [-u U] [-s S] [-t] [-c] [-h] [语句 ...]`

参数：

-n：执行次数  
-r：计时器重复次数  
-s：执行环境配置（通常该语句只被执行一次）    
-p：处理器时间  
-v：打印原始时间  
-h：帮助    

```bash
python -m timeit "[i for i in range(10000)]" # 注意，在windows系统下，命令语句最外层要用双引号

python -m timeit -s "text = 'sample string'; char = 'g'"  "char in text"  # 多行命令，一起测试，可以写成多个语句

# 与之对等的脚本：
import timeit
timeit.timeit('char in text', setup='text = "sample string"; char = "g"')
# 0.41440500499993504
timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"')
# 1.7246671520006203
```