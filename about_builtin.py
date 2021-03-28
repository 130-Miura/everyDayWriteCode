# 組み込み関数の列挙
# print(list(name for name in vars(__builtins__)))

# 組み込み関数の種類（int()など、コンストラクタ含む）
# print(list(name for name in vars(__builtins__) if (name[0].islower() and name not in ('quit', 'exit', 'copyright', 'credits', 'license',)) or name == '__import__'))

# 組み込み関数の個数（int()など、コンストラクタ含む）
# print(len(list(name for name in vars(__builtins__) if (name[0].islower() and name not in ('quit', 'exit', 'copyright', 'credits', 'license',)) or name=='__import__')))