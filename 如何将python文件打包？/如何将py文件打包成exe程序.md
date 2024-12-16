# 如何将 Python 文件打包为 .exe 可执行程序？

## 1.确认环境
```
在python官网下载python https://www.python.org/downloads/，
勾选自动创建路径选项并安装。之后可以在cmd中输入python -version
来确认是否安装成功。
```
### 如果不是在官网，如微软市场下载的python，需要手动配置环境。
```
Ⅰ打开cmd，输入where python获得安装路径并复制，
例如：C:\Users\<你的用户名>\AppData\Local\Programs\Python\Python<版本号>。
Ⅱ右键计算机（此电脑），点击属性，找到高级系统设置，点击环境变量。在下方系统变量中找到path，
双击后点击新建，粘贴已复制的安装路径。
```
### 确认 pyinstaller 是否安装
```
可以在命令行中运行以下命令来检查：pip show pyinstaller
如果 pyinstaller 没有安装，可以使用以下命令来安装：pip install pyinstaller

有时即使安装了 pyinstaller，如果它的安装路径没有添加到环境变量 PATH 中，也可能会导致无法识别命令。
你可以尝试通过 python -m PyInstaller 来代替直接调用 pyinstaller。例如：python -m PyInstaller --version
如果能够成功运行，则说明 pyinstaller 已经正确安装，只是路径没有添加到系统的环境变量中。
如果不能成功运行，则需要添加 Python 和 Scripts 目录到环境变量。
```
***关于检查 Scripts 目录：***
```
Python 安装时会在 Scripts 目录下安装工具（如 pyinstaller）。你可以通过以下路径找到 Scripts 目录：
如果你使用的是 Microsoft Store 安装的 Python，通常路径类似于 C:\Users\buquz\AppData\Local\Microsoft\WindowsApps\Scripts。
你需要将 Python 的 Scripts 目录添加到系统环境变量 PATH 中，这样 pyinstaller 等工具才能在命令行中被识别。
注意：where scripts 命令是用来查找 scripts 可执行文件的位置，但它可能无法找到该文件夹，因为你正在查找的实际上是一个目录，而不是一个可执行文件。

在cmd中可通过 echo %PATH% 来查看PATH 环境变量。
```
***在更改环境变量之后需要重启cmd，否则结果不会更新***

## 2.打包 Python 脚本

Ⅰ编写python程序并保存为.py文件。
Ⅱ在命令行中进入脚本所在目录，运行以下命令：pyinstaller --onefile --noconsole generate_items.py
```
--onefile：将所有依赖打包到一个单独的 .exe 文件中。
--noconsole：隐藏运行时的命令行窗口（适用于图形化应用）。
```
打包完成后，程序会在 dist 文件夹中生成一个名为 generate_items.exe 的可执行文件。

打包程序的优点就是.exe 文件可以复制到其他 Windows 电脑上使用而无需安装 Python 环境。
缺点是因包含了所有 Python 运行时和依赖，打包后文件可能比较大；
打包的 .exe 文件仅能在 Windows 系统上运行；
某些杀毒软件可能会误报 .exe 文件为病毒，这是常见问题。如果分发，建议添加说明。


## 3.更多优化尝试

### 3.1 使用 --icon 参数来指定一个自定义图标，用以更改使用 PyInstaller 打包的 .exe 文件的图标。
***步骤***
####3.1.1 准备图标文件
确保你有一个 .ico 格式的图标文件。如果你有一个 .png 或其他格式的图片，你可以通过在线工具或图标转换软件将其转换为 .ico 格式。

有很多在线工具可以帮助你将图片转换为 .ico 格式。例如：
ConvertICO （https://convertico.com/）或 ICO Convert（https://www.icoconvert.com/）

####3.1.2使用 PyInstaller 打包时指定图标
使用 PyInstaller 打包你的 Python 脚本时，添加 --icon 参数来指定自定义图标文件。例如：
pyinstaller --onefile --icon=your_icon.ico your_script.py
```
--onefile 参数用于将 Python 脚本打包成一个单独的 .exe 文件（可选，具体取决于你的需求）。
--icon=your_icon.ico 指定了你要使用的图标文件。
```
如果你已经打包了 .exe 文件并且希望更改图标，那么你需要重新打包，使用新的图标文件。
PyInstaller 并不支持在已打包的 .exe 文件中直接更改图标，因此你必须重新使用正确的 --icon 参数来打包。
在每次打包时会同时生成一些用作打包配置的中间文件，如build文件夹和.spec文件。如若需要重新打包，请在打包前删除这些文件以防干扰。

