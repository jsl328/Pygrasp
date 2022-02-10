
from selenium import webdriver
from videoDownload import VideoDownload

# youtub视频下载地址
youtubeRsts = [
    'https://mp.weixin.qq.com/s/h69P_2b9yNkMAaywLQ1JFA',
    'https://mp.weixin.qq.com/s/ZVLQ06Q-31fJDKLWR5jOiw',
    'https://mp.weixin.qq.com/s/vPpeOKOFEHH2gCNbkTDcRw',
    'https://mp.weixin.qq.com/s/f8TV5Yf6BH-e3QhckTiROw',
    'https://mp.weixin.qq.com/s/ZP8k5HupxRDk0bJ2-h1P4A',#5
    'https://mp.weixin.qq.com/s/881T0zkLcKCB55lS7q0Cgg',
    'https://mp.weixin.qq.com/s/tAE3KZDwaNtKCZNrBcUB2w',
    'https://mp.weixin.qq.com/s/jWCPPMb_fuIzYXEaNBz1hA',#8
    'https://mp.weixin.qq.com/s/_sB6FLi_hB3zSYfTHI_3fQ',#16
    'https://mp.weixin.qq.com/s/s6zyaDn_1ylI-A3J8TMNxw',
    'https://mp.weixin.qq.com/s/A0YIwu6ep8jR_CBHshkADQ',
    'https://mp.weixin.qq.com/s/Rkj2Dp3Q7d8PcRNGTLvYXA',#22
    'https://mp.weixin.qq.com/s/q8WUdVDJHje2tWybDloYag',
    'https://mp.weixin.qq.com/s/2AmYdjCima6rMsPrx3i-aA',
    'https://mp.weixin.qq.com/s/ivSctXSV7vKpB15s2Sp3Yg',
    'https://mp.weixin.qq.com/s/PMdBoBK4xzuVsNLfQrY0ng',#26
    'https://mp.weixin.qq.com/s/xnjaScZ6CU9ool7RSr9vzg',
    'https://mp.weixin.qq.com/s/G0nt52naS9BcjZV5b3905g',
    'https://mp.weixin.qq.com/s/8v4TqZz1A2gzJcCMVhE2nw',
    'https://mp.weixin.qq.com/s/g3ZsH7MSyDPGTa39lnFvmA',
    'https://mp.weixin.qq.com/s/3dtNuU69Zj-SsFTKyzlL6g',#31
    'https://mp.weixin.qq.com/s/rG1SZsy5Xv0ISwBXSt4fCw',
    'https://mp.weixin.qq.com/s/dDtu7ZRw3CHLO2dmu08CYQ',
    'https://mp.weixin.qq.com/s/e0R9SDjBBgK8rfP0bfSFJA',#44
    'https://mp.weixin.qq.com/s/XejuFUPs0W3OBWVxeicclg',
    'https://mp.weixin.qq.com/s/lyarFKVCsHtI5fy9S7C5dw',
    'https://mp.weixin.qq.com/s/piWzpOQO3R4s2SNwStQD0w',
    'https://mp.weixin.qq.com/s/ioRb5Ea2Uoft1RQBk9H4wA',#48
    'https://mp.weixin.qq.com/s/HtGneXM26Eif8kRR3p2Beg',
    'https://mp.weixin.qq.com/s/PPOXL2nyMHzlvQfMoFtExQ',
    'https://mp.weixin.qq.com/s/lkSecrfRQLyovM5wvLCoNA'
]

class YoutubeInterest:

    def __init__(self):
        """初始化引擎"""
        self.driver = webdriver.Chrome(executable_path="/Users/mac/Downloads/chromedriver-3")
        self.youindex = 0
        pass

    def youtubeInterestExec(self):
        lens = len(youtubeRsts)
        if self.youindex > lens:
            return
        for youtub in range(len(youtubeRsts)):
            if youtubeRsts[youtub]:
                self.driver.get(youtubeRsts[youtub])
                js_title = self.driver.find_element_by_id('js_video_page_title')
                print("youtubeInterest js_title = " + js_title.text)
                js_video_parent = self.driver.find_element_by_class_name("video_fill")
                # js_video_label = js_video_parent.find_element_by_xpath("//video")
                print("youtubeInterest js_video_label_src = " + js_video_parent.get_attribute("src"))
                src = js_video_parent.get_attribute("src")
                res = VideoDownload().excDownlaod(js_title.text, src, "youtube")
                print("youtubeInterestExec DownloadResponseInfo", res.msg)
                self.driver.quit()
                self.youindex += 1
            self.youtubeInterestExec()
        self.driver.close()
        self.driver = None
        pass
