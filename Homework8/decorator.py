from datetime import datetime


def timer(func_name):
    def timer2(function):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            # result = function(*args, **kwargs)
            end = datetime.now()
            print(
                "The name of function is : {function_name} ".format(
                    function_name=func_name
                )
            )
            print(
                "function execution time: {time.seconds}s, {time.microseconds}ms".format(
                    time=end - start
                )
            )

        return wrapper

    return timer2
