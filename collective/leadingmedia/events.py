# Handling Events

def reindexMedia(object, event):
    """
        Reindexes Media catalog indexes on the parent
    """

    if object.id != "whatson" and object.id != 'slideshow':
        #print "Reindexing %s"%object.id
        object.reindexObject(idxs=["hasMedia"])
        object.reindexObject(idxs=["leadMedia"])

        if hasattr(object.getParentNode(), "meta_type"):
            if object.getParentNode().meta_type == "Dexterity Container" and object.getParentNode().portal_type != "Folder":
                reindexMedia(object.getParentNode(), event)
    
    elif object.id == 'slideshow':
        if hasattr(object.getParentNode(), "meta_type"):
            if object.getParentNode().meta_type == "Dexterity Container" and object.getParentNode().portal_type != "Folder":
                reindexMedia(object.getParentNode(), event)

# AUTO CROPPING

def imageObjectCreated(ob, event):
    print "Image object created"
