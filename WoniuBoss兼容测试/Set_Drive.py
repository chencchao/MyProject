from selenium import webdriver


def set_driver(path,binary):
    if 'geckodriver' in path:
        wd = webdriver.Firefox(executable_path=path, firefox_binary=binary)
    if 'chrome' in path:
        wd = webdriver.Chrome(executable_path=path)
    if 'IEDriverServer' in path:
        wd = webdriver.Ie(executable_path=path)
    wd.get('http://192.168.6.237:8080/WoniuBoss3.5/login')
    wd.maximize_window()
    wd.implicitly_wait(10)
    return wd