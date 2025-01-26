Hello,
	Thanks for using my Mod Manager. The mod manager is abbreviated as FSMM (short for Floating Sandbox Mod Manager). 

_____________________________________________________________________________________________________________________________________________________

*HOW TO USE THE MOD MANAGER*
It is simple to use the installer, the steps are as follows:
1. First, make a backup using the backup button (ensure that you have a clean install of FS). 
2. Next Extract the mod zip file in a folder. (for eg TestMod.zip to TestMod folder. Make sure the testmod folder has the 'Floating Sandbox' folder inside it otherwise the mod is not supported by FSMM) 
3. Then choose the folder you extracted (which has the 'Floating Sandbox' folder) through the browse button (eg choose the TestMod folder). 
4. CLick on Install Button and Done! The mod is (hopefully) installed! To uninstall the mod you can either try the uninstall button after choosing the mod path OR load the backup you have created through the 'Load Backup' button. Please provide feedback/suggestions/bugs/anything, idk, via discord.
FOR DETAILED DOCUMENTATION, PLEASE VISIT GITHUB: 
_____________________________________________________________________________________________________________________________________________________

*TROUBLE SHOOTING*
1. If you get error that the mod folder does not exist then: 	1. You have choosen the wrong folder/blank path (Solution: Make sure the choosen folder has 'Floating 								   	   Sandbox' folder inside it)  or
							  	2. The mod is in wrong format (Soluton: Contact the mod owner or try fixing it yourself if you can 								   	   through the 'for modders' section below.)
								3. IDK
2. If you get the error that the fs folder does not exist then well, fs is not installed in your PC. If it is installed and still this error shows then contact me through discord.
3. Another error is for when you try to uninstall a mod but it says that the mod is already not installed, pretty self explanatory.
4. An error may come up that 'FSold folder' does not exist. This is probably due to the modders fault (Using invalid format not supported by FSMM). Contact the owner or try fixing yourself.
5. If you get the error that Mod does not exist then this is due to the modders fault (Using invalid format not supported by FSMM). Contact the owner or try fixing yourself.
5. You may get backup already exists then no need to do backup. If you want to delete the existing backup then use the 'Delete Backup' button.
4. Any other errors or problems, please do contact and report me via discord.
_____________________________________________________________________________________________________________________________________________________

*FOR MODDERS*
	It is same way easy to make the mod installer work for your mod. 
First you need to make the directories in the same order in which they are in the original 'Floating Sandbox' folder only for where you want to place your file. 
For example: if you have changed or added new fish into FS then the texture file should be placed in C:\Users\YOUR_USERNAME\AppData\Local\Floating Sandbox\Data\Textures\Fish. Therefore, first create 'Floating Sandbox' folder in your mod folder, then inside that folder create 'Data' folder then inside it 'Textures' folder, inside it 'Fish' folder and lastly, inside the fish folder add all the new textures and files of your mod. If you wanted to also add some files in the sound folder then come back to 'Data' folder, create 'Sounds' folder and then inside it place all the files of your mod. Similarly you can create the mod and then make only the path through folders and paste the mod files in the folder where it must be in the original 'Floating Sandbox' folder. Other files and folder which are not part of your mod are not required to be added.
	 
For making uninstallation, first make a folder named 'src',
then inside it make .txt (text file) inside it with the name of YOUR MOD and write the modded file paths that need to be removed from the original 'Floating Sandbox' folder. For example: in the Mod 1.txt we must write it in this way:
Floating Sandbox\license.txt
Floating Sandbox\Data\idk2.txt

Lastly make a folder named 'FSold',
then in this folder make the folders from the 'Floating Sandbox' to the location of the file that is going to be replaced and paste the original file in that folder (similar to how you did previously).  IF your mod doesn't replace any exisitng files then just create the 'FSold' folder and then inside it the 'Floating Sandbox' folder.
For example if you replaced a texture in "C:\Users\YOUR_USERNAME\AppData\Local\Floating Sandbox\Data\Textures\World\land_0.png" then first you need to create an 'FSold' folder in your mod folder (same place where you created the 'FLoating Sandbox' folder), then inside it create the 'Floating Sandbox' folder then 'Data folder inside it, then 'Textures folder inside it, then 'World' folder inside it then finally place the original 'land.png'.

IMPORTANT:- 	REMEMBER THAT NAME OF EACH OF THE FOLDER IS CASE SENSITIVE, i.e. it must be same as in original 'Floating Sandbox' folder.
	THE PATHS IN 'filepaths.txt' SHOULD BE IN DIFFERENT LINES FOR EACH FILE.

For a more detailed and perhaps a better guide, watch my video or visit the github:
YT : 
Github : 
_____________________________________________________________________________________________________________________________________________________

Thanks again,
Splayer (Discord:- @splayer_1) (CONTACT FOR ANY HELP)