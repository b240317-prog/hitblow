"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret


def play(digits=3):
    secret = make_secret(digits)
    max_tries = 15
    print(f"Hit & Blow（{digits} 桁・重複なし）")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====

    print(f"解答可能回数は{max_tries}回です．")

    tries = 0
    while True:
        guess = input("予想 > ").strip()

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue

        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")

        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break

# 挑戦回数が最大回数の半分(0.5)以上になったらヒントを表示
        if tries / max_tries >= 0.5:
            # guess と secret は文字列(str)として扱われているため、数値(int)に変換して大小を比較
            if int(guess) > int(secret):
                print("【ヒント】正解は入力した数字よりも「小さい」です")
            elif int(guess) < int(secret):
                print("【ヒント】正解は入力した数字よりも「大きい」です")

        if tries >= max_tries:
            print(f"ゲームオーバー！答えは {secret} でした。")
            break
