from bottle import route, run, request, HTTPError
import fileswork

@route('/login')
def login():
    #login:         <input type="text" name="login" />
    return '''
        <b>FileMiner v 1.0</b></br>
        <form action="/upload_file" method="post" enctype="multipart/form-data">
          Upload </br>
          Select a file: <input type="file" name="upload" />
          <input type="submit" value="Start" />
        </form>
        <form action="/update_file" method="post" enctype="multipart/form-data">
          Update </br>
          Select a file: <input type="file" name="upload" />
          <input type="submit" value="Start" />
        </form>
        <form action="/get_file_data" method="post" enctype="multipart/form-data">
          Get file</br>
          file_name:     <input type="text" name="file_name" />
          <input type="submit" value="Start" />
        </form>
        <form action="/get_file_metadata" method="post" enctype="multipart/form-data">
          Get file metadata </br>
          file_name:     <input type="text" name="file_name" />
          <input type="submit" value="Start" />
        </form>
        <form action="/get_files_list" method="post" enctype="multipart/form-data">
          Get files list </br>
          <input type="submit" value="Start" />
        </form>
    '''


@route('/upload_file', method='POST')
def upload_file():
    try:
        #login        = request.forms.get('login')
        upload       = request.files.get('upload')
        if not upload:
            return HTTPError(400, 'Field file is empty')

        return fileswork.upload_file()
    except Exception:
        return HTTPError(500,'Server error')

@route('/update_file', method='POST')
def update_file():
    try:
        upload = request.files.get('upload')
        if not upload:
            return HTTPError(400, 'Field file is empty')
        return fileswork.update_file()
    except Exception:
        return HTTPError(500,'Server error')

@route('/get_file_data', method='POST')
def get_file_data():
    try:
        file_name = request.forms.get('file_name')
        if not file_name:
            return HTTPError(400, 'Field file is empty')
        return fileswork.get_file_data()
    except Exception:
        return HTTPError(500,'Server error')

@route('/get_file_metadata', method='POST')
def get_file_metadata():
    try:
        file_name = request.forms.get('file_name')
        if not file_name:
            return HTTPError(400, 'Field file is empty')
        return fileswork.get_file_metadata()
    except Exception:
        return HTTPError(500,'Server error')

@route('/get_files_list', method='POST')
def get_files_list():
    try:
        return fileswork.get_files_list()
    except Exception:
        return HTTPError(500,'Server error')

#run(host='localhost', port=8080)