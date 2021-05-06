# asyncがついた関数をpythonではコルーチンと呼ぶ
# 非同期処理される関数にはasyncをつける
# 非同期処理を呼び出すときにはawaitをつける
import asyncio

# async def main():
#     # 並列処理したいコルーチンを asyncio.gather の引数に渡す
#     await asyncio.gather(
#         hello("Taro"),
#         hello("Jiro"),
#         hello("Saburo")
#     )

# async def hello(name: str, wait_time: int = 2):
#     """ サンプルのコルーチン """
#     print('Hello ...')
#     await asyncio.sleep(wait_time)
#     print(f'{name}!')
#     return name  # 戻り値に name を返す

# if __name__ == "__main__":
#     asyncio.run(main())

# async def main():
#     print('a')
#     await asyncio.sleep(1)
#     print('b')

# asyncio.run(main())

# asyncioを動かすために3つの機能が用意されている
# 最上位のエントリーポイントであるmain()を実行するasyncio.run()
# コルーチンをawaitする
# asyncioのTasksとしてasyncioを並行して動かすasyncio.create_tasks()

import asyncio
import time

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)

# async def main():
#     print(f"started at {time.strftime('%X')}")

#     await say_after(1, 'hello')
#     await say_after(2, 'world')

#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())

# asyncio.create_task()を利用することでコルーチンを並行して実行し、処理完了までの時間が1秒短くなった
# async def main():
#     task1 = asyncio.create_task(
#         say_after(1, 'hello'))

#     task2 = asyncio.create_task(
#         say_after(2, 'world'))

#     print(f"started at {time.strftime('%X')}")
#     await task1
#     await task2
#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())