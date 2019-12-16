# unittest使用说明

## unittest介绍  
> 一个TestCase的实例就是一个测试用例。什么是测试用例呢？就是一个完整的测试流程，包括测试前准备环境的搭建(setUp)，执行测试代码(run)，以及测试后环境的还原(tearDown)。元测试(unit test)的本质也就在这里，一个测试用例是一个完整的测试单元，通过运行这个测试单元，可以对某一个问题进行验证。

> 而多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite。

> TestLoader是用来加载TestCase到TestSuite中的，其中有几个loadTestsFrom__()方法，就是从各个地方寻找TestCase，创建它们的实例，然后add到TestSuite中，再返回一个TestSuite实例。
  
> TextTestRunner是来执行测试用例的，其中的run(test)会执行TestSuite/TestCase中的run(result)方法。 
  测试的结果会保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息。
  而对一个测试用例环境的搭建和销毁，是一个fixture。
  


一个class继承了unittest.TestCase，便是一个测试用例，但如果其中有多个以 test 开头的方法，那么每有一个这样的方法，在load的时候便会生成一个TestCase实例，如：一个class中有四个test_xxx方法，最后在load到suite中时也有四个测试用例。


**到这里整个流程就清楚了：**

- 写好TestCase，
- 然后由TestLoader加载TestCase到TestSuite，
- 然后由TextTestRunner来运行TestSuite，
- 运行的结果保存在TextTestResult中，
- 通过命令行或者unittest.main()执行时，main会调用TextTestRunner中的run来执行，或者我们可以直接通过TextTestRunner来执行用例。这里加个说明，在Runner执行时，默认将执行结果输出到控制台，我们可以设置其输出到文件，在文件中查看结果（你可能听说过HTMLTestRunner，是的，通过它可以将结果输出到HTML中，生成漂亮的报告，它跟TextTestRunner是一样的，从名字就能看出来，这个我们后面再说）。



## pycharm 下测试模式的设置

**注意**， pycharm下运行，和命令行运行，输出结果不一样,建议使用控制台输出，更美观
- 在第一行给出了每一个用例执行的结果的标识，成功是 .，失败是 F，出错是 E，跳过是 S。从上面也可以看出，测试的执行跟方法的顺序没有关系，test_divide写在了第4个，但是却是第2个执行的。
- 每个测试方法均以 test 开头，否则是不被unittest识别的。
- 在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1，如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果


pycharm 下，如果文件名以test开头，则默认调用py.test进行单元测试（而非unittest）

此时即便设置了main()函数，也不会执行

可以通过设置运行条件修改测试框架（run —— run —— edit configuration）

https://blog.csdn.net/chenmozhe22/article/details/81700504 （特别详细）


## 教程
1. https://blog.csdn.net/huilan_same/article/details/52944782
2. https://blog.csdn.net/u013378642/article/details/82386226
3. http://c.biancheng.net/view/2679.html
