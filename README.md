# earthquakeDBsGenerator
Various earthquake databases generator(s)

### Requirements
- `python3` (with `pandas` library; can be installed by running `pip install pandas`)
- `wget`
- `head`, `tails` and `sed`

The scripts were teste in `Cygwin` runtime environment running on Windows 10.

### File format
Each script will generate a `.csv` file with the following header: **Year, Month, Day, Hour, Minute, Second, Latitude, Longitude, Depth, Magnitude**
