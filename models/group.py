class Group():

  def __init__(self, id, data):
    self.id = id
    self.name = data['name']
    self.teams = []


  def set_team(self, team):
    self.teams.append(team)
