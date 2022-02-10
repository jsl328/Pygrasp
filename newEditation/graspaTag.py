
from selenium import webdriver
from videoDownload import VideoDownload
# from videoDownload import DownloadResponseInfo
import threading
import time
# import sys
# sys.path.append(r"/Users/mac/Desktop/PyProject/newEditation")
from setumDriver import seleniumDriver

FLODERURLSLIST = []
DOWNLOAD = []


class UrlInfo:
    def __init__(self, txt, href):
        self.txt = txt
        self.href = href
        pass


class GraspaTag:

    def __init__(self):
        self.driver = None
        self.sectionIndex = 0
        self.timer = None
        pass

    def tableExe(self) -> []:
        js_content = self.driver.find_element_by_id('js_content')
        """.指明当前节点"""
        eles = js_content.find_elements_by_xpath("./table[2]//a")
        print("table的数量=" + str(len(eles)) + "个")
        for url in eles:
            href = url.get_attribute("href")
            if href.find('http:') >= 0:
                FLODERURLSLIST.append(url)
        print("table[2]下的a标签的数量=" + str(len(FLODERURLSLIST)) + "个")
        """'先执行一次"""
        self.graspTableExe()
        return FLODERURLSLIST

    def fnexc(self):
        """初始化引擎"""
        self.driver = webdriver.Chrome(executable_path="/Users/mac/Downloads/chromedriver-3")
        self.driver.get("https://mp.weixin.qq.com/s/91qi7Q2iEviHK_42K6Oj4A")
        js_content = self.driver.find_element_by_id('js_content')
        """.指明当前节点"""
        eles = js_content.find_elements_by_xpath("./table[2]//a")
        print("table的数量=" + str(len(eles)) + "个")
        if self.sectionIndex > len(eles):
            """超出边界就返回"""
            return
        for url in range(len(eles)):
            href = eles[self.sectionIndex].get_attribute("href")
            txt = eles[self.sectionIndex].text
            if href.find('http:') >= 0:
                eles[self.sectionIndex].click()
                videoparent = self.driver.find_element_by_id("js_base_container")
                """ 查询video标签并且抓取其src"""
                videonodes = videoparent.find_elements_by_xpath(".//div[@class='js_video_poster video_poster']/video")
                print("videonode__count=" + str(len(videonodes)))
                record = []
                for nodeIndex in range(len(videonodes)):
                    src = videonodes[nodeIndex].get_attribute("src")
                    print("videonode__src=" + src + "txt" + txt)
                    record.append(UrlInfo(txt, src))
                print("a标签点击后video源的数量:" + str(len(record)) + "个")
                for index in range(len(record)):
                    print("urlInfo的txt=" + record[index].txt + "urlInfo的src=" + record[index].href)
                    res = VideoDownload().excDownlaod(record[index].txt, record[index].href, "2")
                    print("DownloadResponseInfo", res.msg)
                    DOWNLOAD.append(record[index].href)
                    """返回上一级，也就是主页重新获取a便签"""
                    self.driver.back()
                    self.driver.refresh()
                    self.sectionIndex += 1
            # break
            self.driver.quit()
            self.fnexc()
        if len(DOWNLOAD) == len(eles):
            print("当前所在测视频已经下载完毕，请手动切换下一册")
        self.driver = self.timer = None

