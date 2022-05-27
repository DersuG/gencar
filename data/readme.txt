The .cst file stands for Comma Separated Table.

The format is basically a .csv with extra features. Mainly:
- The first two rows are header rows and are required.
  - The first row contains the column names.
  - The second row contains the column data types.
    - Valid types include bool, int, string, and float.
    - Rows can't mix types.
- Columns are strictly typed.
  - Bools are like `true` or `false`.
  - Ints are like `5` or `-36`.
  - Strings are like `"wow"` or `"Hello, world!"`.
  - Floats are like `0.533` or `-22.22`.