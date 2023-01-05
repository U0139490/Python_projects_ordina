# Assignment

`catalog.json` contains book prices:

* The keys are ISBN-13 codes, which uniquely identifies each book.
* The values are the price of the book.

`orders.json` contains orders.
Each order has a credit card number and a list of ISBN-13 codes, which are the books that were bought in that order.

We ask you to determine how much each credit card should be charged.
In other words: for each credit card number you need to determine which books were ordered, determine their price and compute the sum.
Note that the same credit card number can appear in multiple orders!

Output the results to `output.txt`:

* Each line should be formatted "CREDIT_CARD_NUMBER TOTAL_AMOUNT", e.g., `060400840751 13426`, which means that the credit card with number 060400840751 should be chared 13426 euros.
* The lines should be ordered by credit card number. Important: sort the credit card numbers as strings, i.e., do NOT convert them to integers first.

## Example

Say `catalog.json` contains

```json
{
    "1": 100,
    "2": 200,
    "3": 300
}
```

`orders.json` contains

```json
[
    {
        "credit_card": "111",
        "items": [
            "1",
            "2"
        ]
    },
    {
        "credit_card": "222",
        "items": [
            "1"
        ]
    },
    {
        "credit_card": "111",
        "items": [
            "3"
        ]
    },
]
```

`output.txt` should then contain

```text
111 600
222 100
```
