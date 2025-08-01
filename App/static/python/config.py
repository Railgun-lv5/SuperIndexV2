#SuperIndex文件配置
# SuperIndex --
#             |-Library                                             用于储存您的资源！
#             |
#             |-Tool--|-resourcetool.exe                            用于管理、备份资源           
#             |
#             |-App--——————————————————————————————————————————————储存着所有处理资源的代码,请不要改变下面文件内容布局
#                   |-static--
#                   |        |-python--|-app.py config.py ...      当前以及所有python文件的位置！
#                   |        |        
#                   |        |-js--                                 一系列主页相关功能js
#                   |             |-hub--|-event.js ... 
#                   |             |                 
#                   |             |-resource_detail--|-event.js ...
#                   |                         ·      
#                   |-templates--
#                   |           |-html                              储存html和css基础网页布局
#                   |           |-css
#                   |-other--
#                   |       |-decorate                              网站首页用于充当背景装饰的图片
#                   |       |-emptycover                            当资源缺失图片内容时所使用的默认图片
#                   |
#                   |-dependency--                                  预留依赖项：ffmpeg,python3.13
#                   |            |-python313
#                   |            |-ffmpeg
#                   |
#                   |-database--
#                   |          |-database.db                        储存资源数据
#                   |          |-thumbnail--|-xxx.jpg               储存预览图
#                   #————————————————————————————————————————————————————————————————————————————————————
import os
import re

#SuperIndex支持的格式
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.tiff', '.ico')
VIDEO_EXTENSIONS = ('.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv','.webm')
SERIES_FOLDER_PATTERN = re.compile(r'^\[.*\]$')

#自动读取SUPERINDEX根目录(/SuperIndex)
SUPERINDEX_BASE_DRIVE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

STATIC_DIR = os.path.join(SUPERINDEX_BASE_DRIVE_PATH, 'App', 'static')
TEMPLATE_DIR = os.path.join(SUPERINDEX_BASE_DRIVE_PATH, 'App', 'templates')
EMPTYCOVER_DIR = os.path.join(SUPERINDEX_BASE_DRIVE_PATH,'App','other','emptycover')

#个性化
DECORATE_DIR = os.path.join(SUPERINDEX_BASE_DRIVE_PATH, 'App', 'other', 'decorate')

#依赖项
FFMPEG_BIN = os.path.join(SUPERINDEX_BASE_DRIVE_PATH, 'App', 'dependency', 'ffmpeg', 'bin', 'ffmpeg.exe')
FFPROBE_BIN = os.path.join(SUPERINDEX_BASE_DRIVE_PATH, 'App', 'dependency', 'ffmpeg', 'bin', 'ffprobe.exe')


#资源目录配置
SUPERINDEX_LIBRARY_ROOT = os.path.join(SUPERINDEX_BASE_DRIVE_PATH, 'Library')
RESOURCE_DIRECTORIES = {
    '里番': os.path.join(SUPERINDEX_LIBRARY_ROOT, 'Animation'),
    '成人视频': os.path.join(SUPERINDEX_LIBRARY_ROOT, 'Pronvideo'),
    'CG渲染': os.path.join(SUPERINDEX_LIBRARY_ROOT, 'CG'),
    '同人志': os.path.join(SUPERINDEX_LIBRARY_ROOT, 'Doujinshi'),
    '图集': os.path.join(SUPERINDEX_LIBRARY_ROOT, 'Illustration'),
    '游戏': os.path.join(SUPERINDEX_LIBRARY_ROOT, 'Eroge'),
    }

#数据
DATABASE_DIR = os.path.join(SUPERINDEX_BASE_DRIVE_PATH, 'App', 'database', 'database.db')
THUMBNAIL_DIR = os.path.join(SUPERINDEX_BASE_DRIVE_PATH, 'App','database', 'thumbnail')

#辅助函数
def check_path(path):
    return "✓" if os.path.exists(path) else "✗"

def Checking_Config_Path():
    print(f"#————————————————————————[config.py]———————————————————————————— —————————— ———————— ———— —— -")
    print(f"|   正在进行资源路径确认,缺失的路径将会标出:")
    print(f"|   {check_path(SUPERINDEX_BASE_DRIVE_PATH)} SuperIndex 根目录: {SUPERINDEX_BASE_DRIVE_PATH}") 
    print(f"|   {check_path(SUPERINDEX_LIBRARY_ROOT)} SuperIndex 资源目录: {SUPERINDEX_LIBRARY_ROOT}")
    print(f"|   {check_path(THUMBNAIL_DIR)} 缩略图目录: {THUMBNAIL_DIR}")
    print(f"|   {check_path(EMPTYCOVER_DIR)} 默认图片目录: {EMPTYCOVER_DIR}")
    print(f"|   {check_path(DECORATE_DIR)} 图片装饰目录: {DECORATE_DIR}")
    print(f"|   {check_path(FFMPEG_BIN)} FFmpeg 路径: {FFMPEG_BIN}")
    print(f"|   {check_path(FFPROBE_BIN)} FFprobe 路径: {FFPROBE_BIN}")
    print(f"|   {check_path(DATABASE_DIR)} 数据目录: {DATABASE_DIR}")
    print(f"|")
    print(f"|   详细资源内容路径:")
    for k, v in RESOURCE_DIRECTORIES.items():
        print(f"|   {check_path(v)}【{k}】:{v}")
    print(f"#————————————————————————[config.py]———————————————————————————— —————————— ———————— ———— —— -")

Checking_Config_Path()