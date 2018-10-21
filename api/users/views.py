from app import App
import logging
from api.users.models import get_all_users

class UserList(App):
    @App.route("/users", methods=['GET'])
    def get(request):
        users_list = get_all_users()
        return request.Response(json=users_list)

