Hello,
	Thanks for using my Mod Installer. It is simple to use the installer. First, make a backup using the backup button (ensure that you have a clean install of FS). Next Extract the mod zip file in a folder. (for eg TestMod.zip to TestMod folder, make sure the testmod folder has the 'Floating Sandbox' folder inside it or it won't work.) then choose the folder with the 'Floating Sandbox' folder through the browse button (eg choose the TestMod folder). CLick on Install Button and Done! The mod is (hopefully) installed! To uninstall the mod you can either try the uninstall button after choosing the mod path OR load the backup you have created through the 'Load Backup' button. Please provide feedback/suggestions/bugs/anything idk via discord.
_______________________________________________________________________________________________________________________________________________________________________

*TROUBLE SHOOTING*
1. If you get error that the mod folder does not exist then: 	1. You have choosen the wrong folder/blank path (Solution: Make sure the choosen folder has 'Floating 								   	   Sandbox' folder inside it)  or
							  	2. The mod is in wrong format (Soluton: Contact the mod owner or try fixing it yourself if you can 								   	   through the for modders section below.)
								3. IDK
2. If you get the error that the fs folder does not exist then well, fs is not installed in your PC. If it is installed and still this error shows then contact me through discord.
3. Another error is for when you try to uninstall a mod but it is already not installed, pretty self explanatory.
4. An error may come up that filepaths.txt does not exist then try the 'Load Backup' method. (This is why backup is important)
5. You may get backup already exists then no need to do backup. If you want to delete the existing backup then unfortunately you have to do it manually for now, the backup file is in "C:\Users\YOUR_USERNAME\AppData\Local\FSBackup"
4. Any other errors or problems, please do contact and report me via discord.
_______________________________________________________________________________________________________________________________________________________________________

*FOR MODDERS*
	It is same way easy to make the mod installer work for your mod. First you need to make the directories in the same order in which they are in the original 'Floating Sandbox' folder only for where you want to place your file. for example: if you have changed or added new fish into FS then the texture file should be placed in C:\Users\YOUR_USERNAME\AppData\Local\Floating Sandbox\Data\Textures\Fish. Therefore, first create 'Floating Sandbox' folder in your mod folder, then inside that folder create 'Data' folder then inside it 'Textures' folder, inside it 'Fish' folder and lastly, inside the fish folder add all the new textures and files of your mod. If you wanted to also add some files in the sound folder then come back to 'Data' folder, create 'Sounds' folder and then inside it place all the files of your mod. Similarly you can create the mod and then make only the path through folders and paste the mod files in the folder where it must be in the original 'Floating Sandbox' folder. Other files and folder which are not part of your mod are not required to be added.
	 For making uninstallation,first make a 'modpath.txt' and put the modded file paths that need to be removed from the original 'Floating Sandbox' folder. For example: in the modpaths.txt we can write:
Floating Sandbox\license.txt
Floating Sandbox\Data\idk2.txt
Then make a folder named 'FSold', then in this folder make the folders from the 'Floating Sandbox' to the location of the file that is going to be replaced and paste the original file in that folder (similar to how you did previously). For example if you replaced a texture in "C:\Users\YOUR_USERNAME\AppData\Local\Floating Sandbox\Data\Textures\World\land_0.png" then first you need to create an 'FSold' folder in your mod folder (same place where you created the 'FLoating Sandbox' folder), then inside it create the 'Floating Sandbox' folder then 'Data folder inside it, then 'Textures folder inside it, then 'World' folder inside it then finally place the original 'land.png'. 

IMP:- 	REMEMBER THAT NAME OF EACH OF THE FOLDER IS CASE SENSITIVE, i.e. it must be same as in original 'Floating Sandbox' folder.
	THE PATHS IN 'filepaths.txt' SHOULD BE IN DIFFERENT LINES FOR EACH FILE.

Thanks again,
Splayer (Discord:- @splayer_1)