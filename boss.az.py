# from bs4 import BeautifulSoup
# import requests
# import re
#
# url = "https://boss.az"
# result=requests.get(url)
# soup=BeautifulSoup(result.text,"html.parser")
#
#
#
# link=[]
# for i in soup.findAll(class_="collection-i-link"):
#     # print(i)
#     for j in (str(i)).split('href="'):
#         for m in j.split('"'):
#             # print(m)
#             link.append(m)
# print(link)
# links=[]
# for d in link:
#     # print(d)
#     if "/vacancies/" in d:
#         url_2 = "https://boss.az"+d
#         result_2 = requests.get(url_2)
#         soup_2 = BeautifulSoup(result_2.text, "html.parser")
#         # print(soup_2.find(class_="phone params-i-val").text)
#         # print(soup_2.find(class_="")
#         for i in str(soup_2).split():
#             if 'data-cfemail="' in i:
#                 for j in i.split('data-cfemail="'):
#                     for m in j.split('"'):
#                         links.append(m)
# def cfDecodeEmail(encodedString):
#     r = int(encodedString[:2],16)
#     email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
#
#     return email
# print(cfDecodeEmail("8ae6fffeece3fcefe6e3f0ebeeefbbcaede7ebe3e6a4e9e5e7"))
#
# # mail = open("mails.txt", "a")
# for i in links:
#
#     if len(i)>26:
#         # mail.write(cfDecodeEmail(i))
#         # mail.write("\n")
#         # print(i)
#         print(cfDecodeEmail(i))
#         if cfDecodeEmail(i)=="boss@boss.az":
#             print(len(i))
# for j in links:
#     print(j)
# url = "https://boss.az/categories/resumes"
# result = requests.get(url)
# soup = BeautifulSoup(result.text,"html.parser")
# link=[]
# for i in soup.findAll(class_="collection-i-link"):
#     # print(i)
#     for j in (str(i)).split('href="'):
#         for m in j.split('">'):
#             # print(m)
#             link.append(m)
# links=[]
# for d in link:
#     # print(d)
#     if "/resumes/" in d:
#         url_2 = "https://boss.az"+d
#         result_2 = requests.get(url_2)
#         soup_2 = BeautifulSoup(result_2.text, "html.parser")
#         print(soup_2.find(class_="phone params-i-val").text)
#         # print(soup_2.find(class_="")
#         for i in str(soup_2).split():
#             if 'data-cfemail="' in i:
#                 for j in i.split('data-cfemail="'):
#                     for m in j.split('">[email'):
#                         links.append(m)
#
#
#
#
# def cfDecodeEmail(encodedString):
#     r = int(encodedString[:2],16)
#     email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
#
#     return email
# print(cfDecodeEmail("8ae6fffeece3fcefe6e3f0ebeeefbbcaede7ebe3e6a4e9e5e7"))
#
# mail = open("mails.txt", "a")
# for i in links:
#
#     if len(i)>26:
#         mail.write(cfDecodeEmail(i))
#         mail.write("\n")
#         print(i)
#         print(cfDecodeEmail(i))
#         if cfDecodeEmail(i)=="boss@boss.az":
#             print(len(i))
#
#
#
# # url_2 = "https://boss.az/resumes/553422"
# # result_2 = requests.get(url_2)
# # soup_2 = BeautifulSoup(result_2.text, "html.parser")
# # for i in str(soup_2).split():
# #     if 'data-cfemail="' in i:
# #         for j in i.split('data-cfemail="'):
# #             for m in j.split('">[email'):
# #                 links.append(m)

print(0.8631690889755406>0.8572459782758146)

