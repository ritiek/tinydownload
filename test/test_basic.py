from tinydownload import tinydownload

query = 'http://s000.tinyupload.com/?file_id=34348317875703136345'

def test_id():
    expect_file_id = '34348317875703136345'
    global file_id
    file_id = tinydownload.get_file_id(query)
    assert file_id == expect_file_id

def test_filename():
    expect_filename = 'test.txt'
    global soup
    soup = tinydownload.make_soup(file_id)
    global filename
    filename = tinydownload.get_filename(soup)
    assert filename == expect_filename

def test_download():
    expect_result = 'TEST PASSED!\n'
    link = tinydownload.get_filelink(soup)
    tinydownload.download(link, filename)
    with open(filename, 'r') as text:
        result = text.read()
    assert result == expect_result
