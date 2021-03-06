# Handling indexes

from plone.indexer.decorator import indexer
from collective.leadingmedia.interfaces import ICanContainMedia
from plone.dexterity.interfaces import IDexterityContainer
from plone.app.contenttypes.interfaces import ICollection, IFolder

@indexer(IDexterityContainer)
def hasMedia(object, **kw):
    return ICanContainMedia(object).hasMedia()

@indexer(IDexterityContainer)
def leadMedia(object, **kw):
    lead = ICanContainMedia(object).getLeadMedia()
    if lead is not None:
        if hasattr(lead, 'getURL'):
            return lead.getURL()
        else:
            return lead.absolute_url()


@indexer(ICollection)
def collection_hasMedia(object, **kw):
    return ICanContainMedia(object).hasMedia()

@indexer(ICollection)
def collection_leadMedia(object, **kw):
    lead = ICanContainMedia(object).getLeadMedia()
    if lead is not None:
        if hasattr(lead, 'getURL'):
            return lead.getURL()
        else:
            return lead.absolute_url()

@indexer(IFolder)
def folder_hasMedia(object, **kw):
    return ICanContainMedia(object).hasMedia()

@indexer(IFolder)
def folder_leadMedia(object, **kw):
    lead = ICanContainMedia(object).getLeadMedia()
    if lead is not None:
        if hasattr(lead, 'getURL'):
            return lead.getURL()
        else:
            return lead.absolute_url()
