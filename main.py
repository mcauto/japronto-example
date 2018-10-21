from app import app

from api.users.views import UserList

app.run(port=8080, debug=True, reload=True)
