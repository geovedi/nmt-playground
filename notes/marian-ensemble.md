

See this thread: https://groups.google.com/forum/#!topic/amunmt/s7-5bCMCCMU

Just to summarize...

From my individual models that can give best 0.585 score,

    In [2]: scores = np.loadtxt('valid.en.id.scores')

    In [3]: for m in range(scores.shape[1]):
       ...:     print((m, np.sum(scores[:, m]) / scores.shape[0]))
       ...:
    (0, 0.58139409095400008)
    (1, 0.58113062415000005)
    (2, 0.57934818018799994)
    (3, 0.58508210277399997)
    (4, 0.56612870015400008)

I was naively hoping to get ~0.65 at minimal cost.

    In [4]: np.sum(np.amax(scores, axis=1)) / scores.shape[0]
    Out[4]: 0.65638549081399999

Turned out after some bruteforce searches to find best weight for each model in ensemble mode, I can get 0.648525.

    ...
    ensemble/fae5f55a-4e15-11e7-8f84-4ccc6a99dbea.out  0.64828
    ensemble/36a44b4c-4e15-11e7-8f84-4ccc6a99dbea.out  0.648325
    ensemble/c2678120-4e0c-11e7-8f84-4ccc6a99dbea.out  0.648418
    ensemble/392ea01a-4e0b-11e7-8f84-4ccc6a99dbea.out  0.648499
    ensemble/976e6e12-4e1a-11e7-8f84-4ccc6a99dbea.out  0.648525

And yes, that improvement given by ensemble method comes with a significant cost on system usage.
