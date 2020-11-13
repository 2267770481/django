"""
    在models中用自己写的UserInfo表替换了django auth 默认的User表
    用django的用户管理模块实现了 用户的
        注册 -- 可以用django的admin管理页面去添加用户，也可以用自己写的 /user/register 去注册
        登录，退出 -- 在 view 中可看到
        登录检查 -- 在setting中配置了 LOGIN_URL，在index的urls中 用 login_required 包裹要检查的路由

    注：
        需要在在user.admin中注册 UserInfo模型类
"""