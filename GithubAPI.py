import urllib.request

gh_url = 'https://manage.auth0.com/#/users/YXV0aDAlN0M1YTUyZWVjNWNhYzE1YTZhYTEwYWRjYzM'
req = urllib.request.Request(gh_url)

password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, gh_url, '*****', '***')

auth_manager = urllib.request.HTTPBasicAuthHandler(password_manager)
opener = urllib.request.build_opener(auth_manager)

urllib.request.install_opener(opener)

handler = urllib.request.urlopen(req)
print(handler.getcode())
print(urllib.request.urlopen(gh_url).read().decode("utf-8"))