import json
import pprint

def get_json_format(dic):
    return json.dumps(dic)

def main():
    bio = {
    'name' : 'Muhamad Sutan Al Rasyid',
    'age' : 18,
    'address' : 'Lampung',
    'hobbies' : ['gaming','coding'],
    'is_married' : False,
    'list_school' : [
        {
            'name' : 'SDN 2 Bandar Agung',
            'year_in' : 2006,
            'year_out' : 2012,
            'major' : 'null'
        },
        {
            'name' : 'SMP IT Bustanul Ulum',
            'year_in' : 2012,
            'year_out' : 2015,
            'major' : 'null'
        },
        {
            'name' : 'SMAN 1 Terusan Nunyai',
            'year_in' : 2015,
            'year_out' : 2018,
            'major' : 'science'
        }
    ],    
    'skills' : 
    [
        {
            'skill_name' : 'coding skills',
            'level' : 'beginner'
        },
        {
            'skill_name' : 'english',
            'level' : 'advanced'
        }
    ],
    'interest_in_coding' : True,
}
    pprint.pprint(get_json_format(bio))

if __name__ == "__main__":
    main()