# 正方教务管理系统成绩推送



## 简介
<img src="https://github.com/slnll/wobuzaixiaoyuan/tree/main/img/0.png" style="zoom:60%;" />

**使用本项目前：**

你在外玩的正嗨时，需要找人签到，你夜不归宿时提心吊胆，生怕导员弄个签到，让你措手不及

**使用本项目后：**

自动检测是否有签到，如果有将自动签到，并将结果告知你（目前能力有限，只有微信的通知）



## 测试环境

我在校园小程序 版本 V2.3.9

嗯，就是下面的

<img src="https://github.com/slnll/wobuzaixiaoyuan/tree/main/img/1.jpg" style="zoom:60%;" />



## 目前支持的功能

1. 主要功能

   1. 每隔 30 分钟（可以自己设）自动检测一次是否有签到，若有更新，将自动签到并通过微信推送及时通知用户。

2. 注意事项

   本项目由于是自动化工程，所以只支持校区签到，目前仅有西安邮电大学适配（我的是长安校区的，雁塔的同学自行修改里面的经纬度）



## 使用方法

### 1. [Fork](https://github.com/NianBroken/ZFCheckScores/fork "Fork") 本仓库

`Fork` → `Create fork`

### 2. [开启](https://github.com/kekeaiaixueer/ZFCheckScores/settings/actions "开启")工作流读写权限

`Settings` → `Actions` → `General` → `Workflow permissions` →`Read and write permissions` →`Save`

### 3. [添加](https://github.com/kekeaiaixueer/ZFCheckScores/settings/secrets/actions "添加") Secrets

`Settings` → `Secrets and variables` → `Actions` → `Secrets` → `Repository secrets` → `New repository secret`

> Name = Name，Secret = 例子

| Name     | 例子                 | 说明                                                         |
| -------- | -------------------- | ------------------------------------------------------------ |
|          |                      |                                                              |
| USERNAME | 2971802058           | 我在校园账号（手机号）                                       |
| PASSWORD | Y3xhaCkb5PZ4         | 我在校园密码                                                 |
| TOKEN    | J65KWMBfyDh3YPLpcvm8 | [Pushplus 的 token](https://www.pushplus.plus/doc/guide/openApi.html#_1-%E8%8E%B7%E5%8F%96token "Pushplus 的 token") |

### 4. [开启](https://github.com/kekeaiaixueer/ZFCheckScores/actions "开启") Actions

`Actions` → `I understand my workflows, go ahead and enable them` → `CheckScores` → `Enable workflow`

### 5. [运行](https://github.com/kekeaiaixueer/ZFCheckScores/actions/workflows/main.yml "运行")程序

`Actions` → `CheckScores` → `Run workflow`

_若你的程序正常运行且未报错，那么在此之后，程序将会每隔 30 分钟自动运行一次_

_若你看不懂上述使用方法，你可以查看[详细使用方法](https://github.com/NianBroken/ZFCheckScores/blob/main/DetailedUsage.md "详细使用方法")_



## 特别感谢

[smallway233/I-can-t-be-on-school](https://github.com/smallway233/I-can-t-be-on-school)

## 其他

欢迎提交 `Issues` 和 `Pull requests`
