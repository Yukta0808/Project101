import os
import dropbox
from dropbox.files import WriteMode

class Transfer_data:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for root,dir,file in os.walk(file_from):
            for file_name in file:
                localpath = os.path.join(root,file_name)
                relative_path = os.path.relpath(localpath,file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(localpath, 'rb')as f:
                    dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))

def main():
    accessToken = 'sl.BIXzuUVRL1WHG8VKzFWyu-V3CjrfGBswrQDDt8hGj2Y7cuD9WYCU6LXSwfeRv_DgtxM6GuZ1GYOHzYWnBRyDQNZo9-WMmshYOAHHrDcFtQ-GdlSir34tLPkmXEvEY9pNgDjD4oLJDuwn'
    transfer_data = Transfer_data(accessToken)
    fileFrom =  str (input('Enter the folder path to transfer: '))
    fileTo = input('Enter the dropbox path: ')
    transfer_data.upload_file(fileFrom, fileTo)
    print('File has been moved!')

main()