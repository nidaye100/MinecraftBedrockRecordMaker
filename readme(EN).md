# Minecraft Bedrock Edition Custom Record Creation Guide

If you don't want to replace the existing records but wish to **add entirely new custom records**, Minecraft Bedrock Edition allows you to load custom music by naming the records. You can import custom music without interfering with existing records by "naming and loading different sound files," but you will still need to use a resource pack.

## Steps:

### 1. Create New Music Sounds
Save the custom songs in **OGG format** and name them with custom names (preferably simple and unique, as this name will need to be inputted in step 2), for example, `my_song_1.ogg`.

#### How to Convert Song Files to OGG Format?
Recommended tools:
 **Audacity** (free, powerful) [Audacity Official](https://www.audacityteam.org/)
 **Online Conversion Tools** (such as CloudConvert).

**File Path:**

```plaintext
CustomMusicPack/
└── assets/
    └── minecraft/
        └── sounds/
            └── custom/
                ├── my_song_1.ogg
                └── my_song_2.ogg


### 2. Create a Behavior Pack
In addition to the resource pack, add a corresponding Behavior Pack to extend the game mechanics. In the behavior pack, modify the items.json to create a new playable item (similar to a record). You can batch-create the items.json file using the generate_items.exe program. Lastly, the items.json file must be placed in the items folder of the behavior pack.

generate_items.exe Usage:
Double-click to run generate_items.exe.
Follow the prompts to input:
Custom song identifier (e.g., my_song_1).
Corresponding sound event (e.g., custom.my_song_1).
Record's item identifier (e.g., custom:my_record_1).
The program will automatically generate an items.json file, saved in the directory you specify.

### 3. Create the Corresponding Resource Pack (Matching Step 1)
In the resource pack, define the sound event custom.my_song_1 (ensure the music file name placed in Step 1 matches the item identifier created in Step 2). Ensure that the behavior pack and resource pack match.

### 4. Use generate_sound.exe to Create the sounds.json File
Place the generated sounds.json file in the sounds folder of the resource pack.

### 5. Item Skin (Icon)
The skin of custom records is determined by Minecraft's image files (usually .png). You need to create an icon for each record and place it in the resource pack so it will display in the game.

You need to place an icon in the textures/items folder in the resource pack, named to match the item identifier. For example, for custom:my_record_1, you can name the icon my_record_1.png and place it in the textures/items folder.

Minecraft will automatically use this icon to display the item. Make sure the icon file name matches the item identifier so it will display as your custom icon.

### 6. Place on Server and Enable
Place the behavior pack and resource pack in the server's behavior_packs and resource_packs folders. Modify the server settings to force load them.

### 7. Use Commands to Get Custom Records
Through Minecraft's commands, you can obtain the custom records. For example, if you set the item identifier to custom:my_record_1 in the JSON files, you can obtain it in-game using the /give command.

## Appendix
Behavior Pack Directory Structure
The behavior pack is a collection of files that define custom items, entities, and more in Minecraft Bedrock Edition. The items.json file needs to be placed in the items folder.

behavior_packs/
└── MyBehaviorPack/                # Main folder of the behavior pack
    ├── manifest.json              # Required metadata file for the behavior pack
    ├── pack_icon.png              # Optional icon for the behavior pack
    ├── items/                     # Folder for defining custom items
    │   ├── items.json             # Custom item configuration file (includes record definition)
    │   └── other_items.json       # Other item files (optional)
    ├── entities/                  # Folder for custom entity definitions (optional)
    ├── recipes/                   # Folder for custom recipes (optional)
    └── trading/                   # Folder for custom trading (optional)


Resource Pack Directory Structure
The resource pack is a collection of files that define custom textures, sounds, and more for Minecraft Bedrock Edition. It is used to provide the sound and icon for the record.

resource_packs/
└── MyResourcePack/                # Main folder of the resource pack
    ├── manifest.json              # Required metadata file for the resource pack
    ├── pack_icon.png              # Optional icon for the resource pack
    ├── sounds/                    # Folder for custom sounds
    │   ├── custom/                # Subfolder for custom sounds (name as needed)
    │   │   ├── my_song_1.ogg     # Custom record sound file
    │   │   └── my_song_2.ogg     # Other sound files
    │   └── sounds.json            # Sound event registration file
    ├── textures/                  # Folder for custom textures
    │   └── items/                 # Subfolder for custom item textures
    │       ├── custom_record.png  # Custom record icon
    │       └── other_item.png     # Other item icons
    └── texts/                     # Folder for language files
        └── en_US.lang             # English language file

        
Overall Directory Structure

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
    │   └
