from datetime import datetime


def timer(function):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = function(*args, **kwargs)
        #end = datetime.now()
        #print(
            #"function execution time: {time.seconds}s, {time.microseconds}ms".format(
                #time=end - start
            #)
        #)
        print("goldston is a big dumbass!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return result
    return wrapper