如果图标没有更新，可能是 PyInstaller 缓存了旧的设置，你可以清理缓存并重新打包：
pyinstaller --clean --onefile --icon=your_icon.ico your_script.py

若任然没有更新，可以尝试重启该cmd或计算机并再次打包。

***关于生成的文件***
dist/ 文件夹：
这是最终的输出文件夹，里面包含了你打包后的 .exe 文件。
例如，如果你打包的程序是 generate_items.py，那么你会在 dist 文件夹里找到 generate_items.exe。

build/ 文件夹：
这个文件夹是 PyInstaller 在打包过程中生成的临时文件夹，里面包含了一些中间文件和缓存数据。
这些文件对于最终生成的 .exe 文件并不重要，你可以在打包完成后删除 build 文件夹。
它是 PyInstaller 用来处理打包过程的内部文件夹。

generate_items.spec 文件：
这个文件是 PyInstaller 为你生成的一个配置文件，里面包含了关于如何构建 .exe 文件的设定。
如果你需要定制化打包过程（比如添加更多的资源文件），可以编辑这个 .spec 文件并重新打包。

在打包完成后，如果你不再需要 PyInstaller 生成的中间文件夹和配置文件，你可以删除以下文件和文件夹：

build/：临时文件夹，包含中间文件，可以删除。
generate_items.spec：如果你不打算修改打包配置，可以删除。
你只需要保留 dist/ 文件夹中的 .exe 文件，它是程序的最终可执行文件。


### 3.2完善程序属性

在 Windows 文件的属性中，文件版本、文件名称和版权等信息是通过修改文件的元数据来设置的。
对于 .exe 文件来说，设置这些信息通常需要在打包时提供相关的配置信息。
这些元数据可以通过在 PyInstaller 打包时使用 --version-file 参数，或使用其他工具来为 .exe 文件添加。
PyInstaller 并没有直接提供命令行选项来设置文件版本信息和版权等。但是你可以通过以下方法来为 .exe 文件添加版本信息和版权信息.

#### 3.2.1使用 PyInstaller 设置文件版本信息

##### Ⅰ创建一个版本信息文件：
你可以创建一个 .txt 文件，称为版本信息文件（通常是 .rc 文件），并在其中定义版本信息、文件名、版权等元数据。



##### Ⅱ生成版本文件：
在 PyInstaller 打包时，通过 --version-file 参数指定一个版本文件。
你可以手动创建一个 .rc 文件，或者使用 PyInstaller 生成一个基本的版本信息文件。
使用以下命令来打包你的程序，并为 .exe 文件添加版本信息：
pyinstaller --onefile --noconsole --icon=cd.ico --version-file=version.txt generate_items.py

***书写建议***
在 .exe 文件中设置的版本信息、公司名称、产品名称、版权等信息，通常是为了提供一些有关软件的基本元数据。
这些信息本身并不具备法律效力，但是它们在某些场景下（比如软件分发、版权声明、版本控制等）会起到重要作用。它们的作用和书写建议如下：

