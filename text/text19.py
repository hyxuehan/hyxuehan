# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################


class MyFrame1 (wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
		                  size=wx.Size(652, 383), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		self.m_menu1 = wx.Menu()
		self.Bind(wx.EVT_RIGHT_DOWN, self.MyFrame1OnContextMenu)

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.m_treeCtrl1 = wx.TreeCtrl(
			self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 300), wx.TR_DEFAULT_STYLE)
		bSizer1.Add(self.m_treeCtrl1, 0, wx.ALL, 5)

		self.SetSizer(bSizer1)
		self.Layout()

		self.Centre(wx.BOTH)

	def __del__(self):
		pass

	def MyFrame1OnContextMenu(self, event):
		self.PopupMenu(self.m_menu1, event.GetPosition())



app = wx.App()
mainwin = MyFrame1(None)
mainwin.Show()
app.MainLoop()