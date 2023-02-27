coments = {}

while True:
    input_st = input()
    if not input_st:
        break
    name, comment = input_st.split(':')
    coments[name] = comment

    print(coments)
    print(len(coments))
