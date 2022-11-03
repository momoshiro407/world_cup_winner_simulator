import json
from models.team import Team
from models.group import Group


def set_teams_to_group():
  """ グループ、チームの情報を読み込みGroup、Teamオブジェクトを返す """

  # チーム情報のjsonを読み込む
  with open('./data/groups_teams.json', 'r') as f:
    data = json.load(f)

  groups = []
  team_id = 1

  for i, group_data in enumerate(data['groups']):
    # グループオブジェクトを生成する
    group = Group(i + 1, group_data)

    for team_data in group_data['teams']:
      # チームオブジェクトを生成しグループに格納する
      group.set_team(Team(team_id, team_data))
      team_id += 1

    print('\n', group.name)
    [print('{0:2d} {1:15} {2:4d}'.format(t.id, t.name, t.rate)) for t in group.teams]

    groups.append(group)

  return groups
