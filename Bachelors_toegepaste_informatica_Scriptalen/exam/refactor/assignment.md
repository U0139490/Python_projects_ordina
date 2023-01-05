# Assignment

Each programming language has its own naming conventions.
It is important to adhere to these, as it improves readability and consistency.
Many companies enforce these rules: not following the agreed upon conventions will lead to a bad code review.

Examples of naming conventions are

* Camel case, where an identifier can contain multiple words, each of them capitalized.
  For example, `BankAccount`, `SaveCommand`, or `InternalFrameInternalFrameTitlePaneInternalFrameTitlePaneMaximizeButtonWindowNotFocusedState` (sadly this is not a fictional example.)
* Snake case, where all letters are lowercase and words are separated by underscores.
  For example, `bank_account`, `save_command` or `internal_frame_internal_frame_title_pane_internal_frame_title_pane_maximize_button_window_not_focused_state`.

In the Python world, classes should follow Camel case, whereas functions/methods should follow the snake case convention.
You are given a file `input.txt` that contains Python code, but where the naming conventions have been reversed: classes are in snake case, methods in camel case.

Write a script that fixes these mistakes and writes its results to `output.txt`.

## Example

```python
class draghidg_rso_steuphugreu_drai:
    def SmaCkouflesl():
        ...

    def CkaplMpoursSmaidg():
        ...

    def NgigroumpNgouPnaiclRkey():
        ...

    def RkaighaiBlarsouBlaupr():
        ...

    def BloumbaiFlSnFlirku():
        ...
```

should be fixed to

```python
class DraghidgRsoSteuphugreuDrai:
    def sma_ckouflesl():
        ...

    def ckapl_mpours_smaidg():
        ...

    def ngigroump_ngou_pnaicl_rkey():
        ...

    def rkaighai_blarsou_blaupr():
        ...

    def bloumbai_fl_sn_flirku():
        ...
```
