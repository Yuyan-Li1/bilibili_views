# bilibili_views
中文版往下⬇️
## English
### get_views.py
#### Description
This tool gets you the title and number of views, likes, and comments of the videos from Bilibili of which the BV numbers you put into `BV.txt`.
#### How to use
1. Install the packages with this command in terminal: `pip3 install -r requirements.txt`(You only need to do this once).
2. Put video BV numbers into `BV.txt`.
3. Type this in terminal: `python3 get_views.py`.
### uid_to_profile_pic.py
#### Description
This tool downloads all the profile pictures of users whose uids you have put into `UID.txt`. You can find the files in the `profile_pics` directory each named with the users' respective uid.
### How to use
1. Install the packages with this command in terminal: `pip3 install -r requirements.txt`(You only need to do this once).
2. Put user ids into `UID.txt`.
3. Type this in terminal: `python3 uid_to_profile_pic.py`.
4. Find files in `profile_pics` folder.
## 中文
### get_views.py
#### 简介
这个工具可以用你放在`BV.txt`里面的 Bilibili 视频 BV 号来提取这些视频的播放量，点赞数和评论数。
#### 使用方法
1. 在终端里用这条命令安装需求文件：`pip3 install -r requirements.txt`（这个只需要做一次）。
2. 将所需视频 BV 号放到`BV.txt`里。
3. 在终端输入：`python3 get_views.py`。
### uid_to_profile_pic.py
#### 简介
这个工具可以将你放在`UID.txt`中所有的 Bilibili uid 所对应用户的头像下载到`profile_pics`目录。文件名是对应用户的 uid。
#### 使用方法
1. 在终端里用这条命令安装需求文件：`pip3 install -r requirements.txt`（这个只需要做一次）。
2. 将所需用户 uid 放到`UID.txt`里。
3. 在终端输入：`python3 uid_to_profile_pic.py`。
4. 在`profile_pics`文件夹里找到你要的文件。
