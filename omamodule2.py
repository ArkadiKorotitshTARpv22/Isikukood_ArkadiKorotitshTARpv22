def sugu(ikood:str)->str:
    """Kui esimene t‰ht on [1,2,3,4,5,6], siis
     m‰‰rame sugu
     param str ikood: Isikukood
     rtype: str
    """
    ikood_list=list(map(int,ikood))
    if ikood_list[0] in [1,3,5]:
        s="mees"
    elif ikood_list[0] in [2,4,6]:
        s="naine"
    else:
        s="viga"
    return s
