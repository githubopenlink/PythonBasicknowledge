#以清华源为例
#临时使用
'''
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package matplotlib
除了matplotlib是要安装的库名外，其他都是固定格式
'''
#设为默认
'''
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
'''
#主流镜像源地址
'''
清华：          https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：        http://mirrors.aliyun.com/pypi/simple/
中国科技大学    https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：  http://pypi.hustunique.com/
山东理工大学：  http://pypi.sdutlinux.org/
豆瓣：          http://pypi.douban.com/simple/
'''
#查看pip版本
'''
​pip --version​
'''
#升级pip
'''
pip install --upgrade pip​
'''
#获取帮助
'''
​pip help​
'''
#批量安装库
'''
pip install -r e:\requirements.txt

requirements.txt文件内容格式如下
matplotlib==3.4.1
pillow==8.2.0
pickleshare=0.7.5
'''
#卸载库
'''
pip uninstall package_name​
'''
#升级库
'''
​pip install --upgrade package_name​
'''
#查看库信息
'''
pip show -f package_name​
'''
#查看已安装的库
'''
​pip list​
'''
#将库列表保存到指定文件中
'''
pip freeze > requirements.txt​
'''
#查看需要升级的库
'''
pip list -o​
'''
#检查兼容问题
'''
pip check package-name​
'''
#将库下载到本地指定文件，保存为whl格式
'''
pip download package_name -d "要保存的文件路径"​
'''