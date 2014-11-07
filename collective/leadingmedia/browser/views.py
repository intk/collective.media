from Acquisition import aq_inner
from zope.component import getUtility
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.interfaces import IPloneSiteRoot


class FolderLeadMediaView(BrowserView):

    template = ViewPageTemplateFile('templates/folder_leadmedia_view.pt')

    