
root="../../../../../../../data"
root_sports_book="/Users/Shared/Projects/e/learning/books/topics/sports/Moljac_Knjiga"
root_sports_reports_lab_kif="/Users/Shared/Projects/d/hw/apps/Ph4ct3x/gl/Ph4ct3x.Docs/users/lara/diagnostics/kif/"


#-----------------------------------------------------------------------------------------------------------------------
# libraries
libs_extraction_from_documents_pdf = [
                                       "PyMuPDF",
                                       "PyPDF2",
                                       "docling",
                                       "docTR",
                                       "kreuzberg",
                                       "marker",
                                       "markitdown",
                                       "pdfium2",
                                       "pdfminer.six",
                                       "pdfplumber",
                                       "pymupdf4llm-c",
                                       "pymupdf4llm",
                                       "pytesseract",
                                       "unstructured",
                                       ]
#-----------------------------------------------------------------------------------------------------------------------
# document per local path or URL
files_private_kif_diagnostic = [
   f"{root_sports_reports_lab_kif}/201907/FINAL-REPORT-Lara-Cvjetko-2019-07.pdf",
   f"{root_sports_reports_lab_kif}/201809/FINAL-REPORT-Cvjetko-Lara-Judo-2018-09.pdf",
   f"{root_sports_reports_lab_kif}/201711/Lara Cvjetko-FINAL REPORT-Judo-2017-11.pdf",
]

files_private_book_pdf = [
   f"{root_sports_book}/RUKOPIS_ver_Final.pdf",
]
files_private_book_docx = [
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
]

files_private_book = [
    *files_private_book_pdf,
    *files_private_book_docx,
]

files_documents_pdfs_legal = [
    "/Volumes/xFAT-1TB-2/e/personal-private/judo/HJS/01-pravno/DORH/02-kaznena-prijava-koraci/TODO/mails/20251201-03-czm-pravobraniteljica--odgovor-akcijski-plan/docs/MAIL_001119.pdf",
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
]

files_documents_pdfs_ebooks = [
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
]

files_documents_pdfs_cheat_sheets = [
   f"{root}/cheat-sheets/cheat-sheet.pdf",
   f"{root}/cheat-sheets/cheat.pdf",
   f"{root}/cheat-sheets/SQL-Cheat-Sheet.pdf",
   f"{root}/cheat-sheets/gdb.pdf",
   f"{root}/cheat-sheets/python-cheatsheet.pdf",
   f"{root}/cheat-sheets/Nmap-Cheat-Sheet.pdf",
   f"{root}/cheat-sheets/python-cheatsheets.pdf",
   f"{root}/cheat-sheets/Pandas_Cheat_Sheet.pdf",
   f"{root}/cheat-sheets/docker_cheatsheet.pdf",
   f"{root}/cheat-sheets/CSE102-CheatSheetCSSLong.pdf",
   f"{root}/cheat-sheets/keyboard-shortcuts-macos.pdf",
   f"{root}/cheat-sheets/GDB Cheat Sheet.pdf",
   f"{root}/cheat-sheets/git-cheat-sheet-education.pdf",
   f"{root}/cheat-sheets/csscheatsheet.pdf",
   f"{root}/cheat-sheets/htmlcheatsheet.pdf",
   f"{root}/cheat-sheets/keyboard-shortcuts-windows.pdf",
   f"{root}/cheat-sheets/analyzing-malicious-document-files.pdf",
   f"{root}/cheat-sheets/CheatSheet.pdf",
   f"{root}/cheat-sheets/git-cheat-sheet.pdf",
   f"{root}/cheat-sheets/vi_cheat_sheet.pdf",
   f"{root}/cheat-sheets/multibagg-ai-cheat-sheet-v1.pdf",
   f"{root}/cheat-sheets/UNIXCheatSheet.pdf",
]


#  "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/RUKOPIS_ver_Final.pdf",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/microsoft/dotnet/maui/NET_MAUI_in_Action.pdf",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/microsoft/dotnet/maui/mvvmpatterninnetmaui.pdf",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/doc_files/13.\ Funkcionalna\ procjena\ pokreta.docx",
#  "/Volumes/xFAT-1TB-2/learning/books/topics/sports/Moljac_Knjiga/doc_files/14.\ Literatura.docx",

