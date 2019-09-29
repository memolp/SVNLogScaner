# -*- coding:utf-8 -*-

"""
  SVN 常用的命令封装
"""

import subprocess


class SVNCommand(object):
    """
    命令行工具
    """
    def __init__(self, command):
        """
        svn命令工具
        :param command:
        """
        self.mCommand = command

    def execute(self):
        """
        执行命令，并返回字符串
        :return: py2 str py3 bytes
        """
        p = subprocess.Popen(self.mCommand, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        if p is None or p.stdout is None:
            return ""
        return p.stdout.read()

    def executeAsfd(self):
        """
        执行命令，返回文件对象fd
        :return:
        """
        p = subprocess.Popen(self.mCommand, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        if p is None or p.stdout is None:
            return None
        return p.stdout

    @staticmethod
    def GetSVNLog(url, *args, **kwargs):
        """
        获取url的提交svn记录
        :param url:
        :param args:
        :param kwargs:
        :return: 返回py2 str py3 bytes
        """
        cmd_str = "svn log {0}".format(url)
        for option in args:
            cmd_str += " -{0}".format(option)
        for key, value in kwargs.items():
            cmd_str += " -{0} {1}".format(key,value)
        cmd = SVNCommand(cmd_str)
        return cmd.execute()

    @staticmethod
    def GetSVNLogfd(url, *args, **kwargs):
        """
        获取url的提交svn记录
        :param url:
        :param args:
        :param kwargs:
        :return: 返回fd
        """
        cmd_str = "svn log {0}".format(url)
        for option in args:
            cmd_str += " -{0}".format(option)
        for key, value in kwargs.items():
            cmd_str += " -{0} {1}".format(key, value)
        print(cmd_str)
        cmd = SVNCommand(cmd_str)
        return cmd.executeAsfd()

    @staticmethod
    def GetSVNVersionFile(url, version):
        """
        获取指定文件，指定版本的内容
        :param url:
        :param version:
        :return: py2 str py3 bytes
        """
        cmd_str = "svn cat {0} -r {1}".format(url, version)
        cmd = SVNCommand(cmd_str)
        return cmd.execute()

    @staticmethod
    def GetSVNVersionFilefd(url, version):
        """
        获取指定文件，指定版本的内容
        :param url:
        :param version:
        :return: 返回fd
        """
        cmd_str = "svn cat {0} -r {1}".format(url, version)
        cmd = SVNCommand(cmd_str)
        return cmd.executeAsfd()


