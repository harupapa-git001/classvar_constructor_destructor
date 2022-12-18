class HogeHoge:
    a = "hoge" # クラス変数(クラスで共通して使いたい変数)
    counter = 0
class Main(HogeHoge): # クラスの継承
    def __init__(self, name, counter): #  __init__ はオブジェクト生成時に必ず実行される(a=Main(""),b=Main("")で2回呼び出し) name引数の設定 = Main("")で呼び出し → 引数なしでもダブルクォーテーションが必要
        self._a = HogeHoge.a # インスタンス生成
        self.name = name # インスタンス生成
        self.counter = counter

        print(f"コンストラクタが呼び出されました:{self.counter}回目")
        print(f"init_self.a:{self.a}")
        print(f"init_self.name:{self.name}") # __init__では戻り値は常にないので呼び出し側の引数 "Hoge" は返されない
        print()
    
    def sub(self, name):
        #self.a = HogeHoge.a # コンストラクタ
        self.name = name
        print(f"sub_self.a:{self.a}")
        print(f"sub_self.name:{self.name}")
        print()
        return self.name # self.nameを戻り値として返すので 呼び出し側の引数 "HOGE" は返される

    def __del__(self):
        print("インスタンスは破棄されました")

a = Main("", 1) # オブジェクトの生成
ans_a = a.__init__("Hoge", 1) # オブジェクトから__init__にアクセス(引数を与える)
print(f"クラス外_ans_a:{ans_a}")
print()

b = Main("", 2) # オブジェクトの生成
ans_b = b.sub("HOGE") # オブジェクトから.sub()にアクセス(引数を与える)
print(f"クラス外_ans_b:{ans_b}")

del Main
