"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install pyttsx3
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

import os
from pathlib import Path

import api_tts_text_to_speech_pyttsx3 as api


# document per local path or URL
texts = [
   "Hi Moljac. What's up?",
   "Hello, world! This is a text-to-speech example using PYTTSX3.",
]

root="../../../../../../data"
root_sports_book="/Users/Shared/Projects/e/learning/books/topics/sports/Moljac_Knjiga"

# document per local path or URL
sources = [
   f"{root}/eBooks-main/current/maui/Enterprise-Application-Patterns-Using-.NET-MAUI.pdf",
   f"{root}/eBooks-main/current/xamarin-forms/Enterprise-Application-Patterns-using-XamarinForms.pdf",
#   f"{root}/eBooks-main/current/azure-quick-start/Azure-Quick-Start-for-NET-Developers.pdf",
#   f"{root}/eBooks-main/current/microservices/NET-Microservices-Architecture-for-Containerized-NET-Applications.pdf",
#   f"{root}/eBooks-main/current/porting-existing-aspnet-apps/Porting-Existing-ASP.NET-Apps-to-.NET.pdf",
#   f"{root}/eBooks-main/current/blogs/net7perf/Performance-Improvements-in-NET7.pdf",
#   f"{root}/eBooks-main/current/cloud-native/Architecting-Cloud-Native-NET-Apps-for-Azure.pdf",
#   f"{root}/eBooks-main/current/grpc-for-wcf-developers/gRPC-for-WCF-Developers.pdf",
#   f"{root}/eBooks-main/current/blazor-for-web-forms-developers/Blazor-for-ASP-NET-Web-Forms-Developers.pdf",
#   f"{root}/eBooks-main/current/containerized-lifecycle/Containerized-Docker-Application-Lifecycle-with-Microsoft-Platform-and-Tools.pdf",
#   f"{root}/eBooks-main/current/serverless/Serverless-apps-Architecture-patterns-and-Azure-implementation.pdf",
#   f"{root}/eBooks-main/current/dotnet-for-java-developers/dotnet-for-java-developers-ebook.pdf",
#   f"{root}/eBooks-main/current/devops-aspnet-core/DevOps-for-ASP.NET-Core-Developers.pdf",
#   f"{root}/eBooks-main/current/architecting-modern-web-apps-azure/Architecting-Modern-Web-Applications-with-ASP.NET-Core-and-Azure.pdf",
#   f"{root}/eBooks-main/current/dapr-for-net-developers/Dapr-for-NET-Developers.pdf",
#   f"{root}/eBooks-main/current/modernize-with-azure-containers/Modernize-Existing-.NET-applications-with-Azure-cloud-and-Windows-Containers.pdf",
#   f"{root}/eBooks-main/current/modernize-desktop-apps/Modernize-Desktop-Apps-on-Windows-with-NET.pdf"
]

def main():
   for text in texts:
      print(f"pyttsx3 <- text = {text}")
      api.speak(text)

   for source in sources:
      print(f"pyttsx3 <- source = {source}")

      filename = f"{source}.hwaifs/text/python/docling/content.md"
      file = Path(filename)
      text = Path(filename).read_text()
      paragraphs = text.split('\n\n')

      for paragraph in paragraphs:
         api.speak(paragraph)


if __name__ == '__main__':
    main()