#  "/Volumes/FAT_VERB/learning/books/topics/microsoft/architecture/adevelopersguidetonetinazure.pdf"
#   "https://arxiv.org/pdf/2408.09869"

files_documents_rtfs = [
   f"{root}/microsoft/rtf/file-sample_1MB.rtf",
   f"{root}/microsoft/rtf/file-sample_300kB.rtf",
   f"{root}/microsoft/rtf/file-sample_100kB.rtf",
   f"{root}/microsoft/rtf/file-sample_500kB.rtf",
]

files_documents_docs = [
   f"{root}/microsoft/word-docx-doc/file-sample_500kB.doc",
   f"{root}/microsoft/word-docx-doc/file-sample_1MB.doc",
   f"{root}/microsoft/word-docx-doc/file-sample_100kB.doc",
]
files_documents_docxs = [
   f"{root}/pravno/zakoni/kazneni-zakon.docx",
   f"{root}/microsoft/word-docx-doc/NET 6.0 - ASP.NET Core Project Templates.Web.EN.docx",
   f"{root}/microsoft/word-docx-doc/visualStudioAsp.netTutorial.docx",
   f"{root}/microsoft/word-docx-doc/file-sample_100kB.docx",
   f"{root}/microsoft/word-docx-doc/file-sample_500kB.docx",
   f"{root}/microsoft/word-docx-doc/file-sample_1MB.docx",
   f"{root}/microsoft/word-docx-doc/wake-up-and-code--workshop/Day2-03-AzureFunctions-Email.docx",
   f"{root}/microsoft/word-docx-doc/wake-up-and-code--workshop/Day1-01-AspNetCore-Mvc.docx",
   f"{root}/microsoft/word-docx-doc/wake-up-and-code--workshop/Day3-02-Azure-ADB2C.docx",
   f"{root}/microsoft/word-docx-doc/wake-up-and-code--workshop/Day2-01C-EFCore-RazorPages.docx",
   f"{root}/microsoft/word-docx-doc/wake-up-and-code--workshop/Day2-01B-AspNetCore-Razor-Long.docx",
   f"{root}/microsoft/word-docx-doc/wake-up-and-code--workshop/Day3-01-AppService-Deploy.docx",
   f"{root}/microsoft/word-docx-doc/wake-up-and-code--workshop/Day3-03-AspNetCore-Authr.docx",
   f"{root}/microsoft/word-docx-doc/Vježba-Izrada-jednostavne-ASP-NET-App.docx",
   f"{root}/microsoft/word-docx-doc/NET MAUI VS Code Extension.Windows, Linux, Mac.WCAG_22.docx",
]

