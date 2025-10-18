def __sorter(items):
    return items["num"]

def get_num_words(book_text):
    book_words = book_text.split()
    return len(book_words)

def get_character_count(text: str):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_sorted_char_dict(text):
    char_dict = get_character_count(text)
    dict_list = []
    for char in char_dict:
        paired_dict = {}
        paired_dict["char"] = char
        paired_dict["num"] = char_dict[char]
        dict_list.append(paired_dict)
    dict_list.sort(reverse=True, key=__sorter)
    return dict_list


"""
test_text = "Schedule 1 MixesPersonal Use BuffGrandaddy PurpleEnergy DrinkParacetamolCheap Early Mix	OG Kush		Banana		Cuke		BananaBest Sell Price 4-step mixesCocaine/Meth	Banana	Cuke	Horse Semen	Mega BeanOG Kush	Addy	Horse Semen	Cuke	Mega BeanSour Diesel	Iodine	Horse Semen	Addy	ViagraGreen Crack	Addy	Horse Semen	Mega Bean	ViagraGranddaddy Purple	Addy	Horse Semen	Viagra	IodineBest Profit 4-step mixesCocaine/Meth	Banana	Cuke	Horse Semen	Mega BeanOG Kush	Mega Bean	Banana	Cuke	ViagraSour Diesel	Cuke	Mega Bean	Iodine	Motor OilGreen Crack	Gasoline	Cuke	Viagra	Mega BeanGranddaddy Purple	Banana	Cuke	Horse Semen	Mega BeanDealer Optimized List	Benji - Northtown		Chloe Bowers		Beth Penn		Ludwig Meyer		Donna Martin		Mick Lubbin		Kathy Henderson		Austin Steiner		Kyle Cooley	Molly - Westville		Doris Lubbin		Meg Cooley		Trent Sherman		Kieth Wagner		Joyce Ball		Charles Rowland		Kim Delaney		Jerry Montero	Brad - Downtown		Kevin Oakley		Jeff Gilmore		Randy Caulfield		Lucy Pennington		Jennifer Rivera		Eugene Buckley		Louis Fourier		Elizabeth Homley	Jane - Docks		Lisa Gardener		Javier Perez		Genghis Barn		Marco Barone		Billy Kramer		Anna Chesterfield		Mac Cooper		Melissa Wood	Wei - Suburbia		Jeremy Wilkinson		Hank Stevenson		Carl Bundy		Jack Knight		Dennis Kennedy		Alison Knight		Karen Kennedy		Chris Sullivan	Leo - Uptown		Mrs. Ming		Sam Thompson		Peggy Myers		Peter File		Philip Wentworth		Greg Figgle		Cranky Frank		Harold ColtWeed Bungalow Restock	Dan's Hardware		30x Extra LongLife Soil		90x Fertilizer	Albert Hoover		90x Granddaddy PurpleMixing Stash & Dash Restock	Gas-Mart (West)		80x Banana		80x Cuke		80x Horse Semen		80x Mega Bean"

def testrun():
    result = get_report(test_text)
    print(result)

testrun()
"""
#"""