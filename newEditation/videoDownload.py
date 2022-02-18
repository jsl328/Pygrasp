
import urllib.request
import urllib.parse
import os
gdst = r"/Users/mac/Desktop/video/"

class DownloadResponseInfo:

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
        pass


class VideoDownload:

    def __init__(self):
        pass

    def excDownlaod(self, txt, downloadurl, dstfolder) -> DownloadResponseInfo:
        if downloadurl:
            dsl = os.path.join(gdst, dstfolder)
            # 检查有没有dsl目录
            if not os.path.exists(dsl):
                os.mkdir(dsl)
            filepath = os.path.join(dsl, txt + '.mp4')
            print("存储路径--" + filepath + ":" + "下载的地址excDownlaodurl--" + downloadurl)
            reponse = urllib.request.urlopen(url=downloadurl)
            # decode()做用是将响应中字节(byte)类型的数据值转成字符串类型
            # data = reponse.read().decode()
            data = reponse.read()
            with open(filepath, 'wb') as fp:
                fp.write(data)
            print('文件写入完毕')
            fp.close()
        return DownloadResponseInfo(200, "success")
