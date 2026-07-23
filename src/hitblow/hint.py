def make_hint(secret, guess):
    if int(guess) > int(secret):
        return "【ヒント】正解は入力した数字よりも「小さい」です"
    elif int(guess) < int(secret):
        return "【ヒント】正解は入力した数字よりも「大きい」です"
    return None