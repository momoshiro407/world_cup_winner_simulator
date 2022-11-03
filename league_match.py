from match_result import run_match_result
import random


TEAM_COUNT = 4 # 1グループ内のチーム数
PASSED_LIMIT = 2 # 勝ち上がり可能なチーム数


def run_league_matches(groups):
  """ グループ毎にリーグ戦を実行し通過チームのリストを返す """

  passed_teams = [] # 各グループを通過したチームのリスト

  for group in groups:
    teams = group.teams
    for i in range(TEAM_COUNT - 1):
      for j in range(1, TEAM_COUNT - i):
          point_1, point_2 = run_match_result(teams[i], teams[i + j])
          # 勝点を更新
          teams[i].update_points(point_1)
          teams[i + j].update_points(point_2)

    # 勝点の降順でチームを並び替える
    sorted_teams = list(sorted(teams, key=lambda t: t.points, reverse=True))

    # 各チームを対戦成績の降順に並べ上2つを通過チームとする
    each_passed_teams = []
    for team in sorted_teams:
      same_points_teams = list(
          filter(lambda t: t.points == team.points, sorted_teams))

      if len(same_points_teams) == 1:
        # 勝点の重複なし
        each_passed_teams.append(team)
      elif len(same_points_teams) == 2:
        # 2チームの勝点が同じ場合は直接対決の結果で判定
        # 0番のチームが1番のチームと対戦した時の結果を参照する
        result = list(
            filter(lambda hist: hist[0] == same_points_teams[1].id, same_points_teams[0].match_history))[0][2]
        if result == 3:
          each_passed_teams.append(same_points_teams[0])
          if len(each_passed_teams) == PASSED_LIMIT:
            break
          each_passed_teams.append(same_points_teams[1])
        elif result == 0:
          each_passed_teams.append(same_points_teams[1])
          if len(each_passed_teams) == PASSED_LIMIT:
            break
          each_passed_teams.append(same_points_teams[0])
        else:
          # 直接対決が引き分けなので抽選で決める
          for t in random.sample(same_points_teams, PASSED_LIMIT - len(each_passed_teams)):
            each_passed_teams.append(t)
      else:
        # 3チーム以上の勝点が同じ場合は抽選で決める
        for t in random.sample(same_points_teams, PASSED_LIMIT - len(each_passed_teams)):
          each_passed_teams.append(t)

      if len(each_passed_teams) == PASSED_LIMIT:
        break

    passed_teams.append(each_passed_teams)

  return passed_teams
