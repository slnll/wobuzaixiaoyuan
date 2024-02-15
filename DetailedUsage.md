# 详细使用方法

## 1. Fork 本仓库

<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/01.png?raw=true" style="zoom:60%;" />
<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/02.png?raw=true" style="zoom:60%;" />

## 2. 开启工作流读写权限

<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/03.png?raw=true" style="zoom:60%;" />
<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/04.png?raw=true" style="zoom:60%;" />
<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/05.png?raw=true" style="zoom:60%;" />

## 3. 添加 Secrets



> Name = Name，Secret = 例子

| Name     | 例子         | 说明                                                         |
| -------- | ------------ | ------------------------------------------------------------ |
| USERNAME | 1008610086   | 我在校园账号（手机号）                                       |
| PASSWORD | I love study | 我在校园密码                                                 |
| TOKEN    | piannide     | [Pushplus 的 token](https://www.pushplus.plus/doc/guide/openApi.html#_1-%E8%8E%B7%E5%8F%96token "Pushplus 的 token") |

<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/06.png?raw=true" style="zoom:60%;" />
<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/07.png?raw=true" style="zoom:60%;" />

### 获取 TOKEN

[登录 Pushplus ](https://www.pushplus.plus/login.html)

<img src="https://cdn.jsdelivr.net/gh/NianBroken/ZFCheckScores/img/17.png" style="zoom:60%;" />

[获取 Token](https://www.pushplus.plus/api/open/user/token)

打开页面后，你会得到一个类似下列所示的 Json 代码块，`data`中的值就是 TOKEN

```json
{
	"code": 200,
	"msg": "请求成功",
	"data": "cd735c356aa14d16b1452aa932ac89cc",
	"count": null
}
```

[相关文档](https://www.pushplus.plus/doc/guide/openApi.html#_1-%E8%8E%B7%E5%8F%96token)

当你的 Secrets 添加完成后，你的页面应该是类似下图所示
<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/08.png?raw=true" style="zoom:60%;" />

## 4. 开启 Actions

<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/09.png?raw=true" style="zoom:60%;" />
<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/10.png?raw=true" style="zoom:60%;" />

## 5. 运行程序

<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/11.png?raw=true" style="zoom:60%;" />
<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/12.png?raw=true" style="zoom:60%;" />

## 6. 查看运行结果

当你的页面类似下图所示时则表示程序正常运行且未报错
<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/13.png?raw=true" style="zoom:60%;" />
<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/14.png?raw=true" style="zoom:60%;" />
在此之后，程序将会每隔 30 分钟自动运行一次

## 7. 成绩更新通知

当检测到成绩更新时，你的页面应该是类似下图所示
<img src="https://github.com/slnll/wobuzaixiaoyuan/blob/main/img/15.png?raw=true" style="zoom:60%;" />
