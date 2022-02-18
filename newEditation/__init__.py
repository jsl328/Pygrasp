
import sys
sys.path.append(r"/Users/mac/Desktop/Pygrasp/newEditation")
from setumDriver import seleniumDriver
from graspaTag import GraspaTag
from youtubeInterest import YoutubeInterest
from businessEnglish import BusinessEnglish

import  threading

def selenium_driver():

    """新概念金典教程视频"""
    edtation = GraspaTag()
    # threading.Timer()
    # t = threading.Thread(target=edtation.fnexc(), args=(edtation, ))
    # t.start()
    edtation.fnexc()
#


def youtubeVideo():
    """youtube经典视频"""
    interest = YoutubeInterest()
    interest.youtubeInterestExec()
    pass


def workplaceVideo():
    """职场经典对话视频"""
    bus = BusinessEnglish()
    bus.businessEnglishExe()
    pass


def australianTelevisionVideo():
    """澳大利亚电视台视频"""
    pass

