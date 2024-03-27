import random
import numpy as np

sabjects = ['სახელი გვარი', 'ქართ', 'მათ', 'ინგლ', 'გეოგრ', 'ისტ']

names = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ', 'კლარა', 'სიმონ', 'ანზორ', 'სოფია',
         'სოსო', 'ნელი', 'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა', 'იზოლდა', 'ომარ', 'ტატიანა',
         'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან', 'სიმონ', 'ნელი', 'ბადრი', 'მადონა', 'ირინე', 'მინდია',
         'ნათია', 'გულნარა', 'კახა', 'ელზა', 'როინ', 'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა',
         'გოჩა', 'მურმან']
surnames = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი', 'ბუჩუკური', 'ტყებუჩავა',
            'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა', 'ნაკაშიძე', 'ღურწკაია', 'გვაზავა',
            'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია', 'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე',
            'ხარაბაძე', 'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა', 'გულუა', 'ხალვაში',
            'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე',
            'ინასარიძე', 'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი']

name_surnames = []
for _ in range(100):
    name_surnames.append(random.choice(names)+' '+random.choice(surnames))

column_names = np.array(sabjects)
row_names = np.array(name_surnames).reshape(-1, 1)
only_data_array = np.random.randint(1, 101, size=(100, 5))
combined_array = np.hstack((row_names, only_data_array))
combined_array = np.vstack((column_names, combined_array))
print(combined_array)
print()

average = np.mean(only_data_array, axis=1)
max_value = np.max(average)
print(f' ყველაზე მაღალი საშუალო ქულის მქონე სტუდენტი {name_surnames[np.where(average == max_value)[0][0]]}  '
      f'ქულა={max_value}')
print()

print(f' მათემატიკაში ყველაზე მაღალი ქულის მქონი სტუდენტები ')
for item in np.where(only_data_array == np.max(only_data_array, axis=0)[1])[0]:
    print(f'       {name_surnames[item]}  ქულა={np.max(only_data_array, axis=0)[1]}')
print()

indices = np.where(only_data_array == np.min(only_data_array, axis=0)[1])[0]
print(f' მათემატიკაში ყველაზე დაბალი ქულის მქონი სტუდენტები ')
for item in indices:
    print(f'       {name_surnames[item]}  ქულა={np.min(only_data_array, axis=0)[1]}')
print()

print(f' ყველა სტუდენტი რომლის ინგლისურის ქულაც მეტია საშუალო ინგლისურის ქულაზე ='
      f' {np.mean(only_data_array, axis=0)[2]}')
for item in np.where(only_data_array[:, 2] > np.mean(only_data_array, axis=0)[2])[0]:
    print(f'       {name_surnames[item]}  ქულა={only_data_array[item][2]}')

