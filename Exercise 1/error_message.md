# Error Message

## Script 1
- **Error Name:** `SyntaxError: '(' was never closed`
- **Cause:** Line 1 was missing a closing parenthesis `)` at the end of `print("This is a simple test"`.
- **Fix:** Added the missing closing parenthesis `)` to properly end the print statement.

## Script 2
- **Error Name:** `NameError: name 'gravitational_acceleration' is not defined`
- **Cause:** The script attempts to multiply `mass_in_kg` by `gravitational_acceleration`, but the variable was never initialized or assigned a value.
- **Fix:** Declared and assigned a value to `gravitational_acceleration = 9.81` before performing the calculation.

## Script 3
- **Error Name:** `ModuleNotFoundError: No module named 'Math'`
- **Cause:** Python module names are case-sensitive. The script tried to import from `Math` with a capital 'M', but the standard library module is spelled `math`.
- **Fix:** Corrected the import statement to use lowercase: `from math import sqrt`.

## Script 4
- **Error Name:** `SyntaxError: Missing parentheses in call to 'print'`
- **Cause:** The script used Python 2 syntax (`print "text"`), which lacks parentheses. Python 3 treats `print()` as a function and requires parentheses.
- **Fix:** Added parentheses around the string: `print("Let's run some legacy code...")`.

## Script 5
- **Error Name:** `TypeError: can't multiply sequence by non-int of type 'float'`
- **Cause:** The script attempted to multiply a string by a floating-point number (`3.`) instead of a whole integer. 
- **Fix:** Changed the multiplier from a float (`3.`) to an integer (`3`).

## Script 6
- **Error Name:** `IndentationError: unindent does not match any outer indentation level`
- **Cause:** The `else:` statement was indented with 2 spaces instead of matching the indentation level of the corresponding `if:` statement (4 spaces).
- **Fix:** Corrected the spacing so that both `if:` and `else:` statements align at the same indentation level.

## Script 7
- **Error Name:** `SyntaxError: invalid syntax`
- **Cause:** The `while` statement was missing a colon (`:`) at the end of the header line, and the subsequent code was merged onto the same line without proper indentation.
- **Fix:** Added the missing colon `:` at the end of the `while` loop condition and formatted the loop body and ending print statement on separate, properly indented lines.