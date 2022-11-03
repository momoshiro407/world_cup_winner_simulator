import csv
import os


# 各種出力ファイルのパス
group_info_path = './result/group_information.csv'
league_match_result_path = './result/league_match_result.csv'
tournament_result_path = './result/tournament_result.csv'
match_history_path = './result/match_history.csv'


def output_group_info(groups):
  """ グループ、所属チームの情報をCSV形式で出力する """

  with open(group_info_path, 'w') as f:
    writer = csv.writer(f)

    for group in groups:
      for team in group.teams:
        writer.writerow([team.id, group.id,  team.name, team.rate]) # チームID, グループID, チーム名, レート


def output_leagu_match_result(i, groups):
  """ 各グループのリーグ戦の結果をCSV形式で出力する """

  with open(league_match_result_path, 'a') as f:
    writer = csv.writer(f)

    writer.writerow([i]) # 試行回数
    for group in groups:
      print('\n' + group.name)
      for team in group.teams:
        print('{0:5d} {1:15} {2:5d}'.format(team.id, team.name, team.points))
        writer.writerow([group.id, team.id, team.points])  # グループID, チームID, 勝点

    f.write('\n')


def output_tournament_result(i, rounds):
  """  トーナメント戦の結果をCSV形式で出力する """

  with open(tournament_result_path, 'a') as f:
    writer = csv.writer(f)

    writer.writerow([i]) # 試行回数
    for round in rounds:
      print([team.id for team in round.teams])
      writer.writerow([team.id for team in round.teams])  # 各ラウンドにいるチーム

    print([rounds[-1].winner_teams[0].id])
    writer.writerow([rounds[-1].winner_teams[0].id])  # 優勝チーム

    f.write('\n')


def output_match_history_result(i, groups):
  """ チーム別の対戦成績をCSV形式で出力する """

  with open(match_history_path, 'a') as f:
    writer = csv.writer(f)

    writer.writerow([i]) # 試行回数
    for group in groups:
      for team in group.teams:
        output = [team.id] + list([x for row in team.match_history for x in row])
        writer.writerow(output)

    f.write('\n')


def remove_result_files():
  """ 各種結果出力ファイルを削除する """

  if os.path.isfile(league_match_result_path):
    os.remove(league_match_result_path)
  if os.path.isfile(tournament_result_path):
    os.remove(tournament_result_path)
  if os.path.isfile(match_history_path):
    os.remove(match_history_path)
