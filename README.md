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



### 3. json.dump(数据, f, ensure_ascii=False, indent=4)
- 用于将 Python 对象编码成 JSON 格式，并写入到文件中。
- data：要序列化的 Python 数据结构（通常是字典或列表）。
- f：一个文件对象，用于写入JSON数据。文件对象应该以写入模式打开（即 'w'）。
- ensure_ascii：默认值为 True，如果设置为 False，则允许 JSON 字符串中包含非ASCII字符。
- indent：用于美化输出的缩进级别。如果设置为 None 或 0，则输出的JSON数据不会进行格式化（即没有缩进和换行）。如果设置为正整数，则输出的JSON数据会根据该缩进级别进行格式化。



### 4. return bool(re.match(r'^1[3-9]\d{9}$', 手机号))
- 用bool来取得是还是否，不需要用if来判断，基本的内置函数巧妙使用



### 5. return 0 < 年龄 < 150
- Python中，函数的返回值可以是任何表达式的结果，包括比较表达式。


### 6. return all(学生["手机号"] != 手机号 and 学生["身份证号"] != 身份证号 for 学生 in 数据)
- 也是用最基础的内置函数来判断是和否，省去了反复的if判断
- all() 函数是 Python 内置的一个函数，用于检查可迭代对象（如列表、元组、集合等）中的所有元素是否都为 True。如果所有元素都为 True，all() 函数返回 True；如果任何一个元素为 False 或者可迭代对象为空，all() 函数返回 False。
- all() 函数经常与生成器表达式或列表推导式一起使用，以检查一个条件是否对所有元素都成立。


### 7. for 编号, 课程名 in enumerate(课程, start=1):
- enumerate() 函数用于将一个可迭代对象（如列表、元组、字符串等）组合为一个索引序列，同时列出数据和数据下标。这个函数通常用于 for 循环中，以便在迭代过程中同时获取每个元素的索引和值。
- Python 字典中有一个类似于 enumerate() 函数的功能，它叫做 items()。items() 方法用于返回一个包含字典中所有键值对的视图对象，每个键值对都是一个元组，其中第一个元素是键，第二个元素是值。这使得你可以在 for 循环中同时迭代字典的键和值。
- enumerate() 函数返回的是一个枚举对象，该对象可以被迭代，产生包含索引和值的元组。通常用在需要对元素进行编号的场景，比如在循环中跟踪元素的位置。
- items() 方法返回的是一个视图对象，该对象也可以被迭代，产生包含键和值的元组。通常用在需要同时访问字典的键和值的场景，比如在循环中处理字典中的每个条目。
 
