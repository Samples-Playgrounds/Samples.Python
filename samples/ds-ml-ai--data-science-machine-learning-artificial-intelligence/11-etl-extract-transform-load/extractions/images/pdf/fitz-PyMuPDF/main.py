"""
rm -fr .venv
python -m venv .venv
source .venv/bin/activate
pip install PyMuPDF

pip install -r requirements.txt
python main.py
"""

sources = [
    '../../../../../../data/eBooks-main/current/architecting-modern-web-apps-azure/Architecting-Modern-Web-Applications-with-ASP.NET-Core-and-Azure.pdf',
    '../../../../../../data/eBooks-main/current/microservices/NET-Microservices-Architecture-for-Containerized-NET-Applications.pdf',
    '../../../../../../data/eBooks-main/current/porting-existing-aspnet-apps/Porting-Existing-ASP.NET-Apps-to-.NET.pdf',
    '../../../../../../data/eBooks-main/current/azure-quick-start/Azure-Quick-Start-for-NET-Developers.pdf',
    '../../../../../../data/eBooks-main/current/blogs/net7perf/Performance-Improvements-in-NET7.pdf',
    '../../../../../../data/eBooks-main/current/cloud-native/Architecting-Cloud-Native-NET-Apps-for-Azure.pdf',
    '../../../../../../data/eBooks-main/current/grpc-for-wcf-developers/gRPC-for-WCF-Developers.pdf',
    '../../../../../../data/eBooks-main/current/blazor-for-web-forms-developers/Blazor-for-ASP-NET-Web-Forms-Developers.pdf',
    '../../../../../../data/eBooks-main/current/containerized-lifecycle/Containerized-Docker-Application-Lifecycle-with-Microsoft-Platform-and-Tools.pdf',
    '../../../../../../data/eBooks-main/current/serverless/Serverless-apps-Architecture-patterns-and-Azure-implementation.pdf',
    '../../../../../../data/eBooks-main/current/dotnet-for-java-developers/dotnet-for-java-developers-ebook.pdf',
    '../../../../../../data/eBooks-main/current/devops-aspnet-core/DevOps-for-ASP.NET-Core-Developers.pdf',
    '../../../../../../data/eBooks-main/current/maui/Enterprise-Application-Patterns-Using-.NET-MAUI.pdf',
    '../../../../../../data/eBooks-main/current/architecting-modern-web-apps-azure/Architecting-Modern-Web-Applications-with-ASP.NET-Core-and-Azure.pdf',
    '../../../../../../data/eBooks-main/current/dapr-for-net-developers/Dapr-for-NET-Developers.pdf',
    '../../../../../../data/eBooks-main/current/modernize-with-azure-containers/Modernize-Existing-.NET-applications-with-Azure-cloud-and-Windows-Containers.pdf',
    '../../../../../../data/eBooks-main/current/modernize-desktop-apps/Modernize-Desktop-Apps-on-Windows-with-NET.pdf',
    '../../../../../../data/eBooks-main/current/xamarin-forms/Enterprise-Application-Patterns-using-XamarinForms.pdf',
]

import api_fitz_PyMuPDF_images as api

for source in sources:

    results = api.extract_images_from_pdf(source)
