# from multiprocessing import Process
# import os

# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

# def f(name):
#     info('function f')
#     print('hello', name)

# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()

# import multiprocessing as mp

# def foo(q):
#     q.put('hello')

# if __name__ == '__main__':
#     mp.set_start_method('spawn')
#     q = mp.Queue()
#     p = mp.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()

# import multiprocessing as mp

# def foo(q):
#     q.put('hello')

# if __name__ == '__main__':
#     ctx = mp.get_context('spawn')
#     q = ctx.Queue()
#     p = ctx.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()