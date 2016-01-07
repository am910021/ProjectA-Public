# Include the Dropbox SDK
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

def file_put2(file, number, saveName):
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
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(file)

def file_put(file, number,saveName):
    client = dropbox.client.DropboxClient(access_token)
    size = file.size
    type = file.content_type.split("/")[1]
    name = saveName+str(number)+"."+type
    
    response = client.put_file('/'+name, file)
    return size==response['bytes']

def file_get(saveName, number, content_type, size):
    client = dropbox.client.DropboxClient(access_token)
    type = content_type.split("/")[1]
    name = saveName+str(number)+"."+type
    file, metadata = client.get_file_and_metadata("/"+name)
    if str(metadata['bytes'])==size:
        return file
    else:
        return False


