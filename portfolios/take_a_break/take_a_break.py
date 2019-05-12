import webbrowser
import time
import os


def promt(times, wait):
	output = [f'Now is {time.ctime()}', 'The program is still running.', '..']
	for i in range(times):
		time.sleep(wait/times)
		for j in range(len(output)):
		    print(output[j])
		    time.sleep(3)


def play_music():
    url = 'page.html'   
    # open a local html file on mac
    try:
    	webbrowser.get('chrome').open('file://' + os.path.realpath(url))
    # open a url
    except:
    	webbrowser.get('chrome').open(url)
        

def take_a_break(breaks, wait_time):
    print(f'This program started on {time.ctime()}')
    for n in range(breaks):
        if wait_time < 60*60:
        	promt(6, wait_time)
        else:
        	promt(12, wait_time)
        play_music()
        print(n)


# take_a_break(6, 60*20)



