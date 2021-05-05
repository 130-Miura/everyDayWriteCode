# asyncがついた関数をpythonではコルーチンと呼ぶ
# 非同期処理される関数にはasyncをつける
# 非同期処理を呼び出すときにはawaitをつける
import asyncio

async def main():
    # 並列処理したいコルーチンを asyncio.gather の引数に渡す
    await asyncio.gather(
        hello("Taro"),
        hello("Jiro"),
        hello("Saburo")
    )

async def hello(name: str, wait_time: int = 2):
    """ サンプルのコルーチン """
    print('Hello ...')
    await asyncio.sleep(wait_time)
    print(f'{name}!')
    return name  # 戻り値に name を返す

if __name__ == "__main__":
    asyncio.run(main())