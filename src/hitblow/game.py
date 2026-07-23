import time

from .core import judge, make_secret
from .result import calculate_score, format_time

def play():

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    while True:
        level = input("何桁で遊びますか？（3～10）> ").strip()

        if level.isdigit():
            digits = int(level)
            if 3 <= digits <= 10:
                break

        print("3～10の数字を入力してください。")

    secret = make_secret(digits)
    max_tries = digits**2 * 2

    print(f"Hit & Blow（{digits} 桁・重複なし）")
    print(f"解答可能回数は{max_tries}回です。")

    # ストップウォッチ開始
    start_time = time.time()

    tries = 0
    while True:
        guess = input("予想 > ").strip()

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue

        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")

        # 挑戦回数が最大回数の半分以上になったらヒントを表示
        if tries >= max_tries / 2:
            if int(guess) > int(secret):
                print("【ヒント】正解は入力した数字よりも「小さい」です")
            elif int(guess) < int(secret):
                print("【ヒント】正解は入力した数字よりも「大きい」です")

        if hit == digits:
            end_time = time.time()
            elapsed = end_time - start_time

            score = calculate_score(digits, tries, elapsed)
            time_str = format_time(elapsed)

            print()
            print("========== RESULT ==========")
            print(f"正解！ 答えは {secret}")
            print(f"解答回数 : {tries}回")
            print(f"クリア時間 : {time_str}")
            print(f"スコア : {score}")
            print("============================")
            break

        if tries >= max_tries:
            print(f"ゲームオーバー！答えは {secret} でした。")
            break