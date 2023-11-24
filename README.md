# Note
I was lost after reading through the basics of SPICE from [SPICE tutorials](https://naif.jpl.nasa.gov/naif/tutorials.html). I wanted practical tutorials, but spiceypy (basically a 2017 version of [SPICE lessons](https://naif.jpl.nasa.gov/naif/lessons.html)) did not fulfill my needs.

Then I found [``Space Science Tutorial`` repo by Thomas Albin](https://github.com/ThomasAlbin/SpaceScienceTutorial) to be extremely helpful, so I decided to learn them by myself. I changed multiple code lines to my taste & performance issues, so this repo is a "*summarized version of the original material, for intermediate-level python users who have basic knowledge of space science.*"
* If you are a beginner in python, I think their original materials and exhaustive "medium" articles will be great learning materials for you.

1. Part 01: Basics of spiceypy
1. Part 02: Movement of the Solar System Barycenter (SSB, id=1) over time with respect to the Sun.
1. Part 03: SSB-planet distance for Giant planets, find correlation between SSB-Sun-planet angle (Jupiter governs the SSB location)
1. Part 04: A practice to find an "observable window" (using the phase angles of [Sun, Earth, Venus, Moon])
1. Part 05: A practice to plot [Sun, Venus, Mars, Moon] on the Ecliptic and Equatorial Coordinates (aitoff)
1. Part 06: Calculating the "state vectors", orbital elements, conversion matrix between reference frames (``ECLIPJ2000``), and orbit of an NEO.
1. *(Part 07: Merged into Part 08)*
1. Part 08: Query the IAUMPC comets DB, add some info, and save as a SQL DB
1. *(Part 09: Omitted because it's a simple visualization that can be fun for students)*
1. Part 10: A practice to calculate the T_Jup parameter in e-i space for different a, make a GIF.
1. *(Part 11: Omitted because it's a simple visualization that can be fun for students)*
1. *(Part 12: Omitted because it's a simple visualization that can b fun for students)*
1. Part 13: 67P orbital (osculating) elements calculation near Jupiter encounter, compare with IAUMPC.
1. Part 14: Finding close-approach time by ``gfdist`` and simple note on the "insufficient ephemeris" error.


Later, I may try looking into their youtube materials and merging them here.

GitHub: https://github.com/ThomasAlbin/Astroniz-YT-Tutorials