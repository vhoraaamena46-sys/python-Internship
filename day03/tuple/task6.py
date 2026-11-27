admin={"Read","Write","Execute","Delete"}
editor={"Read","Write","Execute"}


required_permissions="Read"

if required_permissions in editor:
    print("Editor has  required permissions.")
else:
    print("Editor does not have  required permissions.")