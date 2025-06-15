from unstructured.partition.pdf import partition_pdf


# document per local path or URL
source = "/Volumes/FAT_VERB/learning/topics/security/threat-modelling/effectivethreatinvestigationforsocanalysts.pdf"
# "https://arxiv.org/pdf/2408.09869"  
# /Volumes/FAT_VERB/learning/topics/security/threat-modelling/threatmodeling.pdf


# Returns a List[Element] present in the pages of the parsed pdf document
elements = partition_pdf(source)

print("\n\n".join([str(el) for el in elements]))