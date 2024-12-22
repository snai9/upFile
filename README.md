# 通过写一些简单的功能来学习Python的基础用法



## 自动上传图片

### 1. 类的用法在自动化测试中常见且灵活
- 通过继承一个基类Base来初始化浏览器环境，并在测试方法upload中实现具体的测试逻辑。
- 可以这样理解，在类中定义的函数称作方法，区别是方法通常会用到 self 参数来访问类的属性和方法
- 方法的第一个参数是self，表示类的实例化对象

### 2. os.getenv("browser")
- 首先要在终端中运行set browser=edge
- 也可以在代码中直接os.environ['browser'] = 'edge'，不过是一次性的

### 3. 上传按钮
- 元素查找，上传按钮如果是input，可对用内置的sendkeys(r"c:\0.jpg")上传文件，r是防止转义
- 本例中的上传按钮是div,不能使用sendkeys(r"c:\0.jpg")上传文件,所以用aardio写了该功能  
-- 使用aardio注意：  
--- 要用控制台模式，WIN界面，这样才会静默运行；  
--- 并且要删除末尾的return win.loopMessage()，不然程序不退出会阻碍代码后续执行



### 4.灵活使用函数的返回值
```python
result = os.system(r"D:\\python学习\\自动化测试\\upfile.exe")
            if result == 0:
                print("点击上传成功")  # 打印成功信息
            else:
                print("上传失败，错误代码:", result)
```
- 不用result会造成不管upfile.exe执行与否，都会直接打印“上传成功”。
- 函数或方法返回值正常都应该为0

### 5.使用日志记录库（如Python的标准库logging）来记录测试过程中的重要信息，而不仅仅是打印到控制台。
```python
logging.basicConfig(level=logging.ERROR,  # 设置日志级别
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='test.log',  # 日志文件名
                    filemode='a')  # 追加模式
```
- 详细和可配置的日志记录：logging库提供了详细的日志级别（如DEBUG、INFO、WARNING、ERROR、CRITICAL），可以根据需要配置不同的日志级别，从而在不同测试阶段查看不同级别的日志信息。

- 灵活性和可扩展性：logging库支持多种日志处理器（如文件处理器、控制台处理器等），可以根据需要将日志输出到文件、控制台或其他目的地。

- 调试和故障排除：在调试过程中，可以使用不同的日志级别来记录不同层次的信息。例如，在调试阶段可以设置为DEBUG级别，记录更多的详细信息，而在生产环境中可以设置为WARNING或ERROR级别，只记录重要的错误信息。

- 日志格式化：logging库支持自定义日志格式，可以记录更多的信息，如时间戳、日志级别、模块名、函数名等，便于后续分析。

- 易于读取和分析：日志文件通常格式化良好，便于阅读和分析。这对于长时间运行的测试或复杂的生产环境非常有用。

## 窗口切换
### 1.这里复习一下列表推导式的用法
```python
new_window = [window for window in self.driver.window_handles if window != original_window][0]
```

### 2.切换到原窗口是关键，方法也很多
```python
original_window = self.driver.window_handles[0] #原始窗口
self.driver.switch_to.window(self.driver.window_handles[-1]) #切换到新窗口
```
- 比列表推导式更简单，但只适合窗口较少，不需要频繁切换的情景

### 3.再来段通过上下文管理器来处理的
```python
class WindowSwitcher:
    def __init__(self, driver, original_window):
        self.driver = driver
        self.original_window = original_window

    def __enter__(self):
        new_window = [window for window in self.driver.window_handles if window != self.original_window][0]
        self.driver.switch_to.window(new_window)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.switch_to.window(self.original_window)

with WindowSwitcher(self.driver, original_window):
    self.driver.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("sn")
    time.sleep(5)
```
优点：
- 代码结构清晰，管理窗口切换的逻辑更加明确。
- 自动处理窗口切换，减少出错的可能性。
- 适用于需要频繁切换窗口的复杂场景。
缺点：
- 代码相对复杂，需要定义额外的类。
- 对于简单的窗口切换场景可能显得过于复杂。




 
