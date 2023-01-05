# Assignment

We're playing Quordle, which is the same as Wordle.
The rules are not important for this questions, so we won't bother explaining them here.

You are given a list of words in `words.txt`.
We are looking for 5 words who together have the most distinct letters.

Say, for example, that `words.txt` contains the following words:

```text
STAKE
STARE
STEAK
STALE
RATES
BLAZE
QUARK
CHIMP
SNOWY
FUDGE
```

Say we pick STAKE, STARE, STEAK, STALE and RATES.
Together these words contain the letters A, E, K, L, R, S and T.
In other words, these words are built out of seven distinct letters.

However, if we were to pick BLAZE, CHIMP, FUDGE, QUARK and SNOWY, we use the letters A, B, C, D, E, F, G, H, I, K, L, M, N, O, P, Q, R, S, U, W, Y and Z, or 22 in total.
There is no better selection of five words: no combination uses more than 22 distinct letters.

Your script should find the selection of five words that maximizes the number of distinct letters and write these five words to `output.txt`, one word per line in alphabetical order.
We guarantee these is only one possible such selection of words.

## Example

If `words.txt` contains

```text
STAKE
STARE
STEAK
STALE
RATES
BLAZE
QUARK
CHIMP
SNOWY
FUDGE
```

then the following `output.txt` should be produced:

```text
BLAZE
CHIMP
FUDGE
QUARK
SNOWY
```

## Hints

* Check out `itertools` as it contains a function that takes care of the most difficult part of this question.
* Finding the optimal five words could take a few minutes, depending on how powerful your machine is.
  Take this into account while solving this exercise.
