from lib.slack import post_slack_message
from .event import subscribe


# Setup event handler
def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_registered_event)


# Event handler --> handling event
def handle_user_registered_event(user):
    post_slack_message("Slack channel One",
                       f"{user.name} has registered with email address: {user.email}")
