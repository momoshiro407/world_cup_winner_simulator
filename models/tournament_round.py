class TournamentRound():

  def __init__(self, i, teams):
    self.round_numbner = i
    self.teams = teams
    self.winner_teams = []


  def append_winner_team(self, team):
    self.winner_teams.append(team)
