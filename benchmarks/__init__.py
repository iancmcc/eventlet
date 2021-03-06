import gc
import timeit
import random
    
def measure_best(repeat, iters, 
                 common_setup='pass', 
                 common_cleanup='pass',
                 *funcs):
    funcs = list(funcs)
    results = dict([(f,[]) for f in funcs])

    for i in xrange(repeat):
        random.shuffle(funcs)
        for func in funcs:
            gc.collect()
            t = timeit.Timer(func, setup=common_setup)
            results[func].append(t.timeit(iters))
            common_cleanup()
    
    best_results = {}
    for func, times in results.iteritems():
        best_results[func] = min(times)
    return best_results
    