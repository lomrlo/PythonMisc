import os


def check_ping():
    print ("Enter hostname: ")
    hostname = input()
    response = os.system("ping -c 1 " + hostname)

    # check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

pingstatus = check_ping()
