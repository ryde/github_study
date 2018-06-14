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

def listing(*args) -> list:
    """
    入力された値をリストにして返す
    """
    return [i for i in args]