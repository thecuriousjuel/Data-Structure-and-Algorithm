def function(i, data):
    print(data)
    data.append(i)

    for i in range(5):
        function(i, data)



function(0, [])