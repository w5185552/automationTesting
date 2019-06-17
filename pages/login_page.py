from selenium.webdriver.common.by import By



class LoginPage:
    '''
    管理登录页面所有页面元素，格式为：定位方式，元素路径，元素描述信息
    '''
    username_input = (By.XPATH, "//*[@id='use_name']",'用户名输入框')
    pwd_input = (By.XPATH, "//*[@id='use_pwd']",'密码输入框')
    login_button=(By.XPATH, "//input[@value='登录']",'登录按钮')
    shouye =(By.XPATH,"//span[text()='舌尖上的民族']",'舌尖上的名族')


