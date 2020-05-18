# Not Be Foooled

How to not be foooled? Here is the answer!

## Problem Description

The challenge is asking you for an anomalous curve that cannot be exploited by the Smart attack.


## Solution

1. Generate an anomalous curve.

2. Check if the curve can be exploited by Smart attack. One way to check is to lift the curve, choose a random point P, and check if p * P == 0.


There is a paper about how to generate anomalous curve (http://www.monnerat.info/publications/anomalous.pdf).
Note that this is just *one* possible way to generate *some* anamalous curves.

Inspired by https://crypto.stackexchange.com/questions/70454/why-smarts-attack-doesnt-work-on-this-ecdlp?rq=1, and the original Smart attack's paper, to make the generated curve immune to Smart attack, you can move the generated curve around while keeping the order unchanged. The easiest way is to use `D = 3`, under which `j = 0`, and you will notice that `a = 0` and `b = 0` according to equation (3) and (4) in the above paper. In this case, if we change the value of `b`, the order of the curve doesn't change, yet the lifted curve will be equivalent to change to $y^2 = x^3 + 0 * x + (0 + p * b')$.

So to solve this, all we need to do is to generated a random prime above the threshold, fix a to 0, and enumerate b.

Note that this is not the only solution. There are so many elliptic curves satisfying this property. If you have a way to compute the complete set, please let me know. :)

```python
def find_safe_curve(p):
    for b in xsrange(1, p):
        if b % 10 ** 4 == 0:
            print("Testing..., b = %d" % b)
        E = EllipticCurve(GF(p), [0, b])
          if E.order() == p:
              print("order is satisfied!")
              if test_safe(E, p, b):
                  print("Find Safe Anomalous Curve")
                  yield (E, b)
```

## Another Intersting Solution

https://hxp.io/blog/72/DEFCON-CTF-Quals-2020-notbefoooled/
