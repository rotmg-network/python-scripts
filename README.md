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

## asset_extracter.py
### Extract all tiles and objects from Exalt

This script will autimatically grab all the tiles and objects from the resource.assets

For this to work, you need to put the resource.assets into the same directory as the script and it will dump them into there own xmls called tiles.xml and objects.xml

## metadataheader_extracter.py
### Unscrambles a decrypted metadataheader for Exalt

This script will take a scrambled metadataheader and reorder it so it works with automated tools like il2cppdumper and melonloader

For this to work you need to get a decrypted metadataheader from the global-metadata.dat.

Inorder to do this you can manually grab it from x64dbg from the  a function that returns the decrypted header which is found in il2cpp::vm::MetadataCache::Initialize. refer to this article https://katyscode.wordpress.com/2021/02/23/il2cpp-finding-obfuscated-global-metadata/. copy paste the header in an other file using some hex editor, and run the script with the file in the same directory, it will output a resolved header which you can paste into the begginig of the encrypted global-metadata.dat
  
### More coming soon...