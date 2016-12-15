from bottle import request, static_file, HTTPError
import os,time

def get_base_path():
    return os.getcwd() + '/path_to_safe/'

# Used for uploading file to the server
# All files uploads are executed in "get_base_dir" result created in current base path
def upload_file():
    result_mes   = 'File upload successful'
    #login        = request.forms.get('login')
    upload       = request.files.get('upload')
    #name, ext    = os.path.splitext(upload.filename)
    #raw_filename = upload.raw_filename
    filename     = upload.filename
    #result_mes + '</br> raw_filename = "' + raw_filename + '", saved filename = "' + filename + '"'
    #if ext not in ('.png','.jpg','.jpeg'.'.txt'):
    #    return 'File extension not allowed.'

    save_path = get_base_path();
    #print save_path + '/' + filename
    #result_mes   = result_mes + '</br> save_path = ' + save_path + '/' + filename
    #rm = ResourceManager()
    #rm.add_path('./')
    #print rm.lookup(filename)
    if not(os.path.exists(save_path)): os.makedirs(save_path)
    if os.path.exists(save_path + filename):
        return HTTPError(400, 'File is already exist. Use update_file')
    else:
        upload.save(save_path + filename) # appends upload.filename automatically
    return result_mes

# Used for updating file on the server
def update_file():
    result_mes = 'File update successful'
    #login = request.forms.get('login')
    upload = request.files.get('upload')
    filename = upload.filename
    save_path = get_base_path();
    if not (os.path.exists(save_path)):
        return HTTPError(500, 'Directory is not exist.')
    if not os.path.exists(save_path + filename):
        return HTTPError(404, 'File is not exist. Use upload_file')
    else:
        upload.save(save_path + filename,True)  # appends upload.filename automatically
    return result_mes

def get_file_data():
    #login = request.forms.get('login')
    file_name = request.forms.get('file_name')
    base_path = get_base_path();
    if not os.path.exists(base_path + file_name):
        return HTTPError(404, 'File is not exist. Use upload_file')

    response = static_file(file_name,base_path,download=True)
    return response

def get_file_metadata():
    #login = request.forms.get('login')
    file_name = request.forms.get('file_name')
    base_path = get_base_path();
    if not os.path.exists(base_path + file_name):
        return HTTPError(400, 'File is not exist. Use upload_file')

    metadata = os.stat(base_path + file_name)
    result_mes = 'File metadata: ' + file_name
    result_mes = result_mes + '{ "Change date" "' + str(time.localtime(metadata.st_mtime))+ '"'
    result_mes = result_mes + ' "protection bits" "' + str(metadata.st_mode)+ '"'
    result_mes = result_mes + ' "inode number" "' + str(metadata.st_ino)+ '"'
    result_mes = result_mes + ' "device" "' + str(metadata.st_dev)+ '"'
    result_mes = result_mes + ' "number of hard links" "' + str(metadata.st_nlink)+ '"'
    result_mes = result_mes + ' "user id of owner" "' + str(metadata.st_uid)+ '"'
    result_mes = result_mes + ' "group id of owner" "' + str(metadata.st_gid)+ '"'
    result_mes = result_mes + ' "size of file in bytes" "' + str(metadata.st_size)+ '"'
    result_mes = result_mes + ' "time of most recent access" "' + str(metadata.st_atime)+ '"'
    result_mes = result_mes + ' "time of most recent content modification" "' + str(metadata.st_mtime)+ '"'
    result_mes = result_mes + ' "platform dependent" "' + str(metadata.st_ctime)+ '"'
    result_mes = result_mes + '}'
    return result_mes

def get_files_list():
    base_path = get_base_path();
    files = os.listdir(base_path)
    result_mes = 'Files list:'
    #print files
    if files:
        #files = [file for file in files if os.path.isfile(file)]
        #print files
        if files:
            for fl in files:
                result_mes = result_mes + ' "' + fl + '"'
        else: result_mes = result_mes + ' is empty'
    return result_mes