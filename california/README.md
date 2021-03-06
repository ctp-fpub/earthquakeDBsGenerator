# SOUTHERN CALIFORNIA EARTHQUAKE DATA CENTER CATALOG FORMAT 
      

The SCEDC catalog consists of hypocentral information for 1932 through
the present. For information on catalog completeness and data sources, 
see http://www.data.scec.org/about/data_avail.htm.

SCEDC-format catalog data (described below) are stored in yearly 
ASCII *.catalog files.

## SCEDC CATALOG FORMAT specification (revised 06/17/03)

	col len format name	comment
	--- --- ------ ----	-------
	 1  10   a10   date	YYYY/MM/DD
	12  11   a11   time	HH:mm:SS:ss (UTC time--
					     7 hours ahead of Pacific Daylight Time
					     8 hours ahead of Pacific Standard Time)
	24   2    a2   eventtype event type
					local (le)
					regional (re)
					teleseism (ts)
					quarry blast (qb)
					sonic boom (sn)
                                        nuclear blast (nt)
                                        unknown event (uk)
	27   4   f4.2  magnitude
	32   1    a1   magtype	type of magnitude
					'e'	energy magnitude
					'w'	moment magnitude
					'b'	body-wave magnitude
					's'	surface-wave magnitude
					'l'	local (WOOD-ANDERSON) magnitude
					'c'	coda amplitude 
					'h'	helicorder magnitude (short-period Benioff)
					'd'	coda duration magnitude
					'n'	no magnitude
        36   7   f7.3  lat      decimal degrees  
        44   8   f8.3  lon	decimal degrees
	53   5   f5.1  depth	kilometers
	59   1    a1   quality  location quality
					'A' +- 1 km horizontal distance
					    +- 2 km depth
					'B' +- 2 km horizontal distance	
					    +- 5 km depth
					'C' +- 5 km horizontal distance
					    no depth restriction
					'D' >+- 5 km horizontal distance 
					'Z'  no quality listed in database
	61   8    a8   eventid  event ID
	70   3	  i3   nph	number of picked phases
	75   4    i4   ngrams   number of grams
                                           (i.e. # of station traces)
