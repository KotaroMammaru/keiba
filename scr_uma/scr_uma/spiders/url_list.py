urls_list = []

# urls_list = ['202106040801', '202106040802', '202106040803', '202106040804', '202106040805']
url_1 = "2019" + "06"

for j in range (1, 6):
    url_2 = url_1 +"0" + str(j)

    for k in range (1, 10):
        url_3 = url_2 + "0" + str(k)

        for l in range (1, 13):
            if l < 10:
                post_url = url_3 + "0" + str(l)
            
            else:
                post_url = url_3 + str(l)
            
            urls_list.append(post_url)

