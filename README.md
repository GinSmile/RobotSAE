QRobotX
======

微博机器人，使用Python语言的Flask框架编写，适用于新浪SAE平台。    

本项目依赖于：

* Flask，一个简单的面向需求的微框架，很适合做小项目。    
* sinaweibopy，新浪微博python sdk

类似于英国的大本钟的微博，每小时发布一条微博。本项目微博演示地址：[大笨钟](http://weibo.com/2322493224)

------
###安装
----
 
* 按照官方的[python版hello world教程](http://sae.sina.com.cn/doc/python/tutorial.html)把原始的项目clone到本地。
    * svn co https://svn.sinaapp.com/projectName
2. 用本项目覆盖掉clone的内容
3. 在config文件夹下新建一个myConfig.py文件。

myConfig.py文件内容如下：

	APP_KEY = '225488****'
	APP_SECRET = '3bd49f5d***********' 
	CALL_BACK = 'https://api.weibo.com/oauth2/default.html'
	CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
	USERID = '****登陆邮箱'
	PASSWD = '****密码'
 
	
*  如果需要本地测试，则必须安装Flask，`pip install Flask`。然后用python运行myApp.py，在浏览器输入localhost:5000。也可键入一个其他地址来测试（如localhost:5000/chime用来测试chime函数）。
*  最后用svn提交
   *  svn add 1\
   *  svn ci -m "simple project done!" 

*  此时，键入浏览器地址栏中该项目的地址，projectName.sinaapp.com, 就能进入本项目。


###原理
--------------------
