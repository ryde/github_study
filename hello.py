
def to_doubles(number: int) -> int:
    """
    入力された数値を2倍にして返す
    """
    return number * 2

def add_owata(text: str) -> str:
    """
    入力された文字列に＼(^o^)／ｵﾜﾀを加える
    """
    return text + '＼(^o^)／ｵﾜﾀ'

if __name__ == '__main__':

    print('hello world')

    ans = to_doubles(23)
    print(ans)

    owata = add_owata('富士通の小学生向けPC')
    print(owata)
