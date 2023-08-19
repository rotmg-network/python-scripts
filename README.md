# RotMG Python Scripts
### Miscellaneous small python scripts for Realm of the Mad God.  

These scripts are all too small to be their own full projects so are designed to
run from just a single file.  
  
Contact me on Discord at *him#0001* or open an issue if you have any problems.

## packet_names.py
### Extract all incoming, outgoing and data packet names from Exalt.

This script will automatically grab all packet names from the client and optionally write them to .txt files based on direction (incoming/outgoing).  
  
For this to work, you need a dump of all MonoScript files for the current game version. You can get these by extracting them from the `globalgamemanagers.assets` file using the tool Unity Asset Bundle Extractor (UABE).  The file can be found in your Documents folder, inside `RealmOfTheMadGod\Production\RotMG Exalt_Data`.  
  
Simply extract all MonoScript assets as raw files and put them inside the `monoscript` folder. If you want to use another folder, you can change the target in the script.  

Once packet names are found, the script will ask if you would like to output to files. These will be "incoming_packets" and "outgoing_packets" text files with the date the script was ran appended to the end.

Run the script with `python packet_names.py` and you're done!
  
### More coming soon...