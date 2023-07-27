
# if __name__ == '__main__':
#     print('cargando...')
#     import requests
#     from bs4 import BeautifulSoup
#     url = "https://google.com"
#     print(url)
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")
#     print(soup.input.attrs)
    # contenido = """
    # <html lang="es">
    # <head>
    #     <meta charset="UTF-8">
    #     <title>Página de prueba</title>
    # </head>
    # <body>
    # <div id="main" class="full-width">
    #     <h1>El título de la página</h1>
    #     <p>Este es el primer párrafo</p>
    #     ...
    # </div>
    # <div id="main2" class="full-width">
    #     <h1>El título de la página 2</h1>
    #     <p>Este es el primer párrafo 2</p>
    #     ...
    # </div>
    # </body>
    # </html>
    # """
    # soup = BeautifulSoup(contenido, 'lxml')
    # print(soup.text)#trae los h1 de la pagina
    # div_main = soup.div
    # print(div_main['id'])#trae el id del div
    # print(div_main.attrs)




    # #easy job scraper example
    # #------------------------
    # import requests  # python3 -m pip install requests beautifulsoup4
    # from bs4 import BeautifulSoup
    #
    # url = "https://www.seek.co.nz/python-jobs?salaryrange=100000-999999&salarytype=annual"
    #
    # if "__main__" == __name__:#solo se ejecute cuando el archivo se esté ejecutando directamente como el programa principal y no cuando se importe en otro módulo
    #     page = requests.get(url)
    #     soup = BeautifulSoup(page.content, "html.parser")
    #     def has_data_search(tag):
    #         return tag.has_attr("data-search-sol-meta")
    #
    #     results = soup.find_all(has_data_search)
    #
    #     for job in results:
    #         try:
    #             titleElement = job.find("a", attrs={"data-automation": "jobTitle"})
    #             title = titleElement.get_text()
    #             company = job.find("a", attrs={"data-automation": "jobCompany"}).get_text()
    #             joblink = "https://www.seek.co.nz" + titleElement["href"]
    #             salary = job.find("span", attrs={"data-automation": "jobSalary"})
    #             salary = salary.get_text() if salary else 'n/a'
    #
    #             job = "Titulo: {}\nEmpresa: {}\nSalario: {}\nLink: {}a\n"
    #
    #             job = job.format(title, company, salary, joblink)
    #
    #             print(job)
    #         except Exception as e:
    #             print("Exception: {}".format(e))
    #             pass


    # # Internet Speed tester
    # # pip install speedtest-cli
    # import speedtest as st
    # print('Speed test')
    # print('----------')
    # print('cargando...')
    # # Set Best Server
    # server = st.Speedtest()
    # server.get_best_server()
    # # Test Download Speed
    # down = server.download()
    # down = down / 1000000
    # print(f"Download Speed: {down} Mb/s")
    #
    # # Test Upload Speed
    # up = server.upload()
    # up = up / 1000000
    # print(f"Upload Speed: {up} Mb/s")
    #
    # # Test Ping
    # ping = server.results.ping
    # print(f"Ping Speed: {ping}")

