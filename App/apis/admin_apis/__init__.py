from flask_restful import Api

from App.apis.admin_apis.admin_user_api import AdminUsersResource
from App.apis.admin_apis.cinema_auth_api import CinemasUsersResource,CinemasUserResource

admin_api = Api(prefix='/admin')
admin_api.add_resource(AdminUsersResource,'/users/')
admin_api.add_resource(CinemasUsersResource,'/cinemausers/')
admin_api.add_resource(CinemasUserResource,'/cinemausers/<int:id>/')