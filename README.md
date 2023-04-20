# Lab-8_Group20
### Aim: Python Unit Testing of login module

### Testing Framework 

Default testing framework of Django

As shown in screenshot, default testing framework of django can be initialized by calling setUp() function which creates a new Client.

### Testing Functions 

Test Case 1:

![image](https://user-images.githubusercontent.com/107960916/233367487-3750f533-b2d5-4d54-abfc-c4e6480b7b6d.png)

Test Case 2:

![image](https://user-images.githubusercontent.com/107960916/233383270-7377bc7d-9920-46ea-b601-4a4481442573.png)

Test Case 3:

![image](https://user-images.githubusercontent.com/107960916/233383362-6c597167-6233-4205-bba1-2676f74abae0.png)

Test Case 4:

![image](https://user-images.githubusercontent.com/107960916/233383439-0f875881-bc9f-4703-b3a9-ec0d8c1e0076.png)

Test Case 5:

![image](https://user-images.githubusercontent.com/107960916/233384066-d43814de-1b43-487d-bf9f-e59c883e459f.png)

Test Case 6:

![image](https://user-images.githubusercontent.com/107960916/233384226-207eef73-6ea7-488f-aaaf-a8c9088bd4b4.png)

Test Case 7:

![image](https://user-images.githubusercontent.com/107960916/233384365-a5cf5f6d-0024-486b-a11c-a8c7771c7e1c.png)

Test Case 8:

![image](https://user-images.githubusercontent.com/107960916/233385787-beb0bbf2-6bd0-44c1-8e69-972a1034e943.png)

Test Case 9:

![image](https://user-images.githubusercontent.com/107960916/233385891-c6999c05-2215-46b4-b1ff-1ad198b25eec.png)

Test Case 10:

![image](https://user-images.githubusercontent.com/107960916/233384963-4f2bf3f2-3bfe-476d-9dd3-359a93cdd85d.png)

Test Case 11:

![image](https://user-images.githubusercontent.com/107960916/233385406-3f8bf79c-56f5-4b89-88fd-f51752896cfc.png)

### Executing Testing functions individually:

Correct Test Case 1:

![image](https://user-images.githubusercontent.com/107960916/233386585-0d0cc99c-11a6-4879-ae27-14b4170ddbb3.png)

Incorrect Test Case 1:

![image](https://user-images.githubusercontent.com/107960916/233390858-cbb3a4c0-99b9-45b4-bbc6-69877f510408.png)

Correct Test Case 6:

![image](https://user-images.githubusercontent.com/107960916/233386729-6eab28ba-b1ad-4d11-8609-cfc65bb58812.png)

Inorrect Test Case 6:

![image](https://user-images.githubusercontent.com/107960916/233390698-2a837293-883b-418b-b4f9-09695c581e0e.png)

Correct Test Case 11

![image](https://user-images.githubusercontent.com/107960916/233386903-f7d7d7b1-83e4-48c4-a746-67de7c7497ad.png)

Incorrect Test Case 11:

![image](https://user-images.githubusercontent.com/107960916/233390527-0eacb6cd-4a1f-4d0c-8b9b-31094290da8f.png)

### Executing all testing functions together:

command used for executing all testing functions together is: python manage.py test

All test cases correct:

![image](https://user-images.githubusercontent.com/107960916/233387612-42a5f9cf-6ef1-4744-a38d-e1bbd2566863.png)

With 2 wrong test cases: test case 2 and test case 5

![image](https://user-images.githubusercontent.com/107960916/233389060-f182ab4b-5459-432a-8fce-7f02b08b2f9a.png)


### Login function code:


def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

        if 4 < len(username) < 15:
            for i in username:
                if i == ' ':
                    response = JsonResponse({'message': 'Login Unsuccessful'}, status=401)
                    return response
        else:
            response = JsonResponse({'message': 'Login Unsuccessful'}, status=401)
            return response

        if 8 < len(pass1) < 24:
            upperCase = False
            lowerCase = False
            number = False
            special = False

            for i in pass1:
                if i == ' ':
                    response = JsonResponse({'message': 'Login Unsuccessful'}, status=401)
                    return response
                if i.isupper():
                    upperCase = True
                if i.islower():
                    lowerCase = True
                if i.isdigit():
                    number = True
                if i in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|',
                         ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']:
                    special = True
            if upperCase and lowerCase and number and special:
                pass
            else:
                response = JsonResponse({'message': 'Login Unsuccessful'}, status=401)
                return response
        else:
            response = JsonResponse({'message': 'Login Unsuccessful'}, status=401)
            return response

        collections = db['crosswordApp_user']
        reply = collections.find_one({"username": username})

        # if username is not in database
        if reply is None:
            response = JsonResponse({'message': 'Login Unsuccessful'}, status=401)
            return response

        response = JsonResponse({'message': 'Login Successful'}, status=401)
        return response


