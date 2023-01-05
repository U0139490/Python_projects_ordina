# Assignment

You are given a file named `input.txt`.
We want you to replace all long words (counting at least 8 letters) by an abbreviation which is constructed as follows:

* The first and last letters are preserved.
* The letters in between are replaced by their count.

For example, take `internationalization`.
This word counts `20` letters and is abbreviated `i18n`.

Write the results to `output.txt`.

Extra details:

* A word is a sequence of letters. You can assume all letters are lowercase.
* `input.txt` contains punctuation, i.e., commas and periods. These are not considered as being a part of a word.
* `output.txt` must be identical to `input.txt`, except for the long words being replaced by their abbreviation.

## Example

The file `input.txt`

```text
longword short
comma, and dot. must be preserved and are not part of word
letters, has only 7 letters. and therefore should not be abbreviated.
```

should result in the following `output.txt`:

```text
l6d short
comma, and dot. must be p7d and are not part of word
letters, has only 7 letters. and t7e should not be a9d.
```
