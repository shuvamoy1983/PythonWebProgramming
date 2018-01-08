import urllib.request
from urllib.error import URLError,HTTPError,ContentTooShortError

print("Step 1) Downloading a web page")
def download(url):
    return urllib.request.urlopen(url).read().decode("utf-8")

print("______________________________________________________________")
print("Step 2) Downloading a web page but what happens if we have error")
print("from urllib.error, import URLError,HTTPError,ContentTooShortError")

def download_Error_content(url):
    print("Downloading Started")
    try:
        data = urllib.request.urlopen(url).read().decode("utf-8")

    except (URLError,HTTPError,ContentTooShortError) as e:
        print("Download Error", e.reason)
        data = None

    return data

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




if __name__ == '__main__':
    rslt = download("http://carlofontanos.com/api/tutorials.php?data=all")
    #print(rslt)
    data1 = download_Error_content("http://httpstat.us/500")
    #print(data1)

    final_data = retrying_downloads("http://httpstat.us/500",10)
    print(final_data)