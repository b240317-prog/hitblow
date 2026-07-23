def calculate_score(digits, tries, elapsed):
    score = int((digits**3 * 1000) / (tries + elapsed / 10))
    return max(score, 0)


def format_time(elapsed):
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    centiseconds = int((elapsed % 1) * 100)
    return f"{minutes:02d}:{seconds:02d}.{centiseconds:02d}"