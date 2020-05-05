
from App.modeles.admin.admin_user_model import AdminUser


def get_admin_user(user_ident):

    if not user_ident:
        return None
    #根据id查找
    user = AdminUser.query.get(user_ident)
    if user:
        return user

    #根据username
    user = AdminUser.query.filter(AdminUser.username.__eq__(user_ident)).first()
    if user:
        return user

    #查不到
    return None
