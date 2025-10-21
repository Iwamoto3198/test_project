name = "太郎"
age = 25
height = 170.5
is_student = False

print(f"名前: {name}, 年齢: {age}, 身長: {height} cm, 学生か？ {is_student}")
#fについては本来は　"名前:" + {name} + ",年齢:" + {age} + ",身長:" + {height} + "cm," + "学生か？" + {is_student}と記述するものを短縮する役割と思われる。

def greet(name, age):
    return f"こんにちは、{name}さん！{age}歳！"

print(greet("太郎", 25))


score = 90

if score >= 80:
    print("合格！")
elif score >= 50:
    print("補習が必要です")
else:
    print("不合格…")

fruits = ["りんご", "バナナ", "さくらんぼ"]
print(fruits[2])

person = {
    "name": "花子",
    "age": 30
}
print(person["name"])

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"こんにちは、私は{self.name}です。")

person = Person("花子", 30)
person.greet()

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("0では割り算できません!")

import time

print("1. ご飯を炊く（時間がかかる）")
time.sleep(3)  # 3秒待つ（ご飯が炊けるまで待つ）
print("2. ご飯が炊けた")
print("3. 野菜を切る")
print("4. 味噌汁を作る")
print("5. ご飯を盛る")

import asyncio #import + time or asyncio 

async def cook_rice():
    print("1. ご飯を炊く（時間がかかる）")
    await asyncio.sleep(3)  # 3秒待つ（非同期）
    print("2. ご飯が炊けた")

async def cut_vegetables():
    print("3. 野菜を切る")

async def make_soup():
    print("4. 味噌汁を作る")

async def serve_rice():
    print("5. ご飯を盛る")

async def main():
    # 非同期タスクを同時に実行
    task1 = asyncio.create_task(cook_rice())
    task2 = asyncio.create_task(cut_vegetables())
    task3 = asyncio.create_task(make_soup())
    task4 = asyncio.create_task(serve_rice())

    await task1  # ご飯が炊けるのを待つ
    await task2
    await task3
    await task4

asyncio.run(main())