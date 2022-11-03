class Team():

  def __init__(self, id, data):
    self.id = id
    self.name = data['name']
    self.rate = data['rate']
    self.points = 0
    self.match_history = []


  def update_points(self, point):
    self.points += point

  def update_match_history(self, opponent_id, winning_percentage, p_draw, result):
    self.match_history.append([opponent_id, winning_percentage, p_draw, result])

  def clear_results(self):
    self.points = 0
    self.match_history = []