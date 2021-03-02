#Michael Sieradzki 204256093
import tkinter as tk
import functools
import datetime


def transaction_date(func):
    functools.wraps(func)

    def wrapper_dater(*args, **kwargs):
        value = func(*args, **kwargs)
        print(datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S"))
        return value
    return wrapper_dater


class Account(object):

    def __init__(self, name, ab, an: float):
        self._name = name
        self._ab = ab
        self._loc = 1500
        self._an = an

    def get_name(self):
        return self._name

    def get_ab(self):
        return self._ab

    def get_loc(self):
        return self._loc

    def get_an(self):
        return self._an

    @transaction_date
    def deposit(self, amount: float):
        if amount > 0:
            self._ab = self._ab + amount
            print("DEPOSIT:", self._an, "-", self._name, "- AMOUNT:", amount, "- New Balance:", self.get_ab())
            return True
        return False

    @transaction_date
    def withdraw(self, amount: float):
        if amount <= self.get_ab():
            self._ab -= amount
            print("WITHDRAW:", self._an, "-", self._name, "- AMOUNT:", amount, "- New Balance:",
                  self.get_ab())
            return True
        return False

    def print_balance(self):
        print(self.get_ab())

    def transfer_through_accounts(self, receiver, amount: float):
        if self.withdraw(amount):
            receiver.deposit(amount)
            return True
        return False


def bank_balance(bank: list):
    current_balance = 0
    for account in bank:
        current_balance += account.get_balance()
    yield float(current_balance)


def deposit_to_account():
    main_bank[0].deposit(50)
    tk.Label(root, text=acc1.get_ab(), borderwidth=5).place(x=380, y=80)


def withdraw_from_account():
    main_bank[0].withdraw(63.25)
    tk.Label(root, text=acc1.get_ab(), borderwidth=5).place(x=380, y=80)


def transfer_from_account():
    main_bank[0].transfer_through_accounts(main_bank[1], 300)
    tk.Label(root, text=acc1.get_ab(), borderwidth=5).place(x=380, y=80)


def print_bal():
    acc1.print_balance()


def run_through_file():
    del labels[:]
    f = open("C:\\Users\\Miki\\Desktop\\words.txt", "r+")
    words = f.read().split(',')
    x = 50
    y = 400
    count = 0
    i = 0
    for word in word_generator(words, e2.get(), e1.get()):
        count += 1
        l11 = tk.Label(root, text=word + ",")
        labels.append(l11)
        labels[i].place(x=x, y=y)
        i += 1
        x += 85
        if count == 17:
            x = 50
            y = y + 50
            count = 0


def word_generator(words, letter, boo):
    for word in words:
        if boo.lower() == "exclude":
            if word.find(letter) == -1:
                yield str(word)
        elif boo.lower() == "include":
            if word.find(letter) != -1:
                yield str(word)


def reset():
    for label in labels:
        label.destroy()


if __name__ == '__main__':
    labels = []
    acc1 = Account('Michael', 1150, 1150322)
    acc2 = Account('Moshe', 12150, 1154322)
    main_bank = [acc1, acc2]
    root = tk.Tk()
    root.geometry("1400x700")
    root.title("Central Bank")
    tk.Label(root, text="User Account", font=("arial", 20, "bold")).pack()
    tk.Label(root, text="Question 2", font=("arial", 20, "bold")).place(x=250, y=200)
    tk.Label(root, text="Account name", font=("arial", 10, "bold")).place(x=20, y=50)
    tk.Label(root, text="Account number", font=("arial", 10, "bold")).place(x=200, y=50)
    tk.Label(root, text="Balance", font=("arial", 10, "bold")).place(x=380, y=50)
    tk.Label(root, text="Line of credit", font=("arial", 10, "bold")).place(x=560, y=50)
    tk.Label(root, text=main_bank[0].get_name(), borderwidth=5).place(x=30, y=80)
    tk.Label(root, text=main_bank[0].get_an(), borderwidth=5).place(x=230, y=80)
    tk.Label(root, text=main_bank[0].get_ab(), borderwidth=5).place(x=380, y=80)
    tk.Label(root, text=main_bank[0].get_loc(), borderwidth=5).place(x=600, y=80)
    tk.Button(root, text="Deposit", command=deposit_to_account).place(x=20, y=150)
    tk.Button(root, text="Withdraw", command=withdraw_from_account).place(x=80, y=150)
    tk.Button(root, text="Show Balance", command=print_bal).place(x=150, y=150)
    tk.Button(root, text="Transfer Balance", command=transfer_from_account).place(x=240, y=150)
    tk.Label(root, text="Exclude/Include", font=("arial", 10, "bold")).place(x=420, y=330)
    tk.Label(root, text="Letter to find", font=("arial", 10, "bold")).place(x=420, y=360)
    tk.Button(root, text="Show Words", command=run_through_file).place(x=550, y=300)
    tk.Button(root, text="Reset", command=reset).place(x=630, y=300)
    e1 = tk.Entry(root)
    e2 = tk.Entry(root)
    e2.place(x=550, y=360)
    e1.place(x=550, y=330)
    root.mainloop()









