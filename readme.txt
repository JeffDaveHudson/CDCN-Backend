/rating : lấy ra tất cả book đã được rating(user nào rating book nào)

/rating/id: lấy ra id của object rating (not need to use)

/ratingbyuser/id_user : lấy ra book được user rating
[
    {
        "id": 2,
        "user": 1,
        "book": 1,
        "rating": 5
    },
    {
        "id": 3,
        "user": 1,
        "book": 1,
        "rating": 4
    },
    {
        "id": 7,
        "user": 1,
        "book": 10,
        "rating": 3
    }
]

/ratingavg: lấy ra thông tin về avg_rating và rating_count của book
[
    {
        "book": 1,
        "avg_rating": 4.5,
        "count_rating": 2
    },
    {
        "book": 6,
        "avg_rating": 3.0,
        "count_rating": 2
    },
    {
        "book": 10,
        "avg_rating": 3.0,
        "count_rating": 1
    }
]

/user: lấy ra tất cả thông tin user
[
    {
        "id": 1,
        "username": "cuongphan",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2022-05-08T07:30:37Z"
    },
    {
        "id": 2,
        "username": "admin",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2022-05-08T08:00:30.796104Z"
    }
]

/user/1: lấy user bằng id user
{
    "id": 1,
    "username": "cuongphan",
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_staff": true,
    "is_active": true,
    "date_joined": "2022-05-08T07:30:37Z"
}

UPDATE USER:
Ex:
    {
"first_name": "toan" 
    }
với method= patch(update trường nào thì chỉ cần ghi trường đó)