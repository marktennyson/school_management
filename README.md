## Simple school management system with RestAPI

### all apis endpoint:

##### The endpoint to get a particular student
```http
GET /api/student/?id=1
```
and the response is:

```javascript
{
    "id": 1,
    "name": "Aniket Sarkar",
    "standerd": "Ten",
    "roll_no": 56,
    "gender": "M",
    "dob": "2021-08-10",
    "created_at": "2021-08-14T09:35:55.239Z",
    "is_active": true
}
```

##### The endpoint to get all student data
```http
GET /api/student/
```
and the response is:

```javascript
[
    {
        "id": 1,
        "name": "Aniket Sarkar",
        "standerd": "Ten",
        "roll_no": 56,
        "gender": "M",
        "dob": "2021-08-10",
        "created_at": "2021-08-14T09:35:55.239Z",
        "is_active": true
    },
    {
        "id": 2,
        "name": "Aditi Singh",
        "standerd": "Ten",
        "roll_no": 1,
        "gender": "M",
        "dob": "2021-08-10",
        "created_at": "2021-08-14T09:36:59.692Z",
        "is_active": true
    }
]
```

##### To create a student

```http
POST /api/student/
```

and the response is:
```javascript
{
    "id": 1,
    "name": "Aniket Sarkar",
    "standerd": "Ten",
    "roll_no": 56,
    "gender": "M",
    "dob": "2021-08-10",
    "created_at": "2021-08-14T09:35:55.239Z",
    "is_active": true
}
```

##### to update a student

```http
PUT /api/student/?id=1
```
and the response is:
```javascript
{
    "id": 1,
    "name": "Aniket Sarkar",
    "standerd": "Twelve",
    "roll_no": 57,
    "gender": "M",
    "dob": "2021-08-10",
    "created_at": "2021-08-14T09:35:55.239Z",
    "is_active": true
}
```

##### to delete a student

```http
DELETE /api/student/?id=1
```

and the response is:

```http
204 - Content not found
```