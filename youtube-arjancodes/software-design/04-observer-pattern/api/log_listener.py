from lib.log import log
from lib.slack import post_slack_message
from .event import subscribe


# Event handler --> handling event
def handle_user_registered_event(user):
    log(
        f"{user.name} has registered with email address: {user.email}")


def handle_password_forgotten_event(user):
    log(f"{user.name} has forgotten his password :/")


# Subscribe event handlers to respective evnts
def setup_log_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_password_forgotten_event)
