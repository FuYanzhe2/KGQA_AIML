file_movie = open("movie_name.txt","r")
file_person = open("person_name.txt","r")
dict_file = open("movie_dict.txt","w")

for line in file_movie.readlines():
    line_ =line.decode('utf-8').strip().split()
    if len(line_)>1:
        continue
    else:
        dict_file.write(line_[0].encode('utf-8')+" mn"+'\n')

for line in file_person.readlines():
    if line=='\\N\n':
        continue
    line_ =line.decode('utf-8').strip().split()
    if len(line_)>1:
        continue
    else:
        dict_file.write(line_[0].encode('utf-8')+" n"+'\n')