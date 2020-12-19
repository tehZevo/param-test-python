import random

def choose_params(options):
  params = {}
  for k, r in options.items():
    params[k] = random.choice(r)
  return params

def param_test(param_options, test_func, count=1):
  results = [];

  for i in range(count):
    params = choose_params(param_options)
    score = test_func(params)
    results.append({"params":params, "score":score})

  return results
