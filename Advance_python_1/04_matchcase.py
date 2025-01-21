
#switch case statement in python.


def https_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case _:                                    #default case.
            return "internal issue"
        


print(https_status(201))