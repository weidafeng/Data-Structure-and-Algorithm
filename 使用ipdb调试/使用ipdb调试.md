# 使用ipdb调试

IPDB（Ipython Debugger），和GDB类似，是一款集成了Ipython的Python代码命令行调试工具，可以看做PDB的升级版。


## 安装与使用
IPDB以Python第三方库的形式给出，使用`pip install ipdb`即可轻松安装。

在使用时，有两种常见方式。

- 集成到源代码中
- 通过在代码开头导入包，可以直接在代码指定位置插入断点。如下所示：

```python 
import ipdb
# some code
x = 10
ipdb.set_trace()
y = 20
# other code
```
则程序会在执行完x = 10这条语句之后停止，展开Ipython环境，就可以自由地调试了。

### 命令式
上面的方法很方便，但是也有不灵活的缺点。

对于一段比较棘手的代码，我们可能需要按步执行，边运行边跟踪代码流并进行调试，这时候使用交互式的命令式调试方法更加有效。启动IPDB调试环境的方法也很简单：

`python -m ipdb your_code.py`

```bash
python -m ipdb "3. 数组中重复的数字.py"

然后会启动调试器，跳转到第一行代码

按next 或 step， 往下跳转

如果要在第70行设置断点，使用 b 70

使用step可以进入断点

``` 



## 常用命令

IPDB调试环境提供的常见命令有：

### 帮助

使用h即可调出IPDB的帮助。
```
# ipdb 支持的所有命令
ipdb> h

Documented commands (type help <topic>):
========================================
EOF    cl         disable  interact  next    psource  rv         unt
a      clear      display  j         p       q        s          until
alias  commands   down     jump      pdef    quit     source     up
args   condition  enable   l         pdoc    r        step       w
b      cont       exit     list      pfile   restart  tbreak     whatis
break  continue   h        ll        pinfo   return   u          where
bt     d          help     longlist  pinfo2  retval   unalias
c      debug      ignore   n         pp      run      undisplay

Miscellaneous help topics:
==========================
exec  pdb
```

使用help command的方法查询特定命令的具体用法, 如
```
ipdb> help r
r(eturn)
        Continue execution until the current function returns.
```


### 下一条语句  next
使用n(next)执行下一条语句。

注意一个函数调用也是一个语句。

### 进入函数内部 step
使用s(step into)进入函数调用的内部。

### 打断点  break
使用`b line_number(break)`的方式给指定的行号位置加上断点。

使用`b file_name:line_number`的方法给指定的文件（还没执行到的代码可能在外部文件中）中指定行号位置打上断点。

另外，打断点还支持指定条件下进入，可以查询帮助文档。
```
ipdb> help b
b(reak) [ ([filename:]lineno | function) [, condition] ]
        Without argument, list all breaks.

        With a line number argument, set a break at this line in the
        current file.  With a function name, set a break at the first
        executable line of that function.  If a second argument is
        present, it is a string specifying an expression which must
        evaluate to true before the breakpoint is honored.

        The line number may be prefixed with a filename and a colon,
        to specify a breakpoint in another file (probably one that
        hasn't been loaded yet).  The file is searched for on
        sys.path; the .py suffix may be omitted.
        
```

### 一直执行直到遇到下一个断点 continue
使用c(continue)执行代码直到遇到某个断点或程序执行完毕。

### 一直执行直到返回 return 
使用r(return)执行代码直到当前所在的这个函数返回。

### 跳过某段代码 jump
使用j line_number(jump)可以跳过某段代码，直接执行指定行号所在的代码。

### 显示更多上下文 list
在IPDB调试环境中，默认只显示当前执行的代码行，以及其上下各一行的代码。

如果想要看到更多的上下文代码，可以使用l first[, second](list)命令。
-  l 查看当前的上下文
-  l 10, 20 查看10-20行代码

### 我在哪里 where
一层一层函数调用，显示到当前行

调试兴起，可能你会忘了自己目前所在的行号。例如在打印了若干变量值后，屏幕完全被这些值占据。使用w或者where可以打印出目前所在的行号位置以及上下文信息。


### 列出当前函数的全部参数 argument
当你身处一个函数内部的时候，可以使用a(argument)打印出传入函数的所有参数的值。

### 打印 print 
使用p(print)和pp(pretty print)可以打印表达式的值。
如 p my_varible

### 清除断点 clear
使用cl或者clear file:line_number清除断点。如果没有参数，则清除所有断点。

### 再来一次 restart
使用restart重新启动调试器，断点等信息都会保留。

restart实际是run的别名，使用run args的方式传入参数。

### 退出 quit
使用q退出调试，并清除所有信息。

