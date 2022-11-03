from numpy import random

# 引き分けの確率を計算する時の係数
DRAW_GRADIENT = -0.00045
DRAW_INTERCEPT = 0.316


def calc_winning_percentage(r1, r2):
  """ 対戦チーム同士のレート差から第1引数側のチームの勝利確率を計算する """

  return 1 / (10 ** ((r2 - r1) / 400) + 1)


def calc_draw_percentage(r1, r2):
  """ 対戦チーム同士のレート差から引き分けの確率を計算する """

  diff = abs(r1 - r2)
  p_draw = DRAW_GRADIENT * diff + DRAW_INTERCEPT

  return p_draw


def lottery(percentage_list):
  """ 与えられた確率に基づき抽選を行う """

  # 負: 0, 分: 1, 勝: 3
  result_list = [3, 1, 0]
  point = random.choice(a=result_list, size=1, p=percentage_list)[0]
  
  if point == 1:
    return point, point
  else:
    return point, 3 - point


def run_match_result(team1, team2):
  """ 対戦2チームの勝敗を計算し勝点の結果を返す """
  
  # team1, 2の勝利確率を計算する(引き分け未考慮)
  p_win_1 = calc_winning_percentage(team1.rate, team2.rate)
  p_win_2 = 1 - p_win_1
  p_win_lower = min(p_win_1, p_win_2)
  # 引き分けの確率(候補)を計算する
  p_draw_candidate = calc_draw_percentage(team1.rate, team2.rate)
  # 「弱い方の勝利確率 <= p_draw / 2」となってしまう場合「p_draw = 弱い方の勝利確率」とする
  p_draw = p_win_lower if p_win_lower <= p_draw_candidate / 2 else p_draw_candidate
  # team1, 2の勝利確率を更新する(引き分け考慮)
  p_win_1 -= p_draw / 2
  p_win_2 -= p_draw / 2

  # 勝分負の抽選
  point_1, point_2 = lottery([p_win_1, p_draw, p_win_2])

  # 対戦履歴の更新
  team1.update_match_history(team2.id, p_win_1, p_draw, point_1)
  team2.update_match_history(team1.id, p_win_2, p_draw, point_2)

  return point_1, point_2
