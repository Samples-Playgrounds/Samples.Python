"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install docling pandas
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""


import api_gmft_tables as api

root="../../../../../../../data"

# document per local path or URL
sources = [
   "/Users/moljac/Downloads/20250913/Zapisnik OS NZG K-226-2022-48 od 12.02.2024. - Nastavak glavne rasprave dana 12.02.2024. u 10_00 sati.pdf",
   f"{root}/pravno/zakoni/zakon_o_sportskoj_inspekciji_nn_86_12.pdf",
   f"{root}/pravno/zakoni/kazneni-zakon.docx",
   f"{root}/pravno/zakoni/zakon-o-sportu-NN-19-16.pdf",
   f"{root}/pravno/zakoni/zakon-o-sportu-2022.pdf",
   f"{root}/pravno/zakoni/Kazneni-zakon.pdf",
   f"{root}/pravno/zakoni/55-4.pdf",
   f"{root}/pravno/satuti/hjs/status-HJS-a-2024.pdf",
   f"{root}/pravno/satuti/hoo/Statut-HOO-a_procisceni-tekst_srpanj-2024.pdf",
   f"{root}/pravno/satuti/gnk-dinamo/Nacrt+Prijedloga+Statuta+GNK+Dinamo.pdf",
   f"{root}/pravno/satuti/gnk-dinamo/Prijedlog_Statuta_GNK_Dinamo_finalno_20250811_za+IO.pdf",
   f"{root}/pravno/satuti/gnk-dinamo/statut-dinamo.2023.pdf",
   f"{root}/pravno/satuti/gnk-dinamo/O Statutu_250814_100408.pdf",
   f"{root}/pravno/dokumenti/hjs-zppi-2023-rjesenje.2.600dpi.compressed.pdf",
   f"{root}/pravno/dokumenti/Rješenje - odbijanje zahtjeva Miljenko CVJETKO - 18.8.2025. .pdf",

   f"{root}/eBooks-main/current/maui/Enterprise-Application-Patterns-Using-.NET-MAUI.pdf",
   f"{root}/eBooks-main/current/xamarin-forms/Enterprise-Application-Patterns-using-XamarinForms.pdf",
   f"{root}/eBooks-main/current/azure-quick-start/Azure-Quick-Start-for-NET-Developers.pdf",
   f"{root}/eBooks-main/current/microservices/NET-Microservices-Architecture-for-Containerized-NET-Applications.pdf",
   f"{root}/eBooks-main/current/porting-existing-aspnet-apps/Porting-Existing-ASP.NET-Apps-to-.NET.pdf",
   f"{root}/eBooks-main/current/blogs/net7perf/Performance-Improvements-in-NET7.pdf",
   f"{root}/eBooks-main/current/cloud-native/Architecting-Cloud-Native-NET-Apps-for-Azure.pdf",
   f"{root}/eBooks-main/current/grpc-for-wcf-developers/gRPC-for-WCF-Developers.pdf",
   f"{root}/eBooks-main/current/blazor-for-web-forms-developers/Blazor-for-ASP-NET-Web-Forms-Developers.pdf",
   f"{root}/eBooks-main/current/containerized-lifecycle/Containerized-Docker-Application-Lifecycle-with-Microsoft-Platform-and-Tools.pdf",
   f"{root}/eBooks-main/current/serverless/Serverless-apps-Architecture-patterns-and-Azure-implementation.pdf",
   f"{root}/eBooks-main/current/dotnet-for-java-developers/dotnet-for-java-developers-ebook.pdf",
   f"{root}/eBooks-main/current/devops-aspnet-core/DevOps-for-ASP.NET-Core-Developers.pdf",
   f"{root}/eBooks-main/current/architecting-modern-web-apps-azure/Architecting-Modern-Web-Applications-with-ASP.NET-Core-and-Azure.pdf",
   f"{root}/eBooks-main/current/dapr-for-net-developers/Dapr-for-NET-Developers.pdf",
   f"{root}/eBooks-main/current/modernize-with-azure-containers/Modernize-Existing-.NET-applications-with-Azure-cloud-and-Windows-Containers.pdf",
   f"{root}/eBooks-main/current/modernize-desktop-apps/Modernize-Desktop-Apps-on-Windows-with-NET.pdf"

#  "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/microsoft/dotnet/maui/NET_MAUI_in_Action.pdf",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/microsoft/dotnet/maui/mvvmpatterninnetmaui.pdf",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/doc_files/13.\ Funkcionalna\ procjena\ pokreta.docx",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/doc_files/14.\ Literatura.docx",
]
#  "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#   "https://arxiv.org/pdf/2408.09869"


for source in sources:
   tables, doc = api.ingest_pdf(source)
   doc.close() # once you're done with the document