files_documents_epubs = [
   f"{root}/eBooks-main/archives/microservices/NET-Microservices-Architecture-for-Containerized-NET-Applications-v1.epub",
   f"{root}/eBooks-main/archives/microservices/NET-Microservices-Architecture-for-Containerized-NET-Applications-v2.1.01.epub",
   f"{root}/eBooks-main/archives/microservices/NET-Microservices-Architecture-for-Containerized-NET-Applications-v2.2.0.epub",
   f"{root}/eBooks-main/archives/microservices/NET-Microservices-Architecture-for-Containerized-NET-Applications-v1.1.epub",
   f"{root}/eBooks-main/archives/microservices/NET-Microservices-Architecture-for-Containerized-NET-Applications-v2.2.1.epub",
   f"{root}/eBooks-main/archives/microservices/NET-Microservices-Architecture-for-Containerized-NET-Applications-v2.1.03.epub",
   f"{root}/eBooks-main/archives/microservices/es/Microservicios-NET-Arquitectura-para-aplicaciones-NET-Contenerizadas-es-ES-v2.0.5.epub",
   f"{root}/eBooks-main/archives/microservices/NET-Microservices-Architecture-for-Containerized-NET-Applications-v2.1.02.epub",
   f"{root}/eBooks-main/archives/containerized-lifecycle/Containerized-Docker-Application-Lifecycle-with-Microsoft-Platform-and-Tools-v1.1.epub",
   f"{root}/eBooks-main/archives/containerized-lifecycle/Containerized-Docker-Application-Lifecycle-with-Microsoft-Platform-and-Tools-v1.2.epub",
   f"{root}/eBooks-main/archives/serverless/Serverless-apps-Architecture-patterns-and-Azure-implementation-v1.epub",
   f"{root}/eBooks-main/archives/architecting-modern-web-apps-azure/Architecting-Modern-Web-Applications-with-ASP.NET-Core-and-Azure-v2.0.epub",
   f"{root}/eBooks-main/archives/architecting-modern-web-apps-azure/Architecting-Modern-Web-Applications-with-ASP.NET-Core-and-Azure-v2.2.1.epub",
   f"{root}/eBooks-main/archives/architecting-modern-web-apps-azure/Architecting-Modern-Web-Applications-with-ASP.NET-Core-and-Azure-v2.2.0.epub",
   f"{root}/eBooks-main/archives/architecting-modern-web-apps-azure/Architecting-Modern-Web-Applications-with-ASP.NET-Core-and-Azure-v2.1.epub",
   f"{root}/eBooks-main/archives/modernize-with-azure-containers/Modernize-Existing-.NET-applications-with-Azure-cloud-and-Windows-Containers-v2.2.epub",
   f"{root}/eBooks-main/archives/modernize-with-azure-containers/Modernize-Existing-.NET-applications-with-Azure-cloud-and-Windows-Containers-v1.epub",
   f"{root}/eBooks-main/archives/modernize-with-azure-containers/Modernize-Existing-.NET-applications-with-Azure-cloud-and-Windows-Containers-v2.0.epub",
   f"{root}/epub/Around the World in 28 Languages.epub",
   f"{root}/epub/sample1.epub",
   f"{root}/epub/famouspaintings.epub",
   f"{root}/epub/Sway.epub",
   f"{root}/epub/Alices Adventures in Wonderland.epub",
]

files_excel_xls = [
   f"{root}/microsoft/excel-xlsx-xls/file_example_XLS_1000.xls",
   f"{root}/microsoft/excel-xlsx-xls/file_example_XLS_100.xls",
   f"{root}/microsoft/excel-xlsx-xls/file_example_XLS_5000.xls",
   f"{root}/microsoft/excel-xlsx-xls/file_example_XLS_10.xls",
   f"{root}/microsoft/excel-xlsx-xls/file_example_XLS_50.xls",
]

root="../../../../../../data/images/"
# document per local path or URL
files_images = [
    f"{root}/maui/architecture-diagram.png",
    f"{root}/maui/maui-overview.png",
    f"{root}/android/architecture1.png",
    f"{root}/crime-orgs/judo/Screenshot 2025-11-18 at 13.00.30.png",
    f"{root}/crime-orgs/judo/Screenshot 2025-11-18 at 13.00.30.png",
    f"{root}/dontetconf/2025/Screenshot 2025-11-17 at 11.35.46.edited.png",
    f"{root}/dontetconf/2025/Screenshot 2025-11-17 at 11.35.46.png"
]

files_documents_pdfs = \
            files_documents_pdfs_ebooks \
            + \
            files_documents_pdfs_legal

files_images_web = [
        'https://upload.wikimedia.org/wikipedia/commons/b/bd/Army_Reserves_Recruitment_Banner_MOD_45156284.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/e8/FseeG2QeLXo.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/b/b4/EUBanana-500x112.jpg'
]

youtube_video_ids = [
    "iybdUPYXPEw",
    "845fNBa_R_4",
    "JuXgIqZjRBQ",
    "OOcv9Mj0Fsc",
    "DlsTxZdgklw",
    "OOcv9Mj0Fsc",
    "ck5nw7R1uEs",
    "x37O-PUBvw0",
    "WqFt6YHHy50",
    "nUlomY7RsIg",
    "T__1QViXUxk",
#    "",
]


files = \
         files_private_book \
         + \
         files_private_kif_diagnostic \
         + \
         files_documents_pdfs \
         + \
         files_documents_docxs \
         + \
         files_documents_docs


files += [
]


sources = files
# only smaller documents for testing
# sources = files_documents_pdfs_cheat_sheets