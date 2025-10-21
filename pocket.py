records = [] #[]でrecordsというリスト（番号付きの棚のイメージ）を作成し、そこに複数のデータを保存できる

balance = 0 

def show_menu(): #def で menu という関数を定義(def)
    print("\n" + "="*30) #\n＝改行　＝*30 で＝を30個表示
    print("お小遣いアプリ")
    print("="*30)
    print("1. 収入を記録")
    print("2. 支出を記録")
    print("3. 履歴を見る")
    print("4. 残高を確認")
    print("5. 終了")
    print("="*30)

#[1.収入を記録]のシステム作成
def add_income():
    global balance, records #global で外からの変更を可能にしている
        #簡易例：普通の家電では家の中からしか操作できないが、globalを入れればIOT家電みたく、家の外からでもエアコン等を操作できるようなイメージ
    item = input("収入の内容を入力") #input() で利用者からの入力を受け取れる
    try: #tryがあることでエラー発生時にエラーが起きたところで止まったりせず、↓exceptまで実行される
        amount =int(input("金額を入力: "))
        balance += amount #balance(残高)にamount(収入)を追加
        record = {
            "種類": "収入",
            "内容": item,
            "金額": amount
        }
        records.append(record) #リスト名.append(追加内容)で、今回の場合 recordsというリストに追加された

        print(f"✅{item}{amount}円を保存しました")
        
    except ValueError: #except はエラー発生時のエラー理由、並びに対処の表示等（どうするかは、次の対処内容次第）を行う
                print("✖ 金額は数字で入力してください")

#[2. 支出を記録]のシステム作成
def add_expense():
    global balance, records
    item = input("支出の内容を入力")
    try:
        amount = int(input("金額を入力: "))
        if amount > balance:
            print("✖ 残高が足りません")
            return

        balance -= amount

        record = {
            "種類": "支出",
            "内容": item,
            "金額": amount
        }
        records.append(record)

        print(f"✅{item}{amount}円を記録しました")
        
    except ValueError:
        print("✖ 金額は数字で入力してください")

def show_records():
    print("\n" + "="*30)
    print("お小遣い履歴")
    print("="*30)

    if len(records) == 0:
        print("まだ記録がありません")
        return

    for i, record in enumerate(records, 1):
        print(f"{i}.[{record['種類']}] {record['内容']}: {record['金額']}円")
            
def show_balance():
    print(f"\n 現在の残高:{balance}円")

def main():
    print("お小遣いアプリへようこそ")

    while True:
        show_menu()
        choice = input("\n選択してください (1-5): ")
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_records()
        elif choice == "4":
            show_balance()
        elif choice == "5":
            print("お小遣いを終了します")
            break
        else:
            print("✖ 1-5の数字を入力してください")
    
if __name__ == "__main__":
    main()
        