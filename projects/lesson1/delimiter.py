def get_summ(one, two, delimiter='&'):
    one=str(one).capitalize()
    two=str(two).capitalize()
    new_stat='{}{}{}'.format(one,delimiter,two)
    print(new_stat)
get_summ("learn","python")