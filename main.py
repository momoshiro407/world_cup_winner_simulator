from team_entry import set_teams_to_group
from league_match import run_league_matches
from tournament import run_tournament
from file_controller import output_group_info, output_leagu_match_result,\
  output_match_history_result, output_tournament_result, remove_result_files
from datetime import datetime


def main():
  # 予選グループ、チーム情報を格納
  groups = set_teams_to_group()
  # 予選グループ、チーム情報の出力
  output_group_info(groups)


  trials = 1  # 試行回数

  while True:
    try:
      trials = int(input('試行回数を入力してください。(1〜1000の整数値):'))
      break
    except ValueError:
      print('不正な数値です。')

  while True:
    confirmation = input('シミュレーションを開始しますか？(開始:y):')
    if confirmation == 'y':
      break
  
  # 出力ファイルの削除
  remove_result_files()

  # 処理開始
  start_time = datetime.now()

  for i in range(1, trials + 1):
    # 【リーグ戦】を実施
    passed_teams = run_league_matches(groups)
    # リーグ戦の結果を出力する
    output_leagu_match_result(i, groups)

    # 通過チームをトーナメント第1回戦のブロックに振り分ける
    first_round_teams = []
    for j in range(2):
      for k, teams in enumerate(passed_teams):
        first_round_teams.append(teams[(k + j) % 2])

    # 【決勝トーナメント戦】を実施
    rounds = run_tournament(first_round_teams)
    # 決勝トーナメント戦の結果を出力する
    output_tournament_result(i, rounds)
    print('\n')
    print('WINNER:', rounds[len(rounds) - 1].winner_teams[0].name)

    # チーム毎の全対戦履歴を出力する
    output_match_history_result(i, groups)

    # チーム成績のクリア
    for group in groups:
      for team in group.teams:
        team.clear_results()


  # 完了までの経過時間の出力
  print('\n---- Processing time ----')
  print(datetime.now() - start_time)


if __name__ == '__main__':
  main()
