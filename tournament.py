from models.tournament_round import TournamentRound
from numpy import random
from match_result import run_match_result


TOTAL_ROUNDS = 4 # トーナメント戦の総回戦数


def run_tournament(teams):
  """ トーナメント戦を実行し、結果から生成したTournamentRoundオブジェクトのリストを返す """

  rounds = []  # TournamentRoundオブジェクトのリスト
  winner_teams = teams

  for i in range(TOTAL_ROUNDS):
    round = TournamentRound(i + 1, winner_teams)

    # ラウンド内の試合数
    total_matches = int(len(round.teams) / 2)
    for j in range(total_matches):
      team_1 = round.teams[j * 2]
      team_2 = round.teams[j * 2 + 1]
      point_1, point_2 = run_match_result(team_1, team_2)
      print('{0:15} {1:3d} / {2:15} {3:3d}'.format(team_1.name, point_1, team_2.name, point_2))

      winner = None
      if point_1 == 1 and point_2 == 1:
        # PK戦(勝敗50%)で勝ち上がりチームを決定する
        winner = random.choice(a=[team_1, team_2], size=1, p=[0.5, 0.5])[0]
        print('PK match winner: ', winner.name)
      else:
        # 勝点3が返ってきたチームを勝ち上がりとする
        winner = team_1 if point_1 == 3 else team_2

      round.append_winner_team(winner)

    rounds.append(round)
    winner_teams = round.winner_teams

  return rounds
