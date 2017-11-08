# Works

## 安装说明

### 安装 Uliweb 环境

```
pip install -r requirements.txt
```

因为 `uliweb`, `uliweb-ui`, `uliweb-layout`, `uliweb-apps` 会经常更新，所以建议
使用git创建中的版本。

### 编译 vue 组件

```
cd apps/ui
npm install
npm run build
```

编译后的结果将放在 `apps/ui/static/works` 下。

如果不修改代码可以不需要这一步。

### 初始化项目

在 apps 下创建 local_settings.ini 将数据库连接配置好，并建好对应的数据库，如：

```
[GLOBAL]
DEBUG = True
DEBUG_CONSOLE = True
DEBUG_TEMPLATE = False

[ORM]
CONNECTION = 'mysql://user:password@localhost/works?charset=utf8'
CONNECTION_ARGS = {'pool_recycle': 7200}

[PARAMETER]
cache = False
```

根据示例配置，你需要建一个名为 `works` 的数据库，然后将相关的数据库权限给 `user` ，口令是
`password`。其中 `CONNECTION_ARGS` 用于设置数据库连接池的超时时间。

本系统缺省使用Redis对参数进行缓存，也可以象上面将Redis使用关闭。

然后初始化数据库：

```
uliweb syncdb
```

之后创建超级用户：

```
uliweb createsuperuser
```

根据提示创建即可。

再初始化数据，执行：

```
uliweb dbinit
```

会初始化 content_type 和参数表