import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

fig, ax = plt.subplots()

#print(aaron_judge.columns)
#print(aaron_judge.description.unique())
#print(aaron_judge.type.unique())

def baseballclassifier(player):
  player['type'] = player['type'].map({'S':1, 'B':0})
  #print(player.type)

  #print(player['plate_x'])

  player = player.dropna(subset = ['plate_x', 'plate_z', 'type'])

  plt.scatter(x = player['plate_x'], y = player['plate_z'], c = player['type'], cmap = plt.cm.coolwarm, alpha = 0.25)

  training_set, validation_set = train_test_split(player, random_state = 1)
  classifier = SVC(kernel = 'rbf', gamma = 3, C = 1)
  classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])

  draw_boundary(ax, classifier)
  ax.set_ylim(-2, 6)
  ax.set_xlim(-3, 3)
  plt.show()

  print(classifier.score(validation_set[['plate_x', 'plate_z']], validation_set['type']))

  return None

baseballclassifier(aaron_judge)
baseballclassifier(jose_altuve)
baseballclassifier(david_ortiz)
