"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install extractous
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import api_text_extraction_extractous as api

root="../../../../../../../data"
root_sports_book="/Users/Shared/Projects/e/learning/books/topics/sports/Moljac_Knjiga"
root_sports_reports_lab_kif="/Users/Shared/Projects/d/hw/apps/Ph4ct3x/gl/Ph4ct3x.Docs/users/lara/diagnostics/kif/"

# document per local path or URL
sources = [
   f"{root_sports_reports_lab_kif}/201907/FINAL-REPORT-Lara-Cvjetko-2019-07.pdf",
   f"{root_sports_reports_lab_kif}/201809/FINAL-REPORT-Cvjetko-Lara-Judo-2018-09.pdf",
   f"{root_sports_reports_lab_kif}/201711/Lara Cvjetko-FINAL REPORT-Judo-2017-11.pdf",

   f"{root_sports_book}/RUKOPIS_ver_Final.pdf",
   f"{root_sports_book}/doc_files/2. Testovi jakosti.docx",
   f"{root_sports_book}/doc_files/1. Uvod.docx",
   f"{root_sports_book}/doc_files/14. Literatura.docx",
   f"{root_sports_book}/doc_files/7. Testovi ravnoteze.docx",
   f"{root_sports_book}/doc_files/3. Testovi brzine.docx",
   f"{root_sports_book}/doc_files/0. Naslovnica.docx",
   f"{root_sports_book}/doc_files/4. Testovi izdrzljivosti.docx",
   f"{root_sports_book}/doc_files/9. Longitudinalna dimenzionalnost skeleta.docx",
   f"{root_sports_book}/doc_files/11. Volumen i masa tijela.docx",
   f"{root_sports_book}/doc_files/10. Transverzalna dimenzionalnost skeleta.docx",
   f"{root_sports_book}/doc_files/13. Funkcionalna procjena pokreta.docx",
   f"{root_sports_book}/doc_files/12. Potkožno masno tkivo.docx",
   f"{root_sports_book}/doc_files/Sadržaj.docx",
   f"{root_sports_book}/doc_files/6. Testovi agilnosti.docx",
   f"{root_sports_book}/doc_files/5. Testovi koordinacije.docx",
   f"{root_sports_book}/doc_files/8. Testovi fleksibilnosti.docx",
   "/Volumes/xFAT-1TB-2/e/personal-private/judo/HJS/01-pravno/DORH/02-kaznena-prijava-koraci/TODO/mails/20251201-02-czm-pravobraniteljica--odgovor-akcijski-plan/docs/MAIL_001119.pdf",
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

def main():
   for source in sources:
      print(f"docling <- source = {source}")
      result_txt = api.extract_text_to_file_from_any_document(source)


if __name__ == '__main__':
    main()

