

## Download subtitle for a movie or list of seasons stored in folder
Watch the movie or season in a programmer way

Got your season listed in a folder and you are too lazy to download it one by one.
Congrats, you came to right place.
Just run a few line of commands and you are ready to watch your favourite series or movie without worrying about subtitles.

Clone this directory and Run the below command to setup the environment

    virtualenv -p python3.7 env
    pip install -r requirements.txt
    source env/bin/activate
   
Make sure to create your account on opensubtitles.org
After confirming your account, open the download_subtitles.py file and change the USERNAME and PASSWORD with yours.

Once done, run the script if you want to download subtitle for movie

    python download_subtitles.py --file /full/path/to/your/movie

OR,
If you are a fan of seasons/series and your season is waiting for subtitles in some folder than this is for you

    python download_subtitles.py --folder /full/path/to/your/series/folder

P.S.
At some point in future I would like to do this following thing but for now my series is waiting for me, so any developer is interested feel free to add this listed features and create a pull request.

 - Create this script as library so that it can be installed in global environment and can be run from anywhere in the system.
 - Pass the credentials in arguments.
 - Give user the capability to enter the custom name for a file in case he may not be able to download the subtitle with the help of movie name alone. 
 - Any other suggestions are welcome.

 