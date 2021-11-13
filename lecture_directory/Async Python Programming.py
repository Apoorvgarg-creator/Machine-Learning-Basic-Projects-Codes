# Asynchronous Python Programming (APP)
# --> A type of parallel programming in which a unit of work is allowed to run separately from the primary
# application thread. When the work is complete, it notifies the main thread about completion or failure
# of the worker thread. There are numerous benefits to using it, such as improved application performance and enhanced
# responsiveness

# Synchronous python programming --> we send a request 1 wait for response 1 and then we can send request 2 and then get
# response 2. The tasks are going serial method
# Asynchronous python programming --> we send request 1 and separately send request 2 also and then gets the
# response in parallel for both the request.
# async is faster than sync

# 4 ways of implementing APP -->
# 1. Multi processing
# 2. Multi threading
# 3. couroutines
# 4. AsyncIO - lib in python to implement APP


# MULTI PROCESS -->
# create a python file hello.py
# Go in terminal
# run the code : hello.py & python hello.py --> APP
# if run the code like : hello.py && python hello.py --> one will run completely without any error then other
# will send the request

# from multiprocessing import Process
#
#
# def showsquare(num=2):
#     print(num ** 2)
#
# # create a list of processes that you will run in parallel
#
# procs = []
#
# for i in range(2):
#    procs.append(Process(target=showsquare()))
#
# for proc in procs:
#     proc.start()
# print("Apoorv")
# # for proc in procs:
# #     proc.join()

# Multi Threading
# To perform multi threading, python provides a lib called threading
from threading import Thread

# Coroutines
# in this method we controls the the routine of threads, not automatically done by the operating system
# with the help of generator, coroutines are developed

# AsyncIO



