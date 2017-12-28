import requests
##This file is was created in Python 3.6.2 and requires the
##installation of the "Requests" library at
##http://docs.python-requests.org/en/master/
##This file will check if a link is working properly and print a list of the
##working links to a text file called "FFRKMusicList"
def main():
    url = 'https://dff.sp.mbga.jp/dff/static/lang/bgm/bgm_TTT/bgm_RR_AAA.FFF'
    realms = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,21,22,24,25,30,80,90]
    ask = int(input("Give Realm ID, or type '0' to search all (w/o leading 0's): "))
    form = input("Pick format OGG (Android) or M4A (IOS): ")
    form = form.lower()
    if ask == 0:#Search through all realms
        download = input("Download all? (y/n): ")
        print()
        display = open("FFRKMusicList.txt",'a')#Opens a text file named "FFRKMusicList and adds working URLs to the last line in the file
        for i in realms:
            if i < 10:
                realm = "0"+str(i)
            else:
                realm = str(i)
            for j in range(1,251):#Searches up to AAA = 250
                url = 'https://dff.sp.mbga.jp/dff/static/lang/bgm/bgm_TTT/bgm_RR_AAA.FFF'
                if j < 10:
                    track = "00"+str(j)
                elif j > 9 and j < 100:
                    track = "0"+str(j)
                else:
                    track = str(j)
                url = url.replace("RR",realm)
                url = url.replace("AAA",track)
                url = url.replace("TTT",form)
                url = url.replace("FFF",form)
                res = requests.get(url)
                try:
                    res.raise_for_status()
#Test purposes                    print("A music file exists at:",url)
                    display.write(url + "\n")
                    if download == "y":
                        name = "bgm_"+realm+"_"+track+"."+form
                        f = open("M/"+name,"wb")
                        f.write(res.content)
                        f.close()
                        print("Download Complete!")
                except Exception as exc:
                    print('N/A')
    elif ask in realms:#Search through a specific realm
        if ask < 10:
            realm = "0"+str(ask)
        else:
            realm = str(ask)
        track = int(input("Give the track number or '0' to search all (w/o leading 0's): "))
        download = input("Download selected track(s)? (y/n): ")
        display = open("FFRKMusicList.txt",'a')#Opens a text file named "FFRKMusicList and adds working URLs to the last line in the file
        print()
        if track == 0:#Search through all tracks (AAA)
            for j in range(1,251):#Searches up to AAA = 250
                url = 'https://dff.sp.mbga.jp/dff/static/lang/bgm/bgm_TTT/bgm_RR_AAA.FFF'
                if j < 10:
                    track = "00"+str(j)
                elif j > 9 and j < 100:
                    track = "0"+str(j)
                else:
                    track = str(j)
                url = url.replace("RR",realm)
                url = url.replace("AAA",track)
                url = url.replace("TTT",form)
                url = url.replace("FFF",form)
                res = requests.get(url)
                try:
                    res.raise_for_status()
                    
#Test purposes                    print("A music file exists at:",url)
                    display.write(url + "\n")
                    if download == "y":
                        name = "bgm_"+realm+"_"+track+"."+form
                        f = open("M/"+name,"wb")
                        f.write(res.content)
                        f.close()
                        print("Download Complete!")
                except Exception as exc:
                    print('N/A')
        elif track < 10:#Find specific track where AAA < 10
            track = "00"+str(track)
            url = 'https://dff.sp.mbga.jp/dff/static/lang/bgm/bgm_TTT/bgm_RR_AAA.FFF'
            url = url.replace("RR",realm)
            url = url.replace("AAA",track)
            url = url.replace("TTT",form)
            url = url.replace("FFF",form)
            res = requests.get(url)
            try:
                res.raise_for_status()
#Test purposes                print("A music file exists at:",url)
                display.write(url + "\n")
                if download == "y":
                        name = "bgm_"+realm+"_"+track+"."+form
                        f = open("M/"+name,"wb")
                        f.write(res.content)
                        f.close()
                        print("Download Complete!")
            except Exception as exc:
                print('N/A')
        elif track < 100:#Find specific track if 1 <= AAA < 100
            track = "0"+str(track)
            url = 'https://dff.sp.mbga.jp/dff/static/lang/bgm/bgm_TTT/bgm_RR_AAA.FFF'
            url = url.replace("RR",realm)
            url = url.replace("AAA",track)
            url = url.replace("TTT",form)
            url = url.replace("FFF",form)
            res = requests.get(url)
            try:
                res.raise_for_status()
#Test purposes                print("A music file exists at:",url)
                display.write(url + "\n")
                if download == "y":
                        name = "bgm_"+realm+"_"+track+"."+form
                        f = open("M/"+name,"wb")
                        f.write(res.content)
                        f.close()
                        print("Download Complete!")
            except Exception as exc:
                print('N/A')
##The block commented out below geos up to the max Array ID allowable (999)
##        elif track < 1000:
##            track = str(j)
##            url = 'https://dff.sp.mbga.jp/dff/static/lang/bgm/bgm_TTT/bgm_RR_AAA.FFF'
##            url = url.replace("RR",realm)
##            url = url.replace("AAA",track)
##            url = url.replace("TTT",form)
##            url = url.replace("FFF",form)
##            res = requests.get(url)
##            try:
##                res.raise_for_status()
##                print("A music file exists at:",url)
##            except Exception as exc:
##                print('No music file exists: %s' % (exc),"at",url)
    display.close()
    print("Done!")
main()
#print('No music file exists: %s' % (exc),"at",url) -> Test purposes only
