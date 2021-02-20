from tictactoe import BaseBoard


def string_replacer(origin_str: str, location: int, replace_with: str):
    return origin_str[:location] + replace_with + origin_str[location + 1 :]


def minimax(current_game: BaseBoard, maximized: bool):
    offset = 1 if maximized else -1

    if current_game.game_result() == "Draw":
        return None, 0
    if current_game.game_result() == current_game.current_player:
        return None, 10 * offset
    if current_game.game_result() == current_game.opponent:
        return None, -10 * offset

    best_move = None
    best_score = -100 * offset
    for spot in current_game.empty_cells():
        moved = string_replacer(repr(current_game), spot, current_game.current_player)
        score = minimax(BaseBoard(moved), not maximized)[1]
        if score == 10 * offset:
            return spot, score
        if (score > best_score and maximized) or (not maximized and score < best_score):
            best_score = score
            best_move = spot
    return best_move, best_score


a = "O_XX_X__O"
out = minimax(BaseBoard(a), True)
print(out)
