'''
The script will read lines from a json file.  The file was created
by exporting the 'recorded' table from my old mythtv using phpMyAdmin

For each line it will collect the .mpg and .mpg.png files from the
old server using scp and then read the approprate fields to populate
a .mpg.xml file

I am not bothered about which channel the files came from, so this will 
be left static.

Keys in each recording entry (from recorded.json)

profile,subtitle,recordid,basename,transcoder,cutlist,originalairdate,storagegroup,
watched,transcoded,playgroup,category,progstart,endtime,title,bookmark,hostname,programid,duplicate,progend,
filesize,stars,lastmodified,preserve,findid,description,season,timestretch,deletepending,previouslyshown,
editing,recpriority,seriesid,commflagged,recgroup,episode,bookmarkupdate,autoexpire,chanid,inetref,starttime

'''



import json, glob

file_list = (glob.glob("/home/justin/2TBRaid/Recordings/*.ts"))

with open ('recorded.json', 'r') as f:
	data = json.load(f)

# print data[0]['description']
# print
# for key in data[0].keys():
#     print key, data[0][key]
# print

unique_episodes = []
basename_list = []
for recording in data:
    if 'Castle' == recording['title']: # and 'S1 Ep3' in recording['description']:
        unique_episodes.append(recording['description'])
        basename_list.append(recording['basename'])

for index, episode in enumerate(unique_episodes):
    print episode, basename_list[index]
    if basename_list[index] in file_list:
        print
        print 'file exists!'
        print

