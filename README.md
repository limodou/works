# Works

## 安装说明

### 安装 Uliweb 环境

```
pip install -r requirements.txt
```

### 编译 vue 组件

```
cd apps/ui
npm install
npm run build
```

编译后的结果将放在 `apps/ui/static/works` 下

### 初始化项目

在 apps 下创建 local_settings.ini 将数据库连接配置好，并建好对应的数据库，如：

```
[GLOBAL]
DEBUG = True
DEBUG_CONSOLE = True
DEBUG_TEMPLATE = False

[ORM]
CONNECTION = 'mysql://user:password@localhost/works?charset=utf8'
```

根据示例配置，你需要建一个名为 `works` 的数据库，然后将相关的数据库权限给 `user` ，口令是
`password`

然后初始化数据库：

```
uliweb syncdb
```

之后创建超级用户：

```
uliweb createsuperuser
```

根据提示创建即可。