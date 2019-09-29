# -*- coding:utf-8 -*-

"""
  svn 两个文件对比
"""

import difflib

from svnlog.SVNCommand import *


def SVNDiffFileAsHtml(url,form, to, encoding="gbk"):
    """
    svn diff文件的两个版本，结果返回
    :param url:
    :param form:
    :param to:
    :param encoding:
    :return:
    """
    form_fd = SVNCommand.GetSVNVersionFilefd(url, form)
    to_fd = SVNCommand.GetSVNVersionFilefd(url, to)
    if not form_fd or not to_fd:
        return ""

    form_lines = []
    for line in form_fd:
        str_line = line.decode(encoding=encoding)
        form_lines.append(str_line)

    to_lines = []
    for line in to_fd:
        str_line = line.decode(encoding=encoding)
        to_lines.append(str_line)

    html = difflib.HtmlDiff()
    return html.make_file(form_lines,to_lines)



# q = (SVNDiffFileAsHtml("https://pcw21941.g-bits.com/svn/test/demo.css", 1, "HEAD"))
# with open("test.html","w") as pf:
#     pf.write(q)
#



