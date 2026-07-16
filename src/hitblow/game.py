from .core import judge, make_secret


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

    tries = 0
    while True:
        guess = input("予想 > ").strip()

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue

        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====

        if hit == digits:
            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break

        if tries >= max_tries:
            print(f"ゲームオーバー！答えは {secret} でした。")
            break