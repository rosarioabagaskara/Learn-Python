import time

listData = ["Bagas", "Nemo", "Tes"]


def checkNemo(array):
    for i in array:
        if (i == "Nemo"):
            return ["Bagas", "lose", "Tes"]
    return "not nemo"


t0 = time.time()
print(checkNemo(listData))
t1 = time.time()

print(f"{t1-t0} Milisec")
