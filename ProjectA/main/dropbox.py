# Include the Dropbox SDK
from datetime import datetime
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = ''
app_secret = ''
token = ''

access_token = token


#print('linked account: ', client.account_info())


#f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
#out = open('downloadfile', 'wb')
#out.write(f.read())
#out.close()
#print(metadata)

def file_put2(file, number):
    saveName = str(datetime.strftime(datetime.now(), '%Y%m%d'))
    dbx = dropbox.Dropbox(token)
    size = file.size
    type = file.content_type.split("/")[1]
    name = saveName+str(number)+"."+type
    
    response = dbx.files_upload(file, '/'+name)
    if response.size!=size:
        return False
    
    share = dbx.sharing_create_shared_link('/'+name).url.split("/")
    return share[4]+"/"+name



    
def file_get2(saveName, number, content_type, size):
    dbx = dropbox.Dropbox(token)
    type = content_type.split("/")[1]
    name = saveName+str(number)+"."+type
    file = dbx.files_get('/'+name)


def file_delete(name):
    dbx = dropbox.Dropbox(token)
    delFile = dbx.files_delete('/'+name)
    print(delFile)


