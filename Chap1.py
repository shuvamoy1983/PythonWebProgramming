import urllib.request
from urllib.error import URLError,HTTPError,ContentTooShortError

print("Step 1) Downloading a web page")
def download(url):
    return urllib.request.urlopen(url).read().decode("utf-8")

print("______________________________________________________________")
print("Step 2) Downloading a web page but what happens if we have error")
print("from urllib.error, import URLError,HTTPError,ContentTooShortError")

print("Exception handiling if ")
def download_Error_content(url):
    print("Downloading Started")
    try:
        data = urllib.request.urlopen(url).read().decode("utf-8")

    except (URLError,HTTPError,ContentTooShortError) as e:
        print("Download Error", e.reason)
        data = None

    return data

print("______________________________________________________________")
print("Step 3) Downloading a web page but what happens if we have error")
print("This below function is for retrying to download data from Web")
def retrying_downloads(url, attempt):
    print("Downloading:")
    try:
        dataset = urllib.request.urlopen(url).read().decode("utf-8")
    except (URLError,HTTPError,ContentTooShortError) as e:
        print("download Error" , e.reason)
        dataset= None
        if attempt> 0:
            if hasattr(e,'code') and 500 <= e.code <600:
                return retrying_downloads(url,attempt -1)
    return dataset

print("______________________________________________________________")
print("Step 4) Setting an user Agent")

def setting_an_user_agent(url,user_agent,attempt):
    print("downloading",url)

    request= urllib.request.Request(url)
    request.add_header('User_agent' ,user_agent)

    try:
        load = urllib.request.urlopen(url).read().decode("utf=8")
    except (URLError,HTTPError,ContentTooShortError) as e:
        print("Download Error" ,e.reason)
        load= None
        if attempt > 0:
            if hasattr(e,'code') and 500 <= e.code < 600 :
                #recursive call for the below function
                return setting_an_user_agent(url,user_agent,attempt -1)
    return load

if __name__ == '__main__':

    ## Enable the line while calling the required the function
    rslt = download("http://carlofontanos.com/api/tutorials.php?data=all")
    #print(rslt)
    data1 = download_Error_content("http://httpstat.us/500")
    #print(data1)

    #final_data = retrying_downloads("http://httpstat.us/500",10)
    #print(final_data)

    data_with_agent = setting_an_user_agent("http://www.facebook.com","wswp",5)
    print(data_with_agent)