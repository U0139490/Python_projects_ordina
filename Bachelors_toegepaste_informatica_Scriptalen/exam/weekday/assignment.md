# Assignment

`input.txt` contains a list of names and corresponding birthdays.
These birthdays are written using the `yyyy-mm-dd` format.
We wish to know the weekday of each birthday, i.e., we wish to know if someone was born on a Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.

Write a script that determines the weekday of each birthday and write the results to `output.txt`.
Each line should contain the name (an identical copy to what appears in `input.txt`) followed by a space, followed by the weekday.

## Example

If `input.txt` contains

```text
Aaron Wood 1965-10-11
Abigail Mitchell 1950-01-18
Abigail Thomas 1968-02-11
Adam Ashley 1986-11-26
Adam Gray 1969-06-29
Adam Martin 1979-08-21
Adam Thomas 1967-07-09
Adrian Cortez 1950-05-07
Adrian Frazier 1963-11-21
Adriana Lee 2000-11-20
```

then your script should produce a file `output.txt` with contents

```text
Aaron Wood Monday
Abigail Mitchell Wednesday
Abigail Thomas Sunday
Adam Ashley Wednesday
Adam Gray Sunday
Adam Martin Tuesday
Adam Thomas Sunday
Adrian Cortez Sunday
Adrian Frazier Thursday
Adriana Lee Monday
```
