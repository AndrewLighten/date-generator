## Date generator

This is a trivial little utility that will generate a list of dates for the current calendar year.

It creates a file named `YYYY-Calendar.md` in the current directory. The file contains the date of each day of the year, in Obsidian's page link format (i.e., `[[...]]`).

It also:
- Includes a heading for each month
- Inserts a blank line before each Monday, so weeks are visually separated

Here's an example:

```
## January

[[2023-01-01-Sun]]

[[2023-01-02-Mon]]
[[2023-01-03-Tue]]
[[2023-01-04-Wed]]
[[2023-01-05-Thu]]
[[2023-01-06-Fri]]
[[2023-01-07-Sat]]
[[2023-01-08-Sun]]

[[2023-01-09-Mon]]
[[2023-01-10-Tue]]
[[2023-01-11-Wed]]
[[2023-01-12-Thu]]
[[2023-01-13-Fri]]
```

I wrote this because I always include the day of the week in a timestamp used in my daily notes, and when I'm referring to a future note I need to know what the day of the week is.