# COVID-19 Statistics

Fork of PEDEL-CODE/Covid-Tracker from commit `#872381b`.
This version is the CLI version and does not include Tkinter GUI from later upstream commits (`#d8cc80c`).

Changes in the initial fork:

- The messages shown to the user were updated to be more friendly.
- Multiple countries can be viewed within a single program run.

Later changes (21 May 2021, version 2.0):

- Added aliases for US and UK (workaround for issue #1)
- Fix bad indentation (PYL-W0311) (issue #6)
- Optimised if statement (now uses in as per PYL-R1714/issue #5)
- Improved spacing for readability
- Changed how the option for viewing further countries data works:
  - More variations of Y/yes accepted
  - All other input will end program
- Removed .bat method of running program

# Prerequisites
- Requires Python 3.6 or above, `>=3.9.2` preferred and installed in PATH
- Install requirements.txt via `pip`

# Download & run
1. Download repo using `git clone https://github.com/NDavies-02/COVID-19-Tracker.git`
2. `pip install -r requirements.txt`
3. `python3 ./'COVID-19 Tracker.py'`