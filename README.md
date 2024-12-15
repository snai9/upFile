# 通过写一些简单的功能来学习Python的基础用法



## 自动上传图片

### 1. os.getenv("browser")
- 首先要在终端中运行set browser=edge
- 也可以在代码中直接os.environ['browser'] = 'edge'，不过是一次性的

### 2. 上传按钮
- 元素查找，上传按钮如果是input，可对用内置的sendkeys(r"c:\0.jpg")上传文件，r是防止转义
- 本例中的上传按钮是div,不能使用sendkeys(r"c:\0.jpg")上传文件,所以用aardio写了该功能  
-- 使用aardio注意：  
--- 要用控制台模式，WIN界面，这样才会静默运行；  
--- 并且要删除末尾的return win.loopMessage()，不然程序不退出会阻碍代码后续执行



### 3.
```python
result = os.system(r"D:\\python学习\\自动化测试\\upfile.exe")
            if result == 0:
                print("点击上传成功")  # 打印成功信息
            else:
                print("上传失败，错误代码:", result)
```
- 不用result会造成不管upfile.exe执行与否，都会直接打印“上传成功”。
- 函数或方法返回值正常都应该为0




 
