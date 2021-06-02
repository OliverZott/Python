def scope_test():

    def do_local():
        msg = "local message"

    def do_nonlocal():
        nonlocal msg
        msg = "nonlocal message"

    def do_global():
        global msg
        msg = "global message"


    msg = "test message inside function-body"
    do_local()
    print("From inside function, after do_local(): ", msg)
    do_nonlocal()
    print("From inside function, after do_nonlocal(): ", msg)
    do_global()
    print("From inside function, after go_global(): ", msg)




scope_test()
print("In global scope: ", msg)
