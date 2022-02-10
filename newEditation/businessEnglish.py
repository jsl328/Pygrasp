from selenium import webdriver
from videoDownload import VideoDownload

# 30册商务英语全集
business = [
    'https://mp.weixin.qq.com/s/IPflj8X6K3Kf7o_8-mpMGQ',
    'https://mp.weixin.qq.com/s/ixGnHEG07NlCZ5pbPMFC2g',
    'https://mp.weixin.qq.com/s/LxmjvxENCnxs6lxAZb9nlA',
    'https://mp.weixin.qq.com/s/WuFcE_-v5mLWtXPD5mH3lA',#9
    'https://mp.weixin.qq.com/s/hKu0DYEBOyx5gDu2DN_Ytw',
    'https://mp.weixin.qq.com/s/3r1GdBoLEYctd4WaV28_Mw',
    'https://mp.weixin.qq.com/s/7paC4biLh9mwePJbrxiTSg',
    'https://mp.weixin.qq.com/s/iyeqtscZC01cq92s0-hUyw',#13
    'https://mp.weixin.qq.com/s/7pJBX-68tkGDyQ7t2FDz3Q',
    'https://mp.weixin.qq.com/s/bTaOjDRVNXsGH9bd3C59fg',
    'https://mp.weixin.qq.com/s/xkG49Obz16eG6_j8PgT7hA',
    'https://mp.weixin.qq.com/s/NbVxcHnvrzDof6glev3wHQ',
    'https://mp.weixin.qq.com/s/a0HBmsFoJhtbMd62WAMfuQ',
    'https://mp.weixin.qq.com/s/UgtXibzHn2FRH-0551ocnw',
    'https://mp.weixin.qq.com/s/iU_zGXGapwnI-DzBGjhBNw',#20
]


class BusinessEnglish:
    def __init__(self):
        self.driver = None
        self.businessindex = 0
        pass

    def businessEnglishExe(self):
        self.driver = webdriver.Chrome(executable_path="/Users/mac/Downloads/chromedriver-3")
        lens = len(business)
        if self.businessindex > lens:
            return
        for busin in range(len(business)):
            if business[self.businessindex]:
                self.driver.get(business[self.businessindex])
                js_title = self.driver.find_element_by_id('js_video_page_title')
                print("business js_title = " + js_title.text)
                js_video_parent = self.driver.find_element_by_tag_name("video")
                # js_video_parent = self.driver.find_element_by_class_name("video_fill")
                # js_video_label = js_video_parent.find_element_by_xpath("//video")
                print("business js_video_label_src = " + js_video_parent.get_attribute("src"))
                src = js_video_parent.get_attribute("src")
                res = VideoDownload().excDownlaod(js_title.text, src, "business")
                print("business DownloadResponseInfo", res.msg)
                self.driver.quit()
                self.businessindex += 1
            self.businessEnglishExe()
        self.driver.close()
        self.driver = None
        pass
