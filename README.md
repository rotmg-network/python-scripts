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

## global_metadata_fix.py
### Fixes global-metadata.dat for Exalt 

This script will take a encrypted metadataheader and decrypt + reorder it so it works with automated tools like il2cppdumper and melonloader

For this to work just put the encrypted global-metadata.dat, and it will output a fixed verision. also need to install xxtea `pip install xxtea`

Inorder to do this you put the decrypted global-metadata.dat in the same directory as the script. If it fails this is because the encrytion key has changed. Inorder to fix this you need to find il2cpp::vm::MetadataCache::Initialize. refer to this article https://katyscode.wordpress.com/2021/02/23/il2cpp-finding-obfuscated-global-metadata/. Once you have found that function find the weird string that looks something like this "##%$vsw'lytyqlusxul##p\"lvxrsv\"y\"y'xu%tv\"qsy\"l%%#qlux'ul# wylys\"t 'v$us''A", and replace it in the script, under that string you chould be able to find where the xor is happening, get the key and paste it in the script aswell.
  
### More coming soon...