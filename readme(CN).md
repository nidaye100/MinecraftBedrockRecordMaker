# Minecraft 基岩版自定义唱片创建教程

如果你不想替换现有的唱片，而是希望 增加全新的自定义唱片，
在 Minecraft 基岩版中可以通过命名唱片加载自定义音乐
在不干扰原有唱片的情况下，你可以通过“命名并加载不同的音效文件”实现导入，但仍需使用资源包。


## 步骤：

### 1. 创建新的音乐音效
将自定义歌曲以 OGG 格式保存，并命名为自定义名称（最好简单明了不重复，因为第二步需要输入），
例如 my_song_1.ogg。
#### 如何将歌曲文件转换为 OGG 格式？
推荐使用工具：
Audacity（免费，功能强大）https://www.audacityteam.org/
在线转换工具（如 CloudConvert）。

文件路径：

CustomMusicPack/
└── assets/
    └── minecraft/
        └── sounds/
            └── custom/
                ├── my_song_1.ogg
                └── my_song_2.ogg

### 2. 创建行为包
在资源包之外，添加一个与其配套的 行为包 (Behavior Pack)，用以扩展原有的游戏机制。
在行为包中，通过修改 items.json创建一个新的可播放物品（类似唱片）。
可通过程序generate_items.exe批量创建items.json文件。
最后，items.json 文件需要放入行为包的 items

generate_items.exe使用方法：
Ⅰ. 双击运行 `generate_items.exe`。
Ⅱ. 根据提示依次输入：
   - 自定义歌曲标识符（如：my_song_1）。
   - 对应的音效事件（如：custom.my_song_1）。
   - 唱片的物品标识符（如：custom:my_record_1）。
Ⅲ. 程序会自动生成一个 `items.json` 文件，保存在你指定的目录中。


### 3. 制作配套的资源包（与第一步呼应）
在资源包中定义 custom.my_song_1 对应的音效（确保第一步放置的音乐文件名称与第二部创建的相应的物品标识符一致），确保行为包与资源包匹配。

### 4. 使用generate_sound.exe创建sound.json文件并将其放入资源包sound文件夹下。

### 5. 物品皮肤（图标）
自定义唱片的皮肤是由 Minecraft 的图像文件（通常是 .png 文件）决定的。你需要为每张唱片创建一个图标，并将它放入资源包中，以便它在游戏中显示。
你需要在资源包的 textures/items 文件夹下放置一个名为与你的物品标识符相对应的图标。例如，针对 custom:my_record_1，你可以将图标命名为 my_record_1.png 并放入 textures/items 文件夹中。
Minecraft 会自动使用该图标显示物品。确保图标文件命名与物品标识符一致，这样它就会显示为你自定义的图标。

### 6. 放置在服务器并启用
将行为包和资源包放入服务器的 behavior_packs 和 resource_packs 文件夹。
修改服务器设置以强制加载。

### 7. 使用指令获取自定义唱片
通过 Minecraft 的指令，你可以获取自定义唱片。例如，如果你在 JSON 文件中设置了物品标识符为 custom:my_record_1，那么你可以在游戏中通过 /give 指令获得它。
 



 ## 附录

 行为包目录结构（Behavior Pack）
行为包是 Minecraft 基岩版中定义自定义物品、实体等的文件集合，items.json 需要放在 items 文件夹中。

behavior_packs/
└── MyBehaviorPack/                # 行为包的主文件夹
    ├── manifest.json              # 行为包的元信息文件（必须）
    ├── pack_icon.png              # 行为包的图标文件（可选）
    ├── items/                     # 定义自定义物品的文件夹
    │   ├── items.json             # 自定义物品配置文件（包含唱片定义）
    │   └── other_items.json       # 其他物品文件（可选）
    ├── entities/                  # 自定义实体的定义文件夹（可选）
    ├── recipes/                   # 自定义合成表文件夹（可选）
    └── trading/                   # 自定义交易文件夹（可选）


资源包目录结构（Resource Pack）
资源包是 Minecraft 基岩版中定义自定义材质、声音等的文件集合，用于提供唱片的音效和图标。

resource_packs/
└── MyResourcePack/                # 资源包的主文件夹
    ├── manifest.json              # 资源包的元信息文件（必须）
    ├── pack_icon.png              # 资源包的图标文件（可选）
    ├── sounds/                    # 自定义声音文件夹
    │   ├── custom/                # 自定义声音子文件夹（按需命名）
    │   │   ├── my_song_1.ogg     # 自定义唱片的声音文件
    │   │   └── my_song_2.ogg     # 其他声音文件
    │   └── sounds.json            # 声音事件注册文件
    ├── textures/                  # 自定义材质文件夹
    │   └── items/                 # 自定义物品材质子文件夹
    │       ├── custom_record.png  # 自定义唱片图标
    │       └── other_item.png     # 其他物品图标
    └── texts/                     # 语言文件夹
        └── en_US.lang             # 英文翻译文件


整体结构对照

behavior_packs/
└── MyBehaviorPack/
    ├── manifest.json
    ├── items/
    │   └── items.json

resource_packs/
└── MyResourcePack/
    ├── manifest.json
    ├── sounds/
    │   ├── custom/
    │   │   └── my_song_1.ogg
    │   └── sounds.json
    ├── textures/
    │   └── items/
    │       └── custom_record.png
    └── texts/
        └── en_US.lang

