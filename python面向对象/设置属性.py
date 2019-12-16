# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         设置属性.py
# Author:       wdf
# Date:         12/8/2019
# IDE：         PyCharm 
# Parameters:
#     @param:
#     @param:
# Return： 
#       
# Description:  
# Usage：
#-------------------------------------------------------------------------------

#### 示例一， 未使用@property，手动实现get、set、del
class C_1(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    # x = property(getx, setx, delx, "I'm the 'x' property.")

### 示例二，使用@property， 与示例一完全等价
class C_2(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value): # 设置属性，注意，此函数名与@property下的完全相同
        self._x = value

    @x.deleter
    def x(self):
        del self._x



def main():
    #### 示例一
    c1 = C_1()
    print(c1.getx()) # 初始为None，没有值
    c1.setx(10) # 赋值
    print(c1.getx()) # 有值
    c1.delx() # 删除值
    # print(c1.getx()) # 没有值(报错，因为x属性也被删除了，没有x）

    print()
    print("示例二")
    c2 = C_2()
    print(c2.x) # None
    c2.x = 10 #赋值
    print(c2.x)
    del c2.x # 删除
    print(c2.x) # 同样报错



if __name__ == '__main__':
    main()