from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan

from api.slack_listener import setup_slack_event_handlers
from api.log_listener import setup_log_event_handlers


setup_log_event_handlers()
setup_slack_event_handlers()

# register a new user
register_new_user("User1", "pw1", "user1@mail.com")

# send password reset message
password_forgotten("user1@mail.com")

# upgrade the plan
# upgrade_plan("user1@mail.com")