1. 版本信息（FileVersion 和 ProductVersion）
作用：版本信息通常用于指示程序的版本，帮助用户和开发人员了解当前使用的软件版本。在软件更新、错误修复或兼容性测试时非常有用。
法律效力：版本号本身没有法律效力，但它有助于软件开发者在多个版本间进行区分。
书写建议：
常用格式：主版本.次版本.修订版.构建号，例如：1.0.0.0。
版本号通常递增，确保清晰的更新日志和版本历史。
2. 公司名称（CompanyName）
作用：显示开发或发行该软件的公司或个人的名称。这有助于用户识别软件的来源。
法律效力：在法律上，正确标识公司名称和开发者有助于表明软件的所有者，但仅在文件属性中显示并不会直接产生法律约束力。
书写建议：
使用正式的公司名称，或在软件是个人项目时使用个人名称。
3. 产品名称（ProductName）
作用：指明该软件的名称，通常与公司或产品的品牌相关。
法律效力：产品名称本身没有法律效力，但它是品牌识别的一部分。如果使用某些已注册的商标或品牌名称，可能涉及商标保护的法律规定。
书写建议：
使用准确和一致的产品名称，避免误导消费者。
4. 文件描述（FileDescription）
作用：描述软件或文件的功能和用途。例如，描述该 .exe 是一个“图像编辑工具”或“游戏启动程序”。
法律效力：文件描述本身不具备法律效力，但有助于用户了解软件的用途。需要确保描述准确，避免误导用户。
书写建议：
提供清晰且简洁的描述，避免夸大软件功能或用途。
5. 版权信息（Copyright）
作用：版权声明用于表明软件的所有者以及版权的归属。版权信息的正确书写对于保护软件开发者的合法权益非常重要。
法律效力：版权声明具有法律效力。根据不同国家的版权法，软件的版权由软件开发者自动拥有，或者如果在开发过程中有合同或协议，版权可能属于公司或其他法人。
书写建议：
格式：Copyright (C) [年份] [公司名或个人名]，例如：Copyright (C) 2024 YourCompany。
如果软件包含开源部分或使用开源许可证（如GPL、MIT等），应明确说明哪些部分是开源的，哪些部分是受版权保护的。
6. 商标（Trademark）
作用：如果软件名、公司名或标志已经注册为商标，商标声明可以用来保护品牌和标识。商标声明表明该名称或标识已在某些地区获得法律保护。
法律效力：商标声明有法律效力，表示该商标已注册，并且仅商标持有者有权使用。
书写建议：
如果软件或公司名称已经注册为商标，可以在版权信息后附加商标符号（例如™或®），例如：YourSoftware™ 或 YourSoftware®。
7. 许可证信息（License）
作用：如果软件有特定的许可证（如开源许可证或商业许可证），应在文件属性中标明。
法律效力：许可证有法律效力，规定了软件的使用、分发和修改的条件。许可证通常附带在软件包中，而不仅仅是通过文件属性显示。
书写建议：
如果软件使用了开源许可证（如MIT、GPL等），应在版权信息旁注明许可证类型，并包含完整的许可证文本。
对于商业软件，许可证通常会说明允许的使用范围以及可能的限制。
总结与书写建议：
版权声明：应确保版权信息准确无误。建议标注当前年份以及公司或个人名称。
版本信息：使用清晰且一致的版本号，有助于区分软件的不同版本。
描述信息：保持准确、简洁，避免虚假宣传。
商标信息：如果软件使用了注册商标，应标明商标符号。
许可证信息：如果软件是开源的或有特定的使用许可证，必须在文档中明确标示，并附上完整的许可证条款。
虽然文件中的这些信息并没有直接的法律约束力（除非涉及版权或商标保护），但是它们对于软件分发、品牌保护和用户的知情权有重要作用。
在实际使用时，确保信息的准确性，遵守相关的版权和商标法律，是非常重要的。

样版：
```
# UTF-8
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x4,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'YourCompanyName'),
        StringStruct(u'FileDescription', u'Tool for batch generating items.json files in Minecraft Bedrock Edition'),
        StringStruct(u'FileVersion', u'1.0.0.0'),
        StringStruct(u'InternalName', u'generate_items'),
        StringStruct(u'LegalCopyright', u'Copyright (C) 2024 YourCompanyName'),
        StringStruct(u'OriginalFilename', u'generate_items.exe'),
        StringStruct(u'ProductName', u'ndy100'),
        StringStruct(u'ProductVersion', u'1.0.0.0')])
      ]
    ),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)

```
***关键点解释***
VSVersionInfo 的结构:

它是一个嵌套结构，包含 FixedFileInfo 和 StringFileInfo，后者又包含 StringTable 和 StringStruct。
必须使用正确的括号和逗号，否则会导致解析失败。
常见字段:

CompanyName：公司或个人名称。
FileDescription：工具或文件的简要描述。
FileVersion 和 ProductVersion：版本号，格式为 (主版本号, 次版本号, 修订版本号, 内部版本号)。
LegalCopyright：版权声明。
OriginalFilename：原始文件名（通常是目标 exe 的文件名）。
ProductName：产品名称。
语言和代码页 (Translation):

1033 表示英语 (美国)。
1200 表示 Unicode。
