# LOZ13
Save Files

In this lesson, you will become familiar with how to read and write to a relational database which we will use to save our game progress.

Some minor updates:  Link's PNG file now doesn't include the grey box around him.  You are welcome to use the updated PNG.  Also I have added the intro screen music and the save screen png.  You will need to place those in your program file folder.  You may wish to use the DB browser app if you are on a device you can install it.  Here is the link for that download: https://sqlitebrowser.org/dl/

game1.11.py is the game file we will start with today along with pygame_functions10.py from last time.  game1.11.1.py is the completed game file at the end of the video as well as pygame_functions11.py is the finished functions file.  

Video - YouTube - https://www.youtube.com/watch?v=WuRfxPDI0Uo   
Video - EdPuzzle - Part 1 - https://edpuzzle.com/media/5f28704ab5b95b3f0eba929c  
Video - EdPuzzle - Part 2 - https://edpuzzle.com/media/5f2873442e2ccd3f706938d3  
Slides - https://docs.google.com/presentation/d/1KKAy-gArcu9d2wJ3PmxVjPo-RCS-jWCGHasHmOSEDrQ/edit?usp=sharing    

Extensions:  
1. What if we want to also save link's kill count in the database.  Delete the current database file.  Alter the python_functions code to make another field when making the table.  The kills field should have integer datatype.
2. When you save a file, the DB update should now include the kill count from link.kills
3. When you load a file, the DB statement should now include the kill count and it should update link.kills in the pygame_functions file
4. Test your code by having link's kill count printed in the console when the game is loaded.  Make sure that when you save a game, exit the game, and then reload the same game, that the kill count loads correctly
