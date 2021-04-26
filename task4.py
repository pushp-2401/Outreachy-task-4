# import pywikibot
# site = pywikibot.Site("wikidata", "wikidata")
# repo = site.data_repository()
# item = pywikibot.ItemPage(repo, u"Q4115189")

# qualifier = pywikibot.Claim(repo, u'P276')
# target = pywikibot.ItemPage(repo, "Q183")
# qualifier.setTarget(target)
# claim.addQualifier(qualifier, summary=u'Adding a qualifier.')

import pywikibot
site = pywikibot.Site("wikidata", "wikidata")
repo = site.data_repository()
item1 = pywikibot.ItemPage(repo, u"Q85783283")
item =pywikibot.ItemPage(repo, u"Q15961638")

########## adding date of inception############                 
dateclaim = pywikibot.Claim(repo, u'P571')
dateOfInception = pywikibot.WbTime(year=2015, month=8, day=15)
dateclaim.setTarget(dateOfInception)
item.addClaim(dateclaim, summary=u'Adding dateOfInception')   #added date of icneption to bihar museum's page  https://www.wikidata.org/wiki/Q15961638


#################adding image##################
imageclaim =  pywikibot.Claim(repo, u'P18')
imagetarget = pywikibot.FilePage(repo, title="File:bihar_museum.jpg")
imageclaim.setTarget(imagetarget)
item.addClaim(imageclaim, summary=u'Adding photo')        #added image to bihar museum's page


######### adding identifier################
Identifiersclaim = pywikibot.Claim(repo, u'P214')
Identifiersclaim.setTarget(u'http://viaf.org/viaf/158295799')   #added viaf id to maithili akadami's page Q85783283
item1.addClaim(Identifiersclaim, summary=u'Adding VIAF ID')        #https://www.wikidata.org/wiki/Q85783283


############# adding reference#################
retrieved = pywikibot.Claim(repo, u'P214', is_reference=True)
#date = pywikibot.WbTime(year=2014, month=3, day=20, site=site)
retrieved.setTarget(u'https://viaf.org/viaf/158295799/#Maithil%C4%AB_Ak%C4%81dam%C4%AB')
Identifiersclaim.addSources([retrieved], summary=u'Adding sources.')