# Spreadsheet exports

Example tool file. What was learned reading exports from spreadsheets and from the invoicing software, made by the client. To read before using an export as the source of a send or a count.

## Mistakes not to repeat

- **2026-10-01** An amount written as "1.250,00" was read as 1.25, because the file uses the dot for thousands and the comma for decimals. Cause: the column was read as plain numbers. Instead: read the amount columns as text first, convert them on purpose, and compare the total with the one the client gives.
- **2026-10-01** A client with three overdue invoices appeared as three separate people in the first count. Cause: the export has one row per invoice, not per client. Instead: say which of the two you are counting ("64 invoices", "41 clients") every time you give a number.
- **2026-10-01** Some email addresses had a space at the end, and the check for a valid address failed on them. Cause: the export pads the cells. Instead: trim every text column before using it.

## Ways of working that hold up

- **2026-10-01** Before using the file, ask the person for the number they expect (rows, total amount) and compare it with what you read. Holds when: the export was made by someone else and nobody has counted it yet.
- **2026-10-01** Work on a copy of the file, in the project's `materials/` folder, and leave the original as it was received. Holds when: the export will be requested again next month.

## Verified limits

- **2026-10-01** The export from the invoicing software cannot be filtered by due date before it is downloaded: the filter has to be applied on the copy. Verified on the September export.
