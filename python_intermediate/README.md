# Resources
https://www.youtube.com/watch?v=eiDyK_ofPPM&list=PLC0nd42SBTaNuP4iB4L6SJlMaHE71FG6N




------------------------------------------------------------------
# Cohesion and Coupling
https://www.youtube.com/watch?v=eiDyK_ofPPM

- Look where the information is stored and decide how to split up 




------------------------------------------------------------------
# Dependency Inversion
https://www.youtube.com/watch?v=Kv5jhbSkqLE&list=PLC0nd42SBTaNuP4iB4L6SJlMaHE71FG6N&index=3

- Seperate components, reduces coupling in code
- Inject abstract classes instead of specific implementations
- ABC module
- Type hints: only for developer... interpreter doesnt do typechecking --> use Pycheck for typechecking!




------------------------------------------------------------------
# Strategy Pattern
https://www.youtube.com/watch?v=WQ8bNdxREHU&list=PLC0nd42SBTaNuP4iB4L6SJlMaHE71FG6N&index=3

### Problem

- Problem: low cohesion / high coupling
- lot of if-else to implement various similar methods to process ticket

### Solution

- Extract functionality into separat base-sub classes with specific tasks

### Simplification

- Use lambda expressions (functional programming) directly

### Open Questions

- Use dependency injection if not using lambdas?





------------------------------------------------------------------
# Observer Pattern
https://www.youtube.com/watch?v=oNalXg67XEE&list=PLC0nd42SBTaNuP4iB4L6SJlMaHE71FG6N&index=5

### Problem

- Problem: low cohesion / high coupling
- Lot of "send_mail" functions in several parts ot the code

### Solution
- Fire events and have the Handlers defined seperatly

### Step-by-step
- **Main**
  - Setup event handlers: `setup_eventblub_handlers()`
  - Call functions and do stuff
- **Event Class** 
  - subbscribers collelction dictionary: `event -> handler`
  - Function to subsricbe handler to an event: `subscribe(event, handler)`
  - Function to post events: `post_event(event, data)`
- **Listener** Class
  - Setup function to register/subscribe handlers to events:       
    `setup_log_event_handlers()`
  - Handler functions: `handle_user registered_event()`
- **Business Logic**
  - Publishing event by using the event-class method `post_event(specific_event, data)`





------------------------------------------------------------------
# Unit Testing & Code Coverage
https://www.youtube.com/watch?v=jmP3fp_BhmE

- `pip install coverage`
- `coverage run .\05-unit-testing\test_vehicle_info.py`
- `coverage html`
 
# Remark
- Test must be deterministic (no random stuff)!
- 100% coverage percentage doesn't mean it's bug-free!

------------------------------------------------------------------
# Various
## Code Smells

https://www.amazon.com/gp/product/0134757599/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0134757599&linkCode=as2&tag=johnovo-20&linkId=76277cc89642d31d242d99b0344cf89e

- https://www.youtube.com/watch?v=LrtnLEkOwFE#