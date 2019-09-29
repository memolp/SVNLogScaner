# -*- coding:utf-8 -*-

"""
  获取提交日志列表
"""

import re

from svnlog.SVNCommand import *

SVN_LOG_LINE = "------------------------------------------------------------------------"
SVN_LOG_SPLIT= "|"
SVN_LOG_PATHS= "Changed paths:"

class SVNCommitLogData:
    """
    提交日志信息
    """
    def __init__(self):
        self.version = 0
        self.author = ""
        self.date = None
        self.files = []
        self.comment = ""

    def format(self, lines):
        """
        格式化
        :param lines:
        :return:
        """
        size = len(lines)
        commit_summary = lines[0].split(SVN_LOG_SPLIT)
        if len(commit_summary) < 3:
            raise ValueError("{0} is not commit summary".find(lines[0]))
        self.version = int(commit_summary[0][1:])
        self.author = (commit_summary[1].strip())
        date_match = re.findall(r"\d+-\d+-\d+ \d+:\d+:\d+",commit_summary[2])
        print(date_match,commit_summary[2])
        self.date = date_match[0]
        if size < 2:
            return
        i = 1
        # 如果是详细文件列表
        if lines[i].find(SVN_LOG_PATHS) >= 0:
            i = 2
            while i < size:
                file_line = lines[i]
                if file_line.startswith("\r\n"):
                    break
                i += 1
                file_line = file_line.strip()
                status, filename = file_line.split(" ",maxsplit=1)
                self.files.append({"status":status, "filename":filename.rstrip("\r\n")})
        # 日志
        if lines[i].startswith("\r\n"):
            i = i + 1
            while i < size:
                file_line = lines[i]
                self.comment += file_line
                i += 1




def SVNCommitLog(url, version=0):
    """
    日志SVN提交
    :param url:
    :param version:
    :return:
    """
    result = []

    version_rang = "HEAD"
    if version > 0:
        version_rang = "{0}:HEAD".format(version)

    pf = SVNCommand.GetSVNLogfd(url, "v", r=version_rang)
    if pf is None:
        return result

    commit_log_lines = []
    for line in pf:
        str_line = line.decode(encoding="gbk")
        if str_line.find(SVN_LOG_LINE) >= 0:
            if len(commit_log_lines) == 0:
                continue
            else:
                logData = SVNCommitLogData()
                logData.format(commit_log_lines)
                commit_log_lines = []
                result.append(logData)
        else:
            commit_log_lines.append(str_line)

    return result



# lines = SVNCommitLog("https://pcw21941.g-bits.com/svn/test/",3)
# for l in lines:
#     print(l.comment,l.author,l.files,l.version)