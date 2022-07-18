subscribers = {}

# list of subscribers which are notified
# REMARK: no type hints for functions --> complete mess


# register handler (function) to event
def subscribe(event_type: str, fn):
    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


# raise events in publisher
def post_event(event_type: str, data):
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type]:
        fn(data)
