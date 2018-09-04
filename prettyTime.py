
special_set = {(1,23),(12,34),
               (3,21),
               (0,0),(1,11),(2,22),(3,33),(4,44),(5,55),
               (11,22),(11,33),(11,44),(11,55),
               (22,11),(22,33),(22,44),(22,55)}

def isTimePretty(time):
    print str(time.hour).zfill(2),':',str(time.minute).zfill(2)
    h_dig = time.hour
    m_dig = time.minute
    h_str = str(h_dig)
    m_str = str(m_dig).zfill(2)

    if h_dig == m_dig:
        return True
    if h_str == m_str[::-1]:
        return True
    if (h_dig,m_dig) in special_set:
        return True
    return False



if __name__ == "__main__":
    from datetime import datetime
    print datetime(2011, 8, 15, 0, 0, 0, 0)

    print isTimePretty(datetime(2011, 8, 21, 21, 12, 0, 0))
