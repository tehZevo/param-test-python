from param_test import param_test
import pprint

options = {
  "foo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  "bar": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

def tester(params):
  #score is negative distance to 25
  return -abs(25 - params["foo"] * params["bar"])

results = param_test(options, tester, 100000)

#sort descending by score
results.sort(key=lambda x: x["score"], reverse=True)

#calculate averages by parameter:
optionScores = {};

for option in options.keys():
  optionScores[option] = {};
  for value in options[option]:
    score = 0;
    numScores = 0;

    for result in results:
      if option in result["params"] and result["params"][option] == value:
        score += result["score"]
        numScores += 1

    score /= numScores
    optionScores[option][value] = score

#print(results)
pprint.pprint(optionScores)
