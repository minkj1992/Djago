# 전반적인 계획
- Django(python web framework)를 활용하여 웹 서비스를 제공한다.
- Keras를 통하여 User가 upload한 image 파일을 분석한 뒤, 시각화 페이지에서 stat을 시각화 한다.


# 구현해야 하는 기능
- Input
    - User의 사진을 upload 하는 기능
    - Upload된 이미지를 저장 할 수 있는 database(model in MTV model)
    
- Output
    - Analized data from keras model
    - Visualizing with sth beautiful


# 페이지별 분류 

- Main page: 프로젝트의 목적을 알린다.
    
- Upload page: 
    - 유저의 기본적인 인적사항을 적을 수 있는 페이지(시간이 남는다면 사주팔자 구현)
    - 유저의 사진을 올릴 수 있는 페이지
    - 데이터 분석하는 동안 loading .gif를 보여주도록 한다.
    
 - result page:
    - 유저의 사진과 분석에 주로 사용된 부위를 highlight
    - 사진 옆에는 6가지 stat에 대한 확률을 6각형 도표로 보여준다.
    - 해당 6가지 stat에 대한 유사한 유명인 사진을 보여준다.
    
 # 진행사항
 
1. [장고철학](https://github.com/minkj1992/Djago/blob/master/Basic-0-0-Django.md)
2. [장고 setting](https://github.com/minkj1992/Djago/blob/master/Basic-0-1-Setting.md)
3. [terminal command for Django](https://github.com/minkj1992/Djago/blob/master/Basic-0-2-Cheat_sheet.md)
4. [Hello World](https://github.com/minkj1992/Djago/blob/master/Basic-1-1-Hello_World.md)
5. [MTV pattern](https://github.com/minkj1992/Djago/blob/master/Basic-1-2-MVT_Pattern.md)
6. [first dump prject](https://github.com/minkj1992/Djago/blob/master/Basic-2-1-word_counter1.md)
7. [first dump prject2](https://github.com/minkj1992/Djago/blob/master/Basic-2-2-Word_counter2.md)
8. [first dump prject3](https://github.com/minkj1992/Djago/blob/master/Basic-2-3-Word_counter3.md)
9. [free Html5 with Django](https://github.com/minkj1992/Djago/blob/master/Django_Html5_templates.md)

# 공부할 사항
1. 이미지 업로드 page 구현
2. view에서 업로드한 이미지 데이터베이스 저장법.
3. keras 모델과 Django 연동 


    
